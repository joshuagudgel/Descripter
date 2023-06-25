# pdfplumber analysis
# Description: 
# Review the output of pdfplumber and decide on 
# requirements for redesigning for movie scripts

import movie_script as m

from lib2to3.pgen2.token import NEWLINE
import pdfplumber
import os

# Helpers

### pdfplumber checks
def plumberPdfToText(path):
    with pdfplumber.open(path) as pdf:
        scriptText = ""
        #print(len(pdf.pages))
        for page in pdf.pages:
            if len(page.chars) == 0:
                continue
            #print(len(page.chars))
            currLine = page.chars[0]['y0']
            pageText = ""
            for c in page.chars:
                if c['y0'] != currLine:
                    pageText+='\n'
                currLine = c['y0']
                pageText+=c['text']
            scriptText += "\r------------------------------------------\r" + pageText
        return scriptText

def writeTextToFile(filename,pageText):
    # create subfolder and write output to file
    subfolder = r"C:\src\Descripter\pdfplumber_output"
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)
    
    # Define output file path
    filename = os.path.join(subfolder,filename)

    # Write output to file
    with open(filename + ".txt","w", encoding='utf-8') as f:
        f.write(pageText)

# movie script paths
knivesoutpath = r"C:\src\Descripter\movie_scripts\knivesout-script.pdf"
dunepath = r"C:\src\Descripter\movie_scripts\dune-script.pdf"
spiderversepath = r"C:\src\Descripter\movie_scripts\spiderverse-script.pdf"
departedpath = r"C:\src\Descripter\movie_scripts\departed-script.pdf"
everythingpath = r"C:\src\Descripter\movie_scripts\everything-script.pdf"
groundhogdaypath = r"C:\src\Descripter\movie_scripts\groundhogday-script.pdf"
inglouriouspath = r"C:\src\Descripter\movie_scripts\inglouriusbasterds-script.pdf"
lastnightpath = r"C:\src\Descripter\movie_scripts\lastnightinsoho-script.pdf"
nocountrypath = r"C:\src\Descripter\movie_scripts\nocountry-script.pdf"
hotfuzzpath = r"C:\src\Descripter\movie_scripts\hotfuzz-script.pdf"
parasitepath = r"C:\src\Descripter\movie_scripts\parasite-script.pdf"
interviewpath = r"C:\src\Descripter\movie_scripts\interview-script.pdf"
maverickpath = r"C:\src\Descripter\movie_scripts\maverick-script.pdf"
worldsendpath = r"C:\src\Descripter\movie_scripts\worldsend-script.pdf"
shaunofthedeadpath = r"C:\src\Descripter\movie_scripts\shaunofthedead-script.pdf"
frenchdispatchpath = r"C:\src\Descripter\movie_scripts\frenchdispatch-script.pdf"
fantasticmrfoxpath = r"C:\src\Descripter\movie_scripts\frenchdispatch-script.pdf"
grandbudapestpath = r"C:\src\Descripter\movie_scripts\grandbudapest-script.pdf"
jojorabbitpath = r"C:\src\Descripter\movie_scripts\jojorabbit-script.pdf"
interstellarpath = r"C:\src\Descripter\movie_scripts\interstellar-script.pdf"
inceptionpath = r"C:\src\Descripter\movie_scripts\inception-script.pdf"
glassonionpath = r"C:\src\Descripter\movie_scripts\glassonion-script.pdf"

# print output of char arrays in order for each page
print("Dune")
dunetext = plumberPdfToText(dunepath)
writeTextToFile("dune",dunetext)
print("Knives Out")
knivesouttext = plumberPdfToText(knivesoutpath)
writeTextToFile("knivesout",knivesouttext)
print("Spider Verse")
spiderversetext = plumberPdfToText(spiderversepath)
writeTextToFile("spiderverse",spiderversetext)
print("Departed")
departedtext = plumberPdfToText(departedpath)
writeTextToFile("departed",departedtext)
print("Everything Everywhere All At Once")
everythingtext = plumberPdfToText(everythingpath)
writeTextToFile("everything",everythingtext)
print("Groundhog Day")
groundhogdaytext = plumberPdfToText(groundhogdaypath)
writeTextToFile("groundhogday",groundhogdaytext)
print("Inglourious Basterds")
inglourioustext = plumberPdfToText(inglouriouspath)
writeTextToFile("inglouriousbasterds",inglourioustext)
print("Last Night In SOHO")
lastnighttext = plumberPdfToText(lastnightpath)
writeTextToFile("lastnightinsoho",lastnighttext)
print("No Country for Old Men")
nocountrytext = plumberPdfToText(nocountrypath)
writeTextToFile("nocountry",nocountrytext)
print("Hot Fuzz")
hotfuzztext = plumberPdfToText(hotfuzzpath)
writeTextToFile("hotfuzz",hotfuzztext)
print("Parasite")
parasitetext = plumberPdfToText(parasitepath)
writeTextToFile("parasite",parasitetext)
print("The Interview")
interviewtext = plumberPdfToText(interviewpath)
writeTextToFile("interview",interviewtext)
print("Top Gun: Maverick")
mavericktext = plumberPdfToText(maverickpath)
writeTextToFile("maverick",mavericktext)
print("The World's End")
worldsendtext = plumberPdfToText(worldsendpath)
writeTextToFile("worldsend",worldsendtext)
print("Shaun Of The Dead")
shaunofthedeadtext = plumberPdfToText(shaunofthedeadpath)
writeTextToFile("shaunofthedead",shaunofthedeadtext)
print("French Dispatch")
frenchDispatchText = plumberPdfToText(frenchdispatchpath)
writeTextToFile("frenchdispatch",frenchDispatchText)
print("The Grand Budapest")
grandbudapesttext = plumberPdfToText(grandbudapestpath)
writeTextToFile("grandbudapest",grandbudapesttext)
print("JoJo Rabbit")
jojorabbittext = plumberPdfToText(jojorabbitpath)
writeTextToFile("jojorabbit",jojorabbittext)
print("Interstellar")
interstellartext = plumberPdfToText(interstellarpath)
writeTextToFile("interstellar",interstellartext)
print("Inception")
inceptiontext = plumberPdfToText(inceptionpath)
writeTextToFile("inception",inceptiontext)
print("Glass Onion")
glassoniontext = plumberPdfToText(glassonionpath)
writeTextToFile("glassonion",glassoniontext)