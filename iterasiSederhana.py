import sympy as sp

def simple_iteration_terminal():
    # Input fungsi dalam format string
    g_str = input("Masukkan fungsi g(x) untuk Iterasi Sederhana: ")
    x0 = float(input("Masukkan tebakan awal (x0): "))
    tol = float(input("Masukkan toleransi error: "))
    max_iter = int(input("Masukkan jumlah iterasi maksimal: "))

    # Konversi string ke fungsi
    x = sp.symbols('x')
    try:
        g_ = sp.sympify(g_str)
    except sp.SympifyError:
        print("Fungsi tidak valid. Pastikan fungsi ditulis dengan benar.")
        return
    
    g = sp.lambdify(x, g_, 'numpy')
    
    x = x0
    for i in range(max_iter):
        try:
            x_next = g(x)
            print(f"Iterasi {i}: x = {x_next}, Error = {abs(x_next-x):.6e}")
        except OverflowError:
            print("Overflow terjadi. Fungsi tidak stabil.")
            return

        if abs(x_next - x) < tol:
            print(f"Akar ditemukan: {x_next}, Iterasi: {i + 1}")
            return
        x = x_next
    print("Metode tidak konvergen.")


def newton_raphson():
    # Input dari pengguna
    fx_str = input("Masukkan fungsi f(x): ")
    fx1_str = input("Masukkan fungsi f'(x): ")
    x0 = float(input("Masukkan tebakan awal (x0): "))
    tol = float(input("Masukkan toleransi error: "))
    max_iter = int(input("Masukkan iterasi maksimal: "))

    x = sp.symbols('x')
    try:
        fx = sp.sympify(fx_str)
        fx_aksen = sp.sympify(fx1_str)
    except sp.SympifyError:
        print("Fungsi tidak valid. Pastikan fungsi ditulis dengan benar.")
        return


    f_x = sp.lambdify(x, fx, 'numpy')
    f_x_aksen = sp.lambdify(x, fx_aksen, 'numpy')

    iteration = 0
    while iteration < max_iter:
        fx_value = f_x(x0)
        fx_aksen_value = f_x_aksen(x0)

        if fx_aksen_value == 0:
            print("Turunan sama dengan nol, solusi tidak ditemukan.")
            return

        x_next = x0 - fx_value / fx_aksen_value
        error = abs(x_next - x0)
        print(f"Iterasi {iteration}: x = {x_next}, f(x) = {fx_value:.6e}, f'(x) = {fx_aksen_value:.6e}, error = {error:.6e}")

        if error < tol:
            print(f"\nAkar ditemukan: x = {x_next:.6f} dalam {iteration + 1} iterasi, Error = {error:.6e}")
            return
        
        x0 = x_next
        iteration += 1

    print(f"\nIterasi maksimal tercapai, solusi mungkin tidak konvergen. Nilai terakhir: x = {x0:.6f}")


def secant_terminal():
    f_str = input("Masukkan fungsi f(x) untuk Secant (contoh: x**3 - x - 2): ")
    x0 = float(input("Masukkan tebakan awal (x0): "))
    x1 = float(input("Masukkan tebakan kedua (x1): "))
    tol = float(input("Masukkan toleransi error: "))
    max_iter = int(input("Masukkan jumlah iterasi maksimal: "))

    # Konversi string ke fungsi
    f = sp.lambdify('x', sp.sympify(f_str))
    
    for i in range(max_iter):
        if abs(f(x1) - f(x0)) < 1e-12:  # Hindari pembagian dengan nol
            print("Pembagian dengan nol terjadi.")
            return
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Iterasi {i}: x = {x_next}, error = {f(x_next):.6e}")
        if abs(x_next - x1) < tol:
            print(f"Akar ditemukan: {x_next}, Iterasi: {i}")
            return
        x0, x1 = x1, x_next
    print("Metode tidak konvergen.")

# Menu untuk memilih metode
def main():
    while True:
        print("\nPilih metode:")
        print("1. Iterasi Sederhana")
        print("2. Newton-Raphson")
        print("3. Secant")
        print("4. Exit")
        choice = int(input("Masukkan pilihan (1/2/3/4): "))

# oooooo

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


# mukaku
# oooooo