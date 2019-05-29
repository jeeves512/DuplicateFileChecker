import hashlib
import os
file1 = open("a.txt",'rb')
file2 = open("a.txt",'rb')

def hashfile(path, blocksize = 65536):
    file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hasher.hexdigest()

hash_file1 = hashfile("a.txt")
hash_file2 = hashfile("b.txt")
#os.stat('a.txt') gets all info about given file
file1_size = os.path.getsize('a.txt')
file2_size = os.path.getsize('b.txt')
print(hash_file1,hash_file2)
print(file1_size,file2_size)
if((hash_file1 == hash_file2) and (file1_size == file2_size)):
  print('duplicate')
else:
  print('different')