try:
    idade = int("25 anos")
except Exception as e:
    print(e)
    print(e.__str__())