import re

frase = "criticidad es baja"
buscar =  re.findall(r"criticidad|baja", frase)
print(len(buscar), buscar)