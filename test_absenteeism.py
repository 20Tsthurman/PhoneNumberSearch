from phone_number_converter import PhoneNumberConverter

# Create test dictionary file with just ABSENTEEISM
with open('test_dict.txt', 'w') as f:
    f.write('ABSENTEEISM\n')

# Create converter and test
converter = PhoneNumberConverter()
converter.load_words('test_dict.txt')
converter.test_absenteeism()