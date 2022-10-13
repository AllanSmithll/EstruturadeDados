# 10/10/2022

def n_numbers(n):
  '''Exibe na tela os números de 0 a n'''
  if n < 0:
    return
  n_numbers(n-1)
  print(n, end=' ')

# Programa principal
n = 10
n_numbers(n)