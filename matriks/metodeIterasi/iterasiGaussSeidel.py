from inputMatriks import input_matriks
def gauss_seidel():
    try:
        print("\n=== Program Iterasi Gauss-Seidel ===")
        matrix = input_matriks()

        print("Masukkan elemen-elemen vektor konstanta:")
        constants = list(map(float, input().split()))

        print("Masukkan tebakan awal:")
        initial_guess = list(map(float, input().split()))

        print("Masukkan toleransi kesalahan: ", end="")
        tolerance = float(input())

        print("Masukkan jumlah iterasi maksimum: ", end="")
        max_iterations = int(input())

        n = len(matrix)
        x = initial_guess.copy()

        for iteration in range(max_iterations):
            x_new = x.copy()

            for i in range(n):
                # Calculate the sum of known values
                sum1 = sum(matrix[i][j] * x_new[j] for j in range(i))
                sum2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))

                # Update the current variable's value
                x_new[i] = (constants[i] - sum1 - sum2) / matrix[i][i]

            # Check for convergence
            error = max(abs(x_new[i] - x[i]) for i in range(n))
            if error < tolerance:
                print(f"Converged after {iteration + 1} iterations.")
                print("\nHasil akhir:")
                for i, val in enumerate(x_new):
                    print(f"x[{i + 1}] = {val:.6f}")
                return

            x = x_new

        print("Maximum iterations reached without convergence.")
        print("\nHasil akhir:")
        for i, val in enumerate(x):
            print(f"x[{i + 1}] = {val:.6f}")
    except ValueError:
        print("Input tidak valid. Pastikan semua data yang dimasukkan adalah angka.")
    except ZeroDivisionError:
        print("Terjadi pembagian dengan nol. Pastikan elemen diagonal matriks tidak bernilai nol.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")