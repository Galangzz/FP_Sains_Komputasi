import numpy as np

def input_matrix():
    rows = int(input("Masukkan jumlah baris matriks: "))
    cols = int(input("Masukkan jumlah kolom matriks: "))
    print("Masukkan elemen matriks (baris demi baris, dipisahkan spasi):")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print("Jumlah elemen tidak sesuai, ulangi input baris.")
            return input_matrix()
        matrix.append(row)
    return np.array(matrix)

def matrix_Operation():
    while True:
        print("\nOperasi Matematika pada Matriks")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Transpos Matriks")
        print("5. Exit")

        pilihan = int(input("Pilih operasi (1/2/3/4): "))

        if pilihan in [1, 2, 3]:
            print("Matriks A:")
            A = input_matrix()
            print("Matriks B:")
            B = input_matrix()

            if pilihan == 1:
                if A.shape != B.shape:
                    print("Penjumlahan hanya bisa dilakukan pada matriks dengan ukuran yang sama.")
                else:
                    print("Hasil Penjumlahan Matriks:\n", A + B)

            elif pilihan == 2:
                if A.shape != B.shape:
                    print("Pengurangan hanya bisa dilakukan pada matriks dengan ukuran yang sama.")
                else:
                    print("Hasil Pengurangan Matriks:\n", A - B)

            elif pilihan == 3:
                if A.shape[1] != B.shape[0]:
                    print("Perkalian hanya bisa dilakukan jika jumlah kolom matriks A sama dengan jumlah baris matriks B.")
                else:
                    print("Hasil Perkalian Matriks:\n", np.dot(A, B))

        elif pilihan == 4:
            print("Matriks yang akan ditranspos:")
            A = input_matrix()
            print("Hasil Transpos Matriks:\n", A.T)
        elif pilihan == 5:
            break

        else:
            print("Pilihan tidak valid.")


