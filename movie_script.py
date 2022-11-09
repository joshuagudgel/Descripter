# pdfplumber mvp
from lib2to3.pgen2.token import NEWLINE
import pdfplumber
import re

# Module goals:
# Take PDF as an input and organize details
# such as cast list and lines by cast members
class MovieScript:
  def __init__(self, path):
    self.pdf = pdfplumber.open(path)
    self.cast = MovieScript.findNames(self.pdf.pages)
    self.dialogue = MovieScript.findDialogue(self.pdf.pages, self.cast)

  def extractText(self):
    runningString = ""
    for p in self.pdf.pages:
      runningString += p.extract_text()
    return runningString

  ################ Helpers ################
  # find names
  # populates cast list
  def findNames(pages):
    cast = []
    currentLine = 1000
    isName = False
    for p in pages:
      for c in range(0,len(p.chars)-1):
          if p.chars[c]['y0'] != currentLine:
              currentLine = p.chars[c]['y0']
              if p.chars[c]['x0'] >= 250 and p.chars[c]['x0'] <= 280:
                  isName = True
                  currentLine = p.chars[c]['y0']
                  addName = MovieScript.trimName(MovieScript.copyLine(p,c)).rstrip()
              if isName:
                  if addName not in cast:
                      cast.append(addName)
          isName = False
    return cast

  # find dialogue
  # grabs lines and sorts them into a dictionary
  # with cast members as keys
  def findDialogue(pages, cast):
    dialogue = {}
    for member in cast:
      dialogue[member] = []
    for p in pages:
      currentLine = p.chars[0]['y0']
      for c in range(0,len(p.chars)-1):
          if p.chars[c]['y0'] != currentLine:
              currentLine = p.chars[c]['y0']
              member = MovieScript.trimName(MovieScript.copyLine(p,c)).rstrip()
              if member in cast and c:
                  nextLinePos = MovieScript.nextLine(p,c) #TODO account for names at the end of a file
                  if(nextLinePos == -1):
                    line = ""
                  else:
                    line = MovieScript.recordLines(p,nextLinePos)
                  dialogue[member].append(line)
      return dialogue

  # find indentation of dialogue
  def findDialogueIndent(page):
    currentLine = page.chars[0]['y0']
    for c in range(0,len(page.chars)-1):
        if page.chars[c]['y0'] != currentLine:
            currentLine = page.chars[c]['y0']
            if page.chars[c]['x0'] >= 250 and page.chars[c]['x0'] <= 280:
                return page.chars[c]['x0']
    return -1

  def copyLine(page, pos):
    line =""
    currentLine = page.chars[pos]['y0']
    while pos < len(page.chars) and page.chars[pos]['y0'] == currentLine:
        line += page.chars[pos]['text']
        pos += 1
    return line

  def trimName(name):
    return re.sub(r'\([^()]*\)', '', name)

  #grab a word
  def grabName(page, pos):
    name = ""
    initialLine = page.chars[pos]['y0']
    if page.chars[pos]['x0'] >= 265 and page.chars[pos]['x0'] <= 275:
        while page.chars[pos]['text'].isupper() and initialLine == page.chars[pos]['y0']:
            name+=page.chars[pos]['text']
            if pos+1 < len(page.chars):
                pos+=1
                currentLetter = page.chars[pos]['text']
            else:
                break
    return name

  #returns the index of the first character on the next line
  # -1 if no next line
  def nextLine(page, pos):
    initialLine = page.chars[pos]['y0']
    while pos < len(page.chars) and page.chars[pos]['y0'] == initialLine:
        pos+=1
    if page.chars[pos]['y0'] < initialLine:
      return pos
    return -1

  # find dialogue - using dialogue indent
  # when it's a new line and the indent is the dialogue indent
  # record the following lines
  # TODO:incorporate next page for when lines carry over
  #def findDialogueWithIndent(page, nextPage, dialogueIndent):
  #    currentLine = page.chars[0]['y0']
  #    for c in range(0,len(page.chars)-1):
  #        if page.chars[c]['y0'] != currentLine and page.chars[c]['x0'] == dialogueIndent:
  #            currentLine = page.chars[c]['y0']
  #            name = trimName(copyLine(page,c)).rstrip()
  #            if name in dialogue:
  #                line = recordLines(page,nextLine(page,c))
  #                dialogue[name].append(line)
  #            else:
  #                line = recordLines(page,nextLine(page,c))
  #                dialogue[name] = [line]
  #    return dialogue

  def recordLines(page, pos):
    recordedLine = ""
    initialIndent = page.chars[pos]['x0']
    currentIndent = page.chars[pos]['x0']
    currentLineNumber = page.chars[pos]['y0']
    while initialIndent == currentIndent and pos < len(page.chars)-1:
        if currentLineNumber != page.chars[pos]['y0']:
            currentIndent = page.chars[pos]['x0']
            currentLineNumber = page.chars[pos]['y0']
            if currentIndent != initialIndent:
                break
            recordedLine += " "
        recordedLine += page.chars[pos]['text']
        currentLineNumber = page.chars[pos]['y0']
        pos += 1
    return recordedLine