import numpy as np
from scipy.linalg import lu

# Fungsi untuk menghitung invers matriks
def invers_matriks():
    print("\n== Invers Matriks ==\n")
    a = input_matriks()
    try:
        inv_matrix = np.linalg.inv(a)
        print(inv_matrix) 
    except np.linalg.LinAlgError:
        return "Matriks tidak dapat diinvers karena singular (determinannya 0)."

# Fungsi untuk melakukan dekomposisi LU
def dekomposisi_lu():
    print("\n== Dekomposisi LU ==\n")
    a = input_matriks()
    P, L, U = lu(a)
    print("Matriks L (Lower Triangular):")
    print(L)
    print("Matriks U (Upper Triangular):")
    print(U)

# Input matriks
def input_matriks():
    print("Masukkan ukuran matriks (misal 3x3):")
    n = int(input("Ukuran matriks: "))
    matrix = []
    
    print(f"Masukkan elemen-elemen matriks {n}x{n}:")
    for i in range(n):
        row = list(map(float, input(f"Baris {i+1}: ").split()))
        matrix.append(row)
    
    return np.array(matrix)



