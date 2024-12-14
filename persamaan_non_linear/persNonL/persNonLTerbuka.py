import numpy as np
import sympy as sp

def metode_tabel(f, a, b, step):
    if step <= 0:
        raise ValueError("Langkah (step) harus lebih besar dari 0.")
    x_vals = np.arange(a, b, step)
    results = []
    for x in x_vals:
        results.append((x, f(x)))
    return results

def metode_biseksi(f, a, b, tol):
    if f(a) * f(b) > 0:
        raise ValueError("Fungsi tidak memiliki akar pada rentang ini.")
    if tol <= 0:
        raise ValueError("Toleransi harus lebih besar dari 0.")

    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def metode_regula_falsi(f, a, b, tol):
    if f(a) * f(b) > 0:
        raise ValueError("Fungsi tidak memiliki akar pada rentang ini.")
    if tol <= 0:
        raise ValueError("Toleransi harus lebih besar dari 0.")

    while abs(b - a) > tol:
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def main():
    print("Kalkulator Persamaan Non-Linier")
    print("Pilih metode yang ingin digunakan:")
    print("1. Metode Tabel")
    print("2. Metode Biseksi")
    print("3. Metode Regula Falsi")

    try:
        metode = int(input("Masukkan pilihan metode (1/2/3): "))
        if metode not in [1, 2, 3]:
            raise ValueError("Pilihan tidak valid. Pilih 1, 2, atau 3.")

        # Input persamaan
        expr = input("Masukkan persamaan (misal: x**2 - 4): ")
        f_expr = sp.sympify(expr)
        x = sp.symbols('x')
        f = sp.lambdify(x, f_expr)

        # Input rentang dan toleransi
        a = float(input("Masukkan Nilai Awal a: "))
        b = float(input("Masukkan Nilai Akhir b: "))
        tol = float(input("Masukkan Batas Toleransi (misal: 0.001): "))

        if metode == 1:
            print("\nHasil Metode Tabel:")
            step = float(input("Masukkan langkah (step) untuk tabel: "))
            try:
                tabel = metode_tabel(f, a, b, step)
                for xi, yi in tabel:
                    print(f"x = {xi:.4f}, f(x) = {yi:.4f}")
            except ValueError as e:
                print(e)

        elif metode == 2:
            print("\nHasil Metode Biseksi:")
            try:
                akar_biseksi = metode_biseksi(f, a, b, tol)
                print(f"Akar (Biseksi): {akar_biseksi:.4f}")
            except ValueError as e:
                print(e)

        elif metode == 3:
            print("\nHasil Metode Regula Falsi:")
            try:
                akar_regula_falsi = metode_regula_falsi(f, a, b, tol)
                print(f"Akar (Regula Falsi): {akar_regula_falsi:.4f}")
            except ValueError as e:
                print(e)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
