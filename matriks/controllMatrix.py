from inversDanLUDekomposisi.inversAndDekomposisi import invers_matriks
from inversDanLUDekomposisi.inversAndDekomposisi import dekomposisi_lu
from metodeIterasi.iterasiJacobi import jacobi_method
from metodeIterasi.iterasiGaussSeidel import gauss_seidel
from operasiMatrix.matrixOperation import matrix_Operation
def main():
    while True:
        print("\n=== Matrix ===")
        print("1. Operasi Matriks")
        print("2. Invers Matriks")
        print("3. Dekomposisi LU")
        print("4. Iterasi Jacobi")    
        print("5. Iterasi Gauss-Seidel")    
        print("6. Exit")
        choice = int(input("Masukkan pilihan (1/2/3/4/5/6): "))

        if choice == 1:
            matrix_Operation()
        elif choice == 2:
            invers_matriks()
        elif choice == 3:
            dekomposisi_lu()
        elif choice == 4:
            jacobi_method()
        elif choice == 5:
            gauss_seidel()
        elif choice == 6:
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()