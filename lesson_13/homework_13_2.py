from pathlib import Path
import logging
import json

# Second task - JSON validation

def validate_json_files():

    logging.basicConfig(filename='json_nesterenko.log', level=logging.ERROR)

    directory = Path('./ideas_for_test/work_with_json/')
    files = directory.glob('*.json')  # Only select .json files

    for filepath in files:
        try:
            # Open the file with proper encoding (e.g., utf-8)
            with filepath.open('r', encoding='utf-8', errors='ignore') as file:
                json.load(file)  # Try loading the file as JSON
        except json.JSONDecodeError as e:
            # If the file is not valid JSON, log the error
            logging.error(f"Invalid JSON in {filepath.name}: {e}")
        except UnicodeDecodeError as e:
            # If a decoding error occurs, log the error
            logging.error(f"Encoding error in {filepath.name}: {e}")

validate_json_files()