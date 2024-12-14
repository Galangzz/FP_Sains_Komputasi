import sympy as sp

def simple_iteration_method():
    print("\n=== Metode Iterasi Sederhana ===\n")
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