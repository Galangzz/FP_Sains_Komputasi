import numpy as np
from inputMatriks import input_matriks
from scipy.linalg import lu

# Fungsi untuk menghitung invers matriks
def invers_matriks():
    print("\n== Invers Matriks ==\n")
    a = input_matriks()
    try:
        inv_matrix = np.linalg.inv(a)
        print(inv_matrix) 
    except np.linalg.LinAlgError:
        print("Matriks tidak dapat diinvers karena singular (determinannya 0).")

# Fungsi untuk melakukan dekomposisi LU
def dekomposisi_lu():
    print("\n== Dekomposisi LU ==\n")
    a = input_matriks()
    P, L, U = lu(a)
    print("Matriks L (Lower Triangular):")
    print(L)
    print("Matriks U (Upper Triangular):")
    print(U)





