'''# 15/10/2022
# Faz uma comparação de strings

def compareStr(str1, str2) -> int:
    if (str1 == '') and (str2 == ''):
        return
    print(str1[0], str2[0])
    print(compareStr(str1[1:], str2[1:]))

string1 = "Allan Gato"
string2 = "Allan Gostoso"
compareStr(string1, string2)'''