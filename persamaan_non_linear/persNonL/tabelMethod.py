import numpy as np
import sympy as sp

def metode_tabel():
    print("\n=== Metode Tabel ===\n")
    
    expr = input("Masukkan persamaan (misal: x**2 - 4): ")
    f_expr = sp.sympify(expr)
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr)

    # Input rentang dan toleransi
    a = float(input("Masukkan Nilai Awal a: "))
    b = float(input("Masukkan Nilai Akhir b: "))
    step = float(input("Masukkan langkah (step) untuk tabel: "))
    
    try:
        if step <= 0:
            raise ValueError("Langkah (step) harus lebih besar dari 0.")
        x_vals = np.arange(a, b, step)
        results = []
        for x in x_vals:
            results.append((x, f(x)))
            
        for xi, yi in results:
            print(f"x = {xi:.4f}, f(x) = {yi:.4f}")
            
        for i in range(len(results) - 1):
            if results[i][1] * results[i+1][1] < 0:
                print(f"\nAkar berada di antara x = {results[i][0]:.1f} dan x = {results[i+1][0]:.1f}")
                break
    except ValueError as e:
        print(e)