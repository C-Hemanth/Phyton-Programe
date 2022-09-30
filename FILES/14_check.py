file1='this.txt'
file2='copy.txt'
# file2='loge.txt'

with open (file1)as f:
    f1=f.read()
with open (file2)as f:
    f2=f.read()

if f1==f2:
    print('yes')
else:
    print('no')
