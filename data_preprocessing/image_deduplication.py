import os


path = './data/extracted_data/ikea_processed_data/images/'
files = os.listdir(path)
print(len(files))

def find_duplicates(string_list):
    # Dictionary to store the count of each string
    string_count = {}
    
    # List to store duplicate strings
    duplicates = []
    
    # Count occurrences of each string
    for string in string_list:
        if string in string_count:
            string_count[string] += 1
        else:
            string_count[string] = 1
    
    # Identify duplicates
    for string, count in string_count.items():
        if count > 1:
            duplicates.append(string)
    
    return duplicates

duplicates = find_duplicates(files)
print(duplicates)

## Need to include this function in the main call