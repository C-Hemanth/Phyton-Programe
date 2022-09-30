with open ('repla.txt','r') as g:
    text=g.read()

text = text.replace("donkey","name")

with open ('repla.txt','w') as g:
    g.write(text)


