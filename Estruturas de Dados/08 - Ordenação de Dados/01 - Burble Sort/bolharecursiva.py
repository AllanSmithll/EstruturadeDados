# 07/11/2022
# Técnica de bolha recursiva

def bolha(array, n):
    if n == 1:
        return
    troca = False
    for j in range(0, n-1):
        if array[j] > array[j-1]:
            array[j], array[j+1] = array[j+1], array[j]
            troca = True
    if not troca:
        return
    bolha(array, n-1)

v = [3, 4, 10, 43, 5, 3, 23]
print(f"Array original: {v}")
bolha(v, len(v))
print(f"Array ordenada: {v}")