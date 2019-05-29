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

a = hashfile("a.txt")
b = hashfile("b.txt")
#os.stat('a.txt')
a_size = os.path.getsize('a.txt')
b_size = os.path.getsize('b.txt')
print(a,b)
print(a_size,b_size)
if((a == b) and (a_size == b_size)):
  print('duplicate')
else:
  print('different')