from persNonL import tabelMethod
from persNonL import biseksiMethod
from persNonL import regulaFalsiMethod
from persNonL import simpleIterationMethod
from persNonL import newtonRaphsonMethod
from persNonL import secantMethod

def main():
    while True:
        print("\nPilih metode:")
        print("1. Metode Tabel")
        print("2. Metode Biseksi")
        print("3. Metode Regula Falsi")
        print("4. Metode Iterasi Sederhana")
        print("5. Metode Newton-Raphson")
        print("6. Metode Secant")
        print("7. Exit")
        choice = int(input("Masukkan pilihan (1/2/3/4/5/6/7): "))

        if choice == 1:
            tabelMethod.metode_tabel()
        elif choice == 2:
            biseksiMethod.metode_biseksi()
        elif choice == 3:
            regulaFalsiMethod.metode_regula_falsi()
        elif choice == 4:
            simpleIterationMethod.simple_iteration_method()
        elif choice == 5:
            newtonRaphsonMethod.newton_raphson()
        elif choice == 6:
            secantMethod.secant_method()
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
