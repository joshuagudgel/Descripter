import movie_script as m

path = r"C:\src\Descripter\movie_scripts\knivesout-script.pdf"
script = m.MovieScript(path)
pdf = script.getPdf()

### display cast
#print(script.getCast())

# display text from page

#pageText = ""
#pageNumber = 1
#for c in pdf[pageNumber].chars:
#    pageText += c['text']
#print(pageText[220])

### display cast and dialogue from one character
#for castMember in knivesOutScript.cast:
#    if castMember == 'WALT':
#        print(knivesOutScript.dialogue[castMember])

### write to txt file
#f = open("scriptText.txt","w+")
#f.write(pageText)
#f.close()

# find expected values to test movie_script.nextLine()
manorPos = script.findFirstWord(1,"MANOR")
manorNextLinePos = script.findFirstWord(1, "The")
unlitPos = script.findFirstWord(1, "Unlit")
unlitNextLinePos = script.findFirstWord(1, "arcane")
franPos = script.findFirstWord(1, "FRAN")
franNextLinePos = script.findFirstWord(1, "up")
deadPos = script.findFirstWord(1, "dead.")

print(manorPos)
print(manorNextLinePos)
print(unlitPos)
print(unlitNextLinePos)
print(franPos)
print(franNextLinePos)
print(deadPos)