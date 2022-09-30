with open ('this.txt',) as h:
    text=h.read()

with open ('copy.txt','w') as h:
    h.write(text)