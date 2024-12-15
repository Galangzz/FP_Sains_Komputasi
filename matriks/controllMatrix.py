from inversDanLUDekomposisi.inversAndDekomposisi import invers_matriks
from inversDanLUDekomposisi.inversAndDekomposisi import dekomposisi_lu
from metodeIterasi.iterasiJacobi import jacobi_method
from metodeIterasi.iterasiGaussSeidel import gauss_seidel

def main():
    while True:
        print("\n=== Matrix ===")
        print("1. Invers Matriks")
        print("2. Dekomposisi LU")
        print("3. Iterasi Jacobi")    
        print("4. Iterasi Gauss-Seidel")    
        print("5. Exit")
        choice = int(input("Masukkan pilihan (1/2/3/4/5): "))

        if choice == 1:
            invers_matriks()
        elif choice == 2:
            dekomposisi_lu()
        elif choice == 3:
            jacobi_method()
        elif choice == 4:
            gauss_seidel()
        elif choice == 5:
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()