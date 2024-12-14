from persNonL import *

def main():
    while True:
        print("\nPilih metode:")
        print("1. Iterasi Sederhana")
        print("2. Newton-Raphson")
        print("3. Secant")
        print("4. Exit")
        choice = int(input("Masukkan pilihan (1/2/3/4): "))

        if choice == 1:
            simple_iteration_terminal()
        elif choice == 2:
            newton_raphson()
        elif choice == 3:
            secant_terminal()
        elif choice == 4:
            break;
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
