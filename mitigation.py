import os,sys,stat

# set file permissions for owner
os.chmod("/home/sec-lab/critical", stat.S_IREAD)
print("Successful")
