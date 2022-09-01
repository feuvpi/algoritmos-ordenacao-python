# Ordenar o conjunto inseringo os elementos em um subconjunto já ordenado.

sample = [2, 345, 65, 8, 12, 15, 4, 21, 16, 18, 33, 28, 79, 1]

def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j>= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x

print(sample)
print(f'sorting {sample} with insertion algorithm...:')
insertion_sort(sample)
print(sample)
