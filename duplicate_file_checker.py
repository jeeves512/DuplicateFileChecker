import hashlib
import os


def hashfile(path, block_size=128):
    with open(path, 'rb') as file:
        hash = hashlib.sha256()
        buf = file.read(block_size)
        while len(buf) > 0:
            hash.update(buf)
            buf = file.read(block_size)
        # returns string containing hexadecimal digits
        return hash.hexdigest()


def find_duplicates(parent_folder):
    # Dups in format {hash:[names]}
    duplicates = {}
    # stores file size and file hash
    dup_size = {}
    for dirName, subdirs, fileList in os.walk(parent_folder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in duplicates and os.path.getsize(path) == dup_size[file_hash]:
                duplicates[file_hash].append(path)
            else:
                duplicates[file_hash] = [path]
                dup_size[file_hash] = os.path.getsize(path)
    return duplicates


def merge_dictionaries(dictionary1, dictionary2):
    for hash_value in dictionary2.keys():
        if hash_value in dictionary1:
            dictionary1[hash_value] = dictionary1[hash_value] + dictionary2[hash_value]
        else:
            dictionary1[hash_value] = dictionary2[hash_value]


def print_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicate Folders:')
        print('________     '*10)
        for result in results:
            for subresult in result:
                print(subresult)
            print('________     '*10)
    else:
        print('No duplicate files')


dups = {}
folder_name_one = 'C:\\Users\\jeevan.james\\Desktop\\new test folder one'
folder_name_two = 'C:\\Users\\jeevan.james\\Desktop\\new test folder two'
folders = folder_name_one, folder_name_two
if not isinstance(folders, str):
    for i in folders:
        # Iterate the folders given
        if os.path.exists(i):
            # Find the duplicated files and append them to the dups
            merge_dictionaries(dups, find_duplicates(i))
        else:
            print(f'{i} is not a valid path, please verify')
    print_results(dups)
else:
    print_results(find_duplicates(folders))
"""game theory inoves technolgy using HTML, JavaScipt, XML and other tools designed to aid your multimedia efforts
online. Learn how to create dynamic content for website design that will have the opportunity to show off your newly 
learned web development skills through the completion of a full website."""
