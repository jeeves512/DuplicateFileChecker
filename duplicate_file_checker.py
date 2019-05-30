import hashlib
import os

def hashfile(path, blocksize = 128):
    file = open(path, 'rb')
    hash = hashlib.sha256()
    buf = file.read(blocksize)
    while len(buf) > 0:
        hash.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hash.hexdigest()  # returns string containing hexadecimal digits


def findDuplicates(parentFolder):
    # Dups in format {hash:[names]}
    duplicates = {}
    dupSize = {}  # stores file size and file hash
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in duplicates and os.path.getsize(path) == dupSize[file_hash]:
                duplicates[file_hash].append(path)
            else:
                duplicates[file_hash] = [path]
                dupSize[file_hash] = os.path.getsize(path)
    return duplicates


def mergeDictionaries(dictionary1,dictionary2):
        for hashvalue in dictionary2.keys():
            if hashvalue in dictionary1:
                dictionary1[hashvalue] = dictionary1[hashvalue] + dictionary2[hashvalue]
            else:
                dictionary1[hashvalue] = dictionary2[hashvalue]


def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
    else:
        print('No duplicate files found.')

dups = {}
folders = 'C:\\Users\\Jeeves\\Desktop\\folder','C:\\Users\\Jeeves\\Desktop\\folder', 'C:\\Users\\Jeeves\\Desktop\\folder'
if isinstance(folders,str) == False:
    for i in folders:
        # Iterate the folders given
        if os.path.exists(i):
            # Find the duplicated files and append them to the dups
            mergeDictionaries(dups, findDuplicates(i))
        else:
            print('%s is not a valid path, please verify' % i)
    printResults(dups)
else:
    printResults(findDuplicates(folders))

