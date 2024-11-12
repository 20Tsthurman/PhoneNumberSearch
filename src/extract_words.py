import os
from docx import Document

def extract_words(folder_path: str, output_file: str):
    """Extract words from both .docx files and .txt files"""
    all_words = set()
    
    # Process each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if filename.endswith('.docx'):
            try:
                print(f"Processing DOCX: {filename}")
                doc = Document(file_path)
                for paragraph in doc.paragraphs:
                    words = paragraph.text.strip().split()
                    all_words.update(word.strip() for word in words if word.strip().isalpha())
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
        elif filename.endswith('.txt'):
            try:
                print(f"Processing TXT: {filename}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        word = line.strip()
                        if word.isalpha():
                            all_words.add(word)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    # Write all words to output file
    print(f"\nWriting words to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(all_words):
            f.write(word + '\n')
    
    print(f"Successfully extracted {len(all_words)} unique words")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    words_path = os.path.join(current_dir, "words")
    output_file = os.path.join(current_dir, "data", "dictionary.txt")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    extract_words(words_path, output_file)
