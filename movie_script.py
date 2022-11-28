# pdfplumber mvp
from lib2to3.pgen2.token import NEWLINE
import pdfplumber
import re

# Module goals:
# Take PDF as an input and organize details
# such as cast list and lines by cast members
class MovieScript:
  def __init__(self, path):
    self._pdf = pdfplumber.open(path).pages
    #self._cast = MovieScript.generateCast(self._pdf)
    #self._dialogue = MovieScript.generateDialogue(self._pdf, self._cast)

  def extractText(self):
    runningString = ""
    for p in self._pdf.pages:
      runningString += p.extract_text()
    return runningString
  
  def getPdf(self):
    return self._pdf
  
  def getCast(self):
    return self._cast

  # cycle through pages tracking blocks of dialogue and
  # parsing them into the dialogue object
  def generateDialogue(self):
    dialogue = {}
    # for every line in pdf seach for dialogue

      # if it is found then record the following line

    # begin searching for dialogue after previous line is recorded
    
    return dialogue

  # findNames
  # given a list of pages
  # return cast list
  def generateCast(self,pages):
    cast = []
    for p in range(0,len(pages)-1):
      currPage = self._pdf[p]
      c = 0
      while c < len(currPage.chars) - 1:
        # detectDialogue
        addName = MovieScript.detectDialogue(p,c)
        # if name in position then add to cast
        if addName:
          if addName not in cast:
              cast.append(addName)
        # increment to next line
        c = MovieScript.nextLine(p, c)
        if c == -1:
          break
    return cast

  # TODO remove after writing generateCast
  # if currPage.chars[c]['y0'] != currentLine:
  #        currentLine = currPage.chars[c]['y0']
  #        if currPage.chars[c]['x0'] >= 250 and currPage.chars[c]['x0'] <= 280:
  #          isName = True
  #          currentLine = currPage.chars[c]['y0']
  #          addName = MovieScript.trimName(MovieScript.copyLine(pages, p, c)).rstrip()
  #        if isName:
  #          if addName not in cast:
  #            cast.append(addName)
  #        isName = False
  
  ################ Helpers ################

  ### Parser methods for reading pdfplumber ###
  
  # detectDialogue
  # given
  # return the starting position of the dialogue text
  def detectDialogue(self):
    
    return
  
  # nextLine
  # given a current page index and character index
  # return index of the beginning of the next line
  # return -1 if OOB on page.chars[]
  def nextLine(self, pageNum, pos):
    newPos = pos
    currPage = self._pdf[pageNum]
    currLine = currPage.chars[newPos]['y0']
    while newPos < len(currPage.chars) and currPage.chars[newPos]['y0'] == currLine:
      newPos += 1
    if newPos == len(currPage.chars) or currLine < currPage.chars[newPos]['y0']:
      return -1
    return newPos

  ### Assist in adding dialogue ###
  
  # trimName
  # given name line
  # return cast member name
  def trimName(name):
    return re.sub(r'\([^()]*\)', '', name)

  # copyLine
  # given pageNum and pos
  # return the current line until new line or gap
  def copyLine(self, pageNum, pos):
    line =""
    pages = self._pdf
    currentLine = pages[pageNum].chars[pos]['y0']
    while pos < len(pages[pageNum].chars) and pages[pageNum].chars[pos]['y0'] == currentLine:
      line += pages[pageNum].chars[pos]['text']
      pos += 1
    return line

  ### Unit test support ###

  # findFirstWord
  # given targeted word
  # return index of first occurance
  def findFirstWord(self, pageNum, word):
    targetWord = list(word)
    #print(targetWord)
    compareWord = []
    page = self._pdf[pageNum]
    for i in range(0, len(page.chars)):
      # start recording characters to compare to target
      if i < len(word):
        compareWord.append(page.chars[i]['text'])
        continue
      # update compareWord
      compareWord.pop(0)
      compareWord.append(page.chars[i]['text'])
      # return when it matches
      if compareWord == targetWord:
        return i - (len(targetWord) - 1)
    return -1

  ##########################################
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
                  nextLinePos = MovieScript.nextLine(p,c) 
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

  # returns the index of the first character on the next line
  # -1 if no next line
  def nextLine_old(self, page, pos):
    if pos >= len(page.chars):
      return -1
    initialLine = page.chars[pos]['y0']
    while pos < len(page.chars) and page.chars[pos]['y0'] == initialLine:
      if page.chars[pos]['y0'] < initialLine:
        return pos
      pos += 1

    return -1

  # find dialogue - using dialogue indent
  # when it's a new line and the indent is the dialogue indent
  # record the following lines
  """
  def findDialogueWithIndent(page, nextPage, dialogueIndent):
      currentLine = page.chars[0]['y0']
      for c in range(0,len(page.chars)-1):
          if page.chars[c]['y0'] != currentLine and page.chars[c]['x0'] == dialogueIndent:
              currentLine = page.chars[c]['y0']
              name = trimName(copyLine(page,c)).rstrip()
              if name in dialogue:
                  line = recordLines(page,nextLine(page,c))
                  dialogue[name].append(line)
              else:
                  line = recordLines(page,nextLine(page,c))
                  dialogue[name] = [line]
      return dialogue
  """

  # reference for refactoring generateDialogue
  """
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
  """