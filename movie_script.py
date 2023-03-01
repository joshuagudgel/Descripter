# pdfplumber mvp
import pdfplumber

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

    # find names
    # populates cast list
    def findNames(pages):
        cast = []
        return cast

    # find dialogue
    # grabs lines and sorts them into a dictionary
    # with cast members as keys
    def findDialogue(pages, cast):
        dialogue = {}
        return dialogue