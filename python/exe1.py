persons ={"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry":{"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}
print("display the values:",persons)
per=persons["glossary"]
print(per["title"])
dec=per["GlossDiv"]
print(dec["title"])
print(dec["GlossList"])
person=dec["GlossList"]
print(person["GlossEntry"])
pa=person["GlossEntry"]
print(pa["GlossTerm"])
print(pa["GlossDef"])
div=pa["GlossDef"]
print(div["GlossSeeAlso"])
list=div["GlossSeeAlso"]
print(list[0])
print(list[-1])










