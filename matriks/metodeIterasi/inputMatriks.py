import numpy as np

def input_matriks():
    print("Masukkan ukuran matriks (misal 3x3):")
    n = int(input("Ukuran matriks: "))
    matrix = []
    
    print(f"Masukkan elemen-elemen matriks {n}x{n}:")
    for i in range(n):
        row = list(map(float, input(f"Baris {i+1}: ").split()))
        matrix.append(row)
    
    return np.array(matrix)