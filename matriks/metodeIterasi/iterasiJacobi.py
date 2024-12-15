import numpy as np
from inputMatriks import input_matriks

def jacobi_method():
    try:
        print("\n=== Program Iterasi Jacobi ===")
        print("Masukkan elemen matriks A:")
        A = input_matriks()

        print("Masukkan elemen vektor b:")
        b = list(map(float, input().split()))
        if len(b) != A.shape[1]:
            raise ValueError("Jumlah elemen vektor b tidak sesuai dengan ukuran matriks.")

        print("Masukkan nilai awal solusi (x0):")
        x0 = list(map(float, input().split()))
        if len(x0) != A.shape[1]:
            raise ValueError("Jumlah elemen x0 tidak sesuai dengan ukuran matriks.")

        max_iter = int(input("Masukkan jumlah iterasi maksimum: "))
        tol = float(input("Masukkan toleransi (epsilon): "))

        n = len(b)
        x = np.array(x0, dtype=float)

        for iteration in range(max_iter):
            x_new = np.zeros_like(x)

            for i in range(n):
                s = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - s) / A[i][i]

            # Check convergence
            if np.linalg.norm(x_new - x, ord=np.inf) < tol:
                print(f"Converged in {iteration + 1} iterations.")
                print("Hasil solusi:", x_new)
                return

            x = x_new

        print("Did not converge within the maximum number of iterations.")
        print("Hasil solusi terakhir:", x)
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")