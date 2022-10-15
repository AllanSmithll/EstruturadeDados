# 10/10/2022
# Contagem de caracteres, trabalhar com arrays

def lengthStr(str) -> int:
  if (str == ''):
    return 0
  else:
    return 1 + lengthStr(str[1:])

string = "Allan"
print(lengthStr(string))