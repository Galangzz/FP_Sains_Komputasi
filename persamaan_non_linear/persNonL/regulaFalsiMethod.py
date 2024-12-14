import sympy as sp

def metode_regula_falsi():
    print("\n=== Metode Regula Falsi ===\n")
    # Input persamaan
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

        while abs(b - a) > tol:
            c = b - (f(b) * (b - a)) / (f(b) - f(a))
            if f(c) == 0:
                break
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
        print(f"Akar (Regula Falsi): {c:.4f}")
    except ValueError as e:
        print(e)
