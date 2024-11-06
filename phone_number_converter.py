from typing import List

class Node:
    def __init__(self, word: str):
        self.word = word
        self.next = None

class HashTable:
    def __init__(self, size: int = 5003):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key: int) -> int:
        A = (5 ** 0.5 - 1) / 2  # approximately 0.6180
        return int(self.size * ((key * A) % 1))
    
    def _word_to_number(self, word: str) -> int:
        digit_map = {
            'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3',
            'G':'4', 'H':'4', 'I':'4', 'J':'5', 'K':'5', 'L':'5',
            'M':'6', 'N':'6', 'O':'6', 'P':'7', 'Q':'7', 'R':'7', 'S':'7',
            'T':'8', 'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9', 'Z':'9'
        }
        # Only use the first 10 characters of the word
        word = word[:10]
        return int(''.join(digit_map[c] for c in word.upper()))

    def insert(self, word: str) -> None:
        number = self._word_to_number(word)
        index = self._hash(number)
        
        new_node = Node(word)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            new_node.next = self.table[index]
            self.table[index] = new_node
        print(f"Inserted {word} at index {index} (number: {number})")

    def find(self, number: int) -> List[str]:
        index = self._hash(number)
        results = []
        
        print(f"Looking for number {number} at index {index}")
        current = self.table[index]
        while current:
            word_number = self._word_to_number(current.word)
            print(f"Comparing with word {current.word} (number: {word_number})")
            if word_number == number:
                results.append(current.word)
            current = current.next
        return results

    def print_contents(self):
        """Print all contents of the hash table"""
        print("\nHash Table Contents:")
        for i in range(self.size):
            current = self.table[i]
            if current is not None:
                words = []
                while current:
                    words.append(current.word)
                    current = current.next
                print(f"Index {i}: {words}")

class PhoneNumberConverter:
    def __init__(self):
        self.table_10 = HashTable()  # For 10-length words
        self.table_7 = HashTable()   # For 7-length words
        self.table_4 = HashTable()   # For 4-length words
        self.table_3 = HashTable()   # For 3-length words

    def test_absenteeism(self):
        """Specific test for ABSENTEEISM"""
        word = "ABSENTEEISM"
        number = "2273683347"
        
        print("\nTesting ABSENTEEISM conversion:")
        print("-" * 50)
        
        # Test word to number conversion
        digit_map = {
            'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3',
            'G':'4', 'H':'4', 'I':'4', 'J':'5', 'K':'5', 'L':'5',
            'M':'6', 'N':'6', 'O':'6', 'P':'7', 'Q':'7', 'R':'7', 'S':'7',
            'T':'8', 'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9', 'Z':'9'
        }
        
        print("\nChecking word to number conversion:")
        for i, char in enumerate(word):
            print(f"{char} -> {digit_map[char]}")
        
        # Insert the word
        print("\nInserting ABSENTEEISM into hash table...")
        self.table_10.insert(word)
        
        # Print table contents
        print("\nChecking hash table contents...")
        self.table_10.print_contents()
        
        # Try to find the number
        print("\nAttempting to find the number...")
        results = self.convert_number(number)
        print(f"Results: {results}")

    def load_words(self, filename: str) -> None:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    word = line.strip()
                    if not word.isalpha():
                        continue
                    
                    length = len(word)
                    if length == 10:
                        self.table_10.insert(word)
                    elif length == 7:
                        self.table_7.insert(word)
                    elif length == 4:
                        self.table_4.insert(word)
                    elif length == 3:
                        self.table_3.insert(word)
        except Exception as e:
            print(f"Error loading file {filename}: {e}")

    def convert_number(self, number: str) -> List[str]:
        results = []
        print(f"\nConverting number: {number}")
        
        # Try 10-digit words
        print("Checking 10-digit words...")
        full_words = self.table_10.find(int(number))
        if full_words:
            print(f"Found 10-digit words: {full_words}")
            results.extend([f"1-{word}" for word in full_words])
        else:
            print("No 10-digit words found")
            
        # If no results yet, try 7-digit
        if not results:
            print("\nChecking 7-digit words...")
            seven_digit = self.table_7.find(int(number[3:]))
            if seven_digit:
                print(f"Found 7-digit words: {seven_digit}")
                results.extend([f"1-{number[:3]}-{word}" for word in seven_digit])
            else:
                print("No 7-digit words found")
        
        # If still no results, try 3-4 combinations
        if not results:
            print("\nChecking 3-4 digit combinations...")
            three_digit = self.table_3.find(int(number[3:6]))
            four_digit = self.table_4.find(int(number[6:]))
            if three_digit and four_digit:
                for word3 in three_digit:
                    for word4 in four_digit:
                        results.append(f"1-{number[:3]}-{word3}-{word4}")
                print(f"Found combinations: {results}")
            else:
                print("No 3-4 digit combinations found")
                    
        # If no matches found, format the raw number
        if not results:
            print("\nNo word matches found, using numeric format")
            results.append(f"1-{number[:3]}-{number[3:6]}-{number[6:]}")
            
        return results