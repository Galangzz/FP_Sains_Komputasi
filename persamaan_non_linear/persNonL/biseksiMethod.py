import sympy as sp

def metode_biseksi():
    print("\n=== Metode Biseksi ===\n")
    expr = input("Masukkan persamaan (misal: x**2 - 4): ")
    f_expr = sp.sympify(expr)
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr)

    # Input rentang dan toleransi
    a = float(input("Masukkan Nilai Awal a: "))
    b = float(input("Masukkan Nilai Akhir b: "))
    tol = float(input("Masukkan Batas Toleransi (misal: 0.001): "))
    try:
        if f(a) * f(b) > 0:
            raise ValueError("Fungsi tidak memiliki akar pada rentang ini.")
        if tol <= 0:
            raise ValueError("Toleransi harus lebih besar dari 0.")

        loop = 0
        while abs(b - a) > tol:
            c = (a + b) / 2
            if abs(f(c)) < tol:
                break
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
                
            loop += 1
            print(f"Iterasi {loop}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}")
                
        print(f"Akar (Biseksi): {(a + b) / 2:.4f} setelah {loop} iterasi.")
    except ValueError as e:
        print(e)
