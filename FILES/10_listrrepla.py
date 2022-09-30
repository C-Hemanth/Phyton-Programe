words=['johnny depp','gal gadot','tom cruise']
with open ('replac.txt','r') as g:
    text=g.read()
    
for word in words:

    text = text.replace(word,"name")

with open ('replac.txt','w') as g:
    g.write(text)




