## Implantação de Buuble Sort

sample = [2, 345, 65, 8, 12, 15, 4, 21, 16, 18, 33, 28, 79, 1]

def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j] > v[j+1]):
                print(v)
                v[j], v[j+1] = v[j+1], v[j]

bubble_sort(sample)

print(sample)