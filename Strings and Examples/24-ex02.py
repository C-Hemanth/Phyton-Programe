from types import DynamicClassAttribute


letter='''Dear <|Name|>,
you are selected
so plese join by the given date
Date:<|Date|>'''

name=input("Enter your name")
date=input("Enter your date")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)

print(letter)