import os
from .phone_converter import PhoneNumberConverter

def main():
    # Initialize converter
    converter = PhoneNumberConverter()
    
    # Get the path to dictionary.txt
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dictionary_path = os.path.join(current_dir, "data", "dictionary.txt")
    
    # Load the dictionary
    print("Loading dictionary...")
    converter.load_words(dictionary_path)
    print("Dictionary loaded successfully!")
    
    while True:
        # Get input from user
        number = input("\nEnter a 10-digit phone number (or 'q' to quit): ").strip()
        
        if number.lower() == 'q':
            break
            
        if not number.isdigit() or len(number) != 10:
            print("Error: Please enter a valid 10-digit number")
            continue
            
        # Convert the number
        results = converter.convert_number(number)
        
        # Print results
        print("\nPossible representations:")
        for result in results:
            print(f"  {result}")

if __name__ == "__main__":
    main()