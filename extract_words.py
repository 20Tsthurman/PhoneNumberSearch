import os
from docx import Document

def extract_words_from_docx(folder_path: str, output_file: str):
    """
    Extract words from all .docx files in the specified folder and save to a single text file.
    
    Args:
        folder_path: Path to the folder containing .docx files
        output_file: Name of the output text file
    """
    # Set to store unique words
    all_words = set()
    
    # Process each .docx file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            try:
                print(f"Processing {filename}...")
                file_path = os.path.join(folder_path, filename)
                doc = Document(file_path)
                
                # Extract words from each paragraph
                for paragraph in doc.paragraphs:
                    # Split paragraph text into words and add to set
                    words = paragraph.text.strip().split()
                    all_words.update(word.strip() for word in words if word.strip().isalpha())
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    # Write all words to output file
    print(f"\nWriting words to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(all_words):
            f.write(word + '\n')
    
    print(f"Successfully extracted {len(all_words)} unique words to {output_file}")

if __name__ == "__main__":
    # Adjust these paths based on your setup
    WORDS_FOLDER = "words"  # Change this to your folder name
    OUTPUT_FILE = "dictionary.txt"
    
    # Create absolute path from current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    words_path = os.path.join(current_dir, WORDS_FOLDER)
    
    # Extract words
    extract_words_from_docx(words_path, OUTPUT_FILE)