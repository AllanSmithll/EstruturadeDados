# 10/10/2022
# Contagem de caracteres, trabalhar com arrays

def lengthStr(str) -> int:
  if (str == ''):  # Caso base, se a string for vazia
    return 0
  else:
    return 1 + lengthStr(str[1:])  # Se tiver caracter, retorne 1 + o resultado da chamada de lengthStr, que contará a partir do próximo índice
                                   
string = "Allan"
print(lengthStr(string))