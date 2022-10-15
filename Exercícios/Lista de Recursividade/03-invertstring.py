# 15/10/2022
# Inverter qualquer string com recursão

def invertString(str) -> str:
    if (str == ''):
        return
    n = str[0]
    print(n, end='')
    print(invertString(str[:]))

string = "Allan"
print(invertString(string))