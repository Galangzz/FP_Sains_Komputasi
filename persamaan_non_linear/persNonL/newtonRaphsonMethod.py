import sympy as sp

def newton_raphson():
    print("\n=== Metode Newton Raphson ===\n")
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
