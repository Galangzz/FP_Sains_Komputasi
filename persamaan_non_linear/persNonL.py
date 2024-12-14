import sympy as sp

def simple_iteration_terminal():
    g_str = input("Masukkan fungsi g(x) untuk Iterasi Sederhana: ")
    x0 = float(input("Masukkan tebakan awal (x0): "))
    tol = float(input("Masukkan toleransi error: "))
    max_iter = int(input("Masukkan jumlah iterasi maksimal: "))

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
            print(f"Iterasi {i + 1}: x = {x_next}, Error = {abs(x_next-x):.6e}")
        except OverflowError:
            print("Overflow terjadi. Fungsi tidak stabil.")
            return

        if abs(x_next - x) < tol:
            print(f"Akar ditemukan: {x_next}, Iterasi: {i + 1}")
            return
        x = x_next
    print("Metode tidak konvergen.")


def newton_raphson():
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

    try:
        f = sp.lambdify('x', sp.sympify(f_str), 'numpy')
    except sp.SystemError:
        print("Fungsi tidak valid. Pastikan fungsi ditulis dengan benar.")
        return
    
    for i in range(max_iter):
        if abs(f(x1) - f(x0)) < 1e-12: 
            print("Pembagian dengan nol terjadi.")
            return
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Iterasi {i}: x0 = {x0}, xn = {x1}, error = {abs(x_next-x1):.6e}")
        if abs(x_next - x1) < tol:
            print(f"Akar ditemukan: {x1}, Iterasi: {i}")
            return
        x0, x1 = x1, x_next
    print("Metode tidak konvergen.")





