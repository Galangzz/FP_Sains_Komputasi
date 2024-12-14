import sympy as sp

def secant_method():
    print("\n=== Metode Secant ===\n")
    f_str = input("Masukkan fungsi f(x): ")
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
