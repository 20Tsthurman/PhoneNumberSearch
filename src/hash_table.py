# src/hash_table.py
import math

class Node:
    def __init__(self, word: str, phone_number: int):
        self.word = word
        self.phone_number = phone_number  # Store the phone number representation
        self.next = None

class HashTable:
    def __init__(self, size: int = 5003):
        """Initialize hash table with size m>=1000 (default 5003)"""
        self.size = size
        self.table = [None] * size  # Array of linked lists
        self.A = (math.sqrt(5) - 1) / 2  # approximately 0.6180
        
    def _word_to_number(self, word: str) -> int:
        """Convert a word to its phone number representation"""
        digit_map = {
            'A':'2', 'B':'2', 'C':'2',
            'D':'3', 'E':'3', 'F':'3',
            'G':'4', 'H':'4', 'I':'4',
            'J':'5', 'K':'5', 'L':'5',
            'M':'6', 'N':'6', 'O':'6',
            'P':'7', 'Q':'7', 'R':'7', 'S':'7',
            'T':'8', 'U':'8', 'V':'8',
            'W':'9', 'X':'9', 'Y':'9', 'Z':'9'
        }
        return int(''.join(digit_map[c] for c in word.upper()))

    def _hash(self, K: int) -> int:
        """
        Hash function h(K) = ⌊M(KA mod 1)⌋
        where A = (√5-1)/2 ≈ 0.6180
        """
        KA_mod_1 = (K * self.A) % 1  # Get fractional part
        return math.floor(self.size * KA_mod_1)

    def insert(self, word: str) -> None:
        """Insert a word into the hash table"""
        # Convert word to phone number
        phone_num = self._word_to_number(word)
        
        # Calculate hash index
        index = self._hash(phone_num)
        
        # Create new node
        new_node = Node(word, phone_num)
        
        # Insert at beginning of linked list (separate chaining)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            new_node.next = self.table[index]
            self.table[index] = new_node

    def find(self, number: int) -> list[str]:
        """Find all words that match a given phone number"""
        index = self._hash(number)
        
        # If index is empty (NILL)
        if self.table[index] is None:
            return []
            
        # Search the linked list at this index
        results = []
        current = self.table[index]
        while current:
            if current.phone_number == number:
                results.append(current.word)
            current = current.next
            
        return results
        
    def print_stats(self):
        """Print statistics about the hash table"""
        total_entries = 0
        max_chain = 0
        empty_slots = 0
        
        for i in range(self.size):
            if self.table[i] is None:
                empty_slots += 1
                continue
                
            # Count entries in this chain
            chain_length = 0
            current = self.table[i]
            while current:
                chain_length += 1
                current = current.next
                
            total_entries += chain_length
            max_chain = max(max_chain, chain_length)
        
        print(f"Hash Table Statistics:")
        print(f"Total size: {self.size}")
        print(f"Total entries: {total_entries}")
        print(f"Empty slots: {empty_slots}")
        print(f"Load factor: {total_entries/self.size:.2f}")
        print(f"Maximum chain length: {max_chain}")