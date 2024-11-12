# src/phone_converter.py

class PhoneNumberConverter:
    def __init__(self):
        """Initialize four separate hash tables as specified"""
        from .hash_table import HashTable
        
        # Create 4 hash tables as specified in requirements
        self.table_10 = HashTable(5003)  # Table1: words of length 10
        self.table_7 = HashTable(5003)   # Table2: words of length 7
        self.table_4 = HashTable(5003)   # Table3: words of length 4
        self.table_3 = HashTable(5003)   # Table4: words of length 3
        
    def load_words(self, filename: str) -> None:
        """Load words into appropriate hash tables based on length"""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    word = line.strip()
                    if not word.isalpha():
                        continue
                    
                    # Sort words into appropriate tables based on length
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
            print(f"Error loading dictionary: {e}")
            
    def print_table_stats(self):
        """Print statistics for all hash tables"""
        print("\nTable 1 (10-letter words):")
        self.table_10.print_stats()
        print("\nTable 2 (7-letter words):")
        self.table_7.print_stats()
        print("\nTable 3 (4-letter words):")
        self.table_4.print_stats()
        print("\nTable 4 (3-letter words):")
        self.table_3.print_stats()

    def convert_number(self, number: str) -> list[str]:
        """
        Convert phone number to words following the specified procedure:
        1. Look in Table1 for 10-digit matches
        2. If not found, look in Table2 for 7-digit matches
        3. If not found, try combinations of Table3 and Table4
        4. If no matches found, return formatted number
        """
        if not number.isdigit() or len(number) != 10:
            return ["Error: Please enter a valid 10-digit number"]
            
        results = []
        
        # 1. First try Table1 (10-digit words)
        ten_digit = self.table_10.find(int(number))
        if ten_digit:
            results.extend([f"1-{word}" for word in ten_digit])
            return results
            
        # 2. If no match in Table1, try Table2 (7-digit words)
        seven_digit = self.table_7.find(int(number[3:]))
        if seven_digit:
            results.extend([f"1-{number[:3]}-{word}" for word in seven_digit])
            return results
        
        # 3. If no match in Table2, try Table3 + Table4 combination
        three_digit = self.table_3.find(int(number[3:6]))
        four_digit = self.table_4.find(int(number[6:]))
        if three_digit and four_digit:
            for word3 in three_digit:
                for word4 in four_digit:
                    results.append(f"1-{number[:3]}-{word3}-{word4}")
            return results
                    
        # 4. If no matches found, format the raw number
        return [f"1-{number[:3]}-{number[3:6]}-{number[6:]}"]