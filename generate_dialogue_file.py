import movie_script as m
from pathlib import Path

# Helpers
def format_dialogue_dictionary(dialogue_dict):
    """Format the dialogue dictionary into a readable string."""
    output = "MOVIE SCRIPT CHARACTER DIALOGUE\n"
    output += "=============================\n\n"
    
    # Sort characters alphabetically for consistent output
    for character in sorted(dialogue_dict.keys()):
        output += f"CHARACTER: {character}\n"
        output += "----------------------------------------\n"
        
        # Add each line with a bullet point
        for i, line in enumerate(dialogue_dict[character], 1):
            output += f"{i}. \"{line}\"\n"
        
        output += "\n\n"
    
    return output

def save_dialogue_to_file(script_path, output_filename):
    """Process a script and save its dialogue to a text file."""
    try:
        # Load the script
        print(f"Processing script: {script_path}")
        script = m.MovieScript(script_path)
        
        # Format the dialogue dictionary
        formatted_dialogue = format_dialogue_dictionary(script.dialogue)
        
        # Save to file
        output_path = Path(output_filename).with_suffix('.txt')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted_dialogue)
        
        print(f"Dialogue saved to: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing script: {e}")
        return False

def main():
    # Get the directory containing the current script
    BASE_DIR = Path(__file__).parent
    
    # Reference files relative to the project
    knivesout_path = BASE_DIR / "movie_scripts" / "knivesout-script.pdf"
    
    # Generate dialogue file
    save_dialogue_to_file(knivesout_path, "knivesout_dialogue")

if __name__ == "__main__":
    main()