f=open('Hemu.txt')                    # read line  makes the txt to read to read only one line if we type read line again we get other line
data=f.readline()
print(data)
data=f.readline()
print(data)
f.close()