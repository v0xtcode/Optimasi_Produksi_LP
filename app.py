from flask import Flask, render_template, request, jsonify
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os
import base64
from io import BytesIO

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/app')
def app_page():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    # Mengambil data input dari form
    data = request.form
    
    # Log debugging untuk melihat data yang diterima
    print("Data yang diterima:")
    for key, value in data.items():
        print(f"{key}: {value}")
    
    # Keuntungan per produk (koefisien fungsi tujuan)
    c = [-float(data['profit_a']), -float(data['profit_b'])]  # Negatif karena kita ingin memaksimalkan
    
    # Batasan sumber daya (koefisien batasan)
    A = [
        [float(data['material_a_for_a']), float(data['material_a_for_b'])],  # Bahan A
        [float(data['material_b_for_a']), float(data['material_b_for_b'])],  # Bahan B
        [float(data['labor_for_a']), float(data['labor_for_b'])]             # Tenaga Kerja
    ]
    
    # Ketersediaan sumber daya (ruas kanan batasan)
    b = [
        float(data['material_a_available']),  # Ketersediaan Bahan A
        float(data['material_b_available']),  # Ketersediaan Bahan B
        float(data['labor_available'])        # Ketersediaan Tenaga Kerja
    ]
    
    # Log debugging untuk melihat model LP
    print("Model LP:")
    print(f"Fungsi Tujuan: Maksimalkan Z = {-c[0]}*x1 + {-c[1]}*x2")
    print("Batasan:")
    for i in range(len(A)):
        print(f"{A[i][0]}*x1 + {A[i][1]}*x2 <= {b[i]}")
    print("x1, x2 >= 0")
    
    # Batasan non-negatif
    bounds = [(0, None), (0, None)]
    
    # Menyelesaikan masalah optimasi
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    # Log debugging hasil
    print("Hasil optimasi:")
    print(result)
    
    # Menampilkan hasil
    if result.success:
        product_a = round(result.x[0], 2)
        product_b = round(result.x[1], 2)
        total_profit = round(-result.fun, 2)  # Negatif dari fungsi objektif (karena kita memaksimalkan)
        
        # Memvisualisasikan hasil
        plot_url = create_visualization(A, b, product_a, product_b, float(data['profit_a']), float(data['profit_b']))
        
        return jsonify({
            'status': 'success',
            'product_a': product_a,
            'product_b': product_b,
            'total_profit': total_profit,
            'plot_url': plot_url
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Optimasi tidak dapat diselesaikan. Periksa kembali input Anda.'
        })

def create_visualization(A, b, opt_x, opt_y, profit_a, profit_b):
    plt.figure(figsize=(10, 6))
    
    # Menghasilkan titik-titik x untuk plot
    x = np.linspace(0, max(b) * 1.5, 1000)
    
    # Plot setiap batasan
    colors = ['r', 'g', 'b']
    labels = ['Bahan A', 'Bahan B', 'Tenaga Kerja']
    
    for i in range(len(A)):
        if A[i][1] != 0:  # Hindari pembagian oleh nol
            y = (b[i] - A[i][0] * x) / A[i][1]
            valid_idx = y >= 0
            plt.plot(x[valid_idx], y[valid_idx], colors[i], label=f'Batasan {labels[i]}')
        else:
            plt.axvline(x=b[i]/A[i][0], color=colors[i], label=f'Batasan {labels[i]}')
    
    # Area fisibel
    plt.fill_between([0], [0], color='gray', alpha=0.2)
    
    # Titik optimal
    plt.scatter([opt_x], [opt_y], color='black', s=100, label=f'Solusi Optimal ({opt_x:.2f}, {opt_y:.2f})')
    
    # Garis iso-profit
    x_vals = np.array([0, b[0] * 1.5])
    # Garis profit dengan nilai optimal
    optimal_profit = profit_a * opt_x + profit_b * opt_y
    y_vals = (optimal_profit - profit_a * x_vals) / profit_b
    plt.plot(x_vals, y_vals, 'k--', label=f'Iso-profit (Rp {optimal_profit:.2f})')
    
    plt.xlabel('Jumlah Produk A')
    plt.ylabel('Jumlah Produk B')
    plt.title('Visualisasi Solusi Optimasi Linear Programming')
    plt.grid(True)
    plt.legend()
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    
    # Ubah plot menjadi gambar untuk dikirim ke halaman web
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True) 