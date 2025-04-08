# Descripter

Descripter is a Python tool for extracting and organizing character dialogue from movie script PDFs. It parses movie scripts to identify character names and their corresponding dialogue, then outputs the data in a structured format.

# Features

- Extract character names from screenplay PDFs
- Organize dialogue by character
- Generate readable text output of dialogue

# Known Issues:

- Does not account for moments when two people are speaking at once.
- Pages from Knives Out are not documented and an error appears:
  "CropBox missing from /Page, defaulting to MediaBox".
- Dialogue appears to only be the first line on each dialogue block.
- Movie scripts are an initial guide for actors to follow. These lines are not exactly what is said in each movie.

# Project Structure

```text
descripter/
├── movie_script.py # Core script parser class
├── generate_dialogue_file.py # Script to generate dialogue text files
├── test_movie_script.py # Test file for movie_script
├── movie_scripts/ # Directory for movie script PDFs to process
│ └── knivesout-script.pdf
├── movie_scripts_outputs/ # Generated output files
│ └── knivesout_dialogue.txt
├── .gitignore # Git ignore file
└── README.md # Project documentation
```

Installation

1. Clone the repository:
   ```text
   git clone https://github.com/joshuagudgel/Descripter.git
   cd Descripter
   ```
2. Create a virtual environment
   ```text
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```text
   pip install pdfplumber
   ```

Usage

Process a movie script

```text
from movie_script import MovieScript
from pathlib import Path

# Load and parse a movie script

script_path = Path("movie_scripts/knivesout-script.pdf")
script = MovieScript(script_path)

# Get the list of characters

print(f"Characters: {script.cast}")

# Access dialogue by character

for character, lines in script.dialogue.items():
print(f"\n{character}:")
for line in lines:
print(f" - {line}")
```

Generate a dialogue file

```text
python generate_dialogue_file.py
```

License
MIT License
