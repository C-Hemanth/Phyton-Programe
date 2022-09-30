import os


oldfile='samp.txt'
newfile='pyth.txt'
with open (oldfile)as h:
    text=h.read()

with open(newfile,'w')as h:
    h.write(text)

os.remove(oldfile)