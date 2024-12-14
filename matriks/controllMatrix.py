from inversAndDekomposisi import *
from persamaan_non_linear import persNonL

def main():
    while True:
        print("\n=== Matrix ===")
        print("1. Invers Matriks")
        print("2. Dekomposisi LU")
        print("3. Exit")
        choice = int(input("Masukkan pilihan (1/2/3/4): "))

        if choice == 1:
            invers_matriks()
        elif choice == 2:
            dekomposisi_lu()
        elif choice == 3:
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()