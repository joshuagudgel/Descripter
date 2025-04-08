# pdfplumber mvp
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

    # find names
    # populates cast list
    @staticmethod
    def findNames(pages):
        cast = set()
        
        # Pattern for character names - typically all caps followed by dialogue
        name_pattern = re.compile(r'^([A-Z][A-Z\s\']+)(?:\s*\(.*\))?\s*$')
        
        for page in pages:
            if page.extract_text() is None:
                continue
            
            lines = page.extract_text().split('\n')
            for line in lines:
                line = line.strip()
                match = name_pattern.match(line)
                if match:
                    character_name = match.group(1).strip()
                    # Filter out common headers and page numbers
                    if (len(character_name) > 1 and 
                        not character_name.isdigit() and
                        not character_name.startswith('CONTINUED') and
                        not character_name.startswith('PAGE')):
                        cast.add(character_name)
        
        return list(cast)

    # find dialogue
    # grabs lines and sorts them into a dictionary
    # with cast members as keys
    @staticmethod
    def findDialogue(pages, cast):
        dialogue = {character: [] for character in cast}
        current_character = None
        collecting_dialogue = False
        
        for page in pages:
            if page.extract_text() is None:
                continue
                
            lines = page.extract_text().split('\n')
            for line in lines:
                line = line.strip()
                
                # Check if this line is a character name
                if line in cast:
                    current_character = line
                    collecting_dialogue = True
                    continue
                    
                # If we're collecting dialogue and this isn't a direction
                if collecting_dialogue and current_character and line:
                    # Check if it's a stage direction (often in parentheses)
                    if not (line.startswith('(') and line.endswith(')')):
                        # Skip scene headings - typically ALL CAPS and contain INT/EXT
                        if not (line.isupper() and ('INT.' in line or 'EXT.' in line)):
                            dialogue[current_character].append(line)
                            collecting_dialogue = False
        
        # Clean up empty entries
        dialogue = {k: v for k, v in dialogue.items() if v}
        return dialogue