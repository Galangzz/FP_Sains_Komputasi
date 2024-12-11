import sympy as sp

# Fungsi Newton-Raphson
def newton_raphson(fx_expr, x0, tol, max_iter):
    # Menggunakan sympy untuk konversi ekspresi dan turunan
    x = sp.symbols('x')
    
    # Konversi ekspresi string ke simbolik
    fx = sp.sympify(fx_expr, locals={"e": sp.exp(1)})
    dfx = sp.diff(fx, x)  # Hitung turunan otomatis
    
    # Membuat fungsi numerik
    f_lambdified = sp.lambdify(x, fx, 'math')
    df_lambdified = sp.lambdify(x, dfx, 'math')
    
    # Iterasi Newton-Raphson
    iteration = 0
    while iteration < max_iter:
        fx_val = f_lambdified(x0)
        dfx_val = df_lambdified(x0)
        
        # Cek apakah turunan tidak nol untuk menghindari pembagian dengan nol
        if dfx_val == 0:
            print("Turunan sama dengan nol, solusi tidak ditemukan.")
            return None, iteration
        
        # Hitung nilai x berikutnya
        x_next = x0 - fx_val / dfx_val
        error = abs(x_next - x0)
        print(f"Iterasi {iteration}: x = {x_next}, error = {error}")
        
        # Jika error lebih kecil dari toleransi, kita dapat berhenti
        if error < tol:
            return x_next, iteration
        
        x0 = x_next
        iteration += 1
    
    return None, max_iter  # Jika iterasi maksimal tercapai

# Input dari pengguna
fx_str = input("Masukkan fungsi f(x) (misalnya: x - e(-x)): ")
x0 = float(input("Masukkan tebakan awal (x0): "))
tol = float(input("Masukkan toleransi error: "))
max_iter = int(input("Masukkan iterasi maksimal: "))

# Pemanggilan fungsi
root, iters = newton_raphson(fx_str, x0, tol, max_iter)

if root is not None:
    print(f"\nAkar ditemukan: x = {root:.6f} dalam {iters} iterasi")
else:
    print("\nIterasi maksimal tercapai, solusi mungkin tidak konvergen.")
