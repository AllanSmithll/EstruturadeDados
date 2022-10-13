# 10/10/2022
# Contagem de caracteres, trabalhar com arrays

def strLength(str, i=0) -> int:
  if i == len(str):
    return 0
  else: 
      return 1 + strLength(str, i + 1)

# Programa principal
print("Tamanho da string:", strLength('ifpb'))
