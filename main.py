import movie_script as m

from lib2to3.pgen2.token import NEWLINE
import pdfplumber

# Helpers

### pdfplumber checks
def plumberPageToText(path, pageNo):
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[pageNo]
        pageText = ""
        currLine = page.chars[0]['y0']
        for c in page.chars:
            if c['y0'] != currLine:
                print(c['y0'])
                pageText+='\n'
            currLine = c['y0']
            pageText+=c['text']
        return pageText

def writeTextToFile(filename,pageText):
    f = open(filename + ".txt","w+")
    f.write(pageText)
    f.close()

# main
knivesOutPath = r"C:\src\Descripter\movie_scripts\knivesout-script.pdf"
dunePath = r"C:\src\Descripter\movie_scripts\dune-script.pdf"
spiderVersePath = r"C:\src\Descripter\movie_scripts\spiderverse-script.pdf"
"""
script = m.MovieScript(path)
pdf = script.getPdf()
"""

#knivesOutPageText = plumberPageToText(knivesOutPath,2)
#writeTextToFile("knivesout",knivesOutPageText)

#spiderVersePageText = plumberPageToText(spiderVersePath,2)
#writeTextToFile("spiderverse",spiderVersePageText)

dunePageText = plumberPageToText(dunePath,4)
writeTextToFile("dune",dunePageText)


### display cast
"""
cast = script.getCast()
cast.sort()
print(cast)
"""

# display text from page
"""
pageText = ""
pageNumber = 2
for c in pdf[pageNumber].chars:
    pageText += c['text']
#print(pageText)
"""

### display cast and dialogue from one character
"""
for castMember in knivesOutScript.cast:
    if castMember == 'WALT':
        print(knivesOutScript.dialogue[castMember])
"""