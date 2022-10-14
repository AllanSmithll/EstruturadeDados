# 14/10/2022
# Retorne a str 

def printstr(str) -> int:
  if (str == ''):
    return
  else:
    print(str[0], end='')
    print(printstr[1:])

# Programa Principal

str = "Aguarde sensacionais revelações"
print(str)