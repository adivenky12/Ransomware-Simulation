import pyAesCrypt
import glob
import os
# Encryption/decryption buffer size
bufferSize = 64 * 1024

# Get current directory
currentDir = os.getcwd()
# Prompt user for password to decrypt files
pwd = 'Ah@f781'
 

# code to decrypt all files recursively
for x in glob.glob('/home/sec-lab/critical/**/*', recursive=True):
    fullpath = os.path.join(currentDir, x)
    newpath = os.path.join(currentDir, os.path.splitext(x)[0])
    # Decryption code
    if os.path.isfile(fullpath):
        
        try:
            pyAesCrypt.decryptFile(fullpath, newpath, pwd, bufferSize)
            print('Decrypted File: \t' + newpath + '\n')
            os.remove(fullpath)    
        except ValueError:
            print('Wrong password!\n')