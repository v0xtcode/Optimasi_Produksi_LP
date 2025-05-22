# Aplikasi Optimasi Produksi Linear Programming

## Deskripsi
Aplikasi ini digunakan untuk menentukan jumlah optimal produk yang harus diproduksi untuk memaksimalkan keuntungan dengan mempertimbangkan keterbatasan sumber daya seperti bahan baku dan tenaga kerja. Aplikasi mengimplementasikan metode Linear Programming untuk menemukan solusi optimal berdasarkan batasan-batasan yang diberikan.

## Fitur Utama
1. Input kebutuhan bahan, tenaga kerja, dan keuntungan per produk
2. Optimasi menggunakan solver Linear Programming (scipy.optimize.linprog)
3. Visualisasi solusi optimal dengan grafik interaktif
4. Tampilan jumlah produk A dan B yang harus dibuat serta total keuntungan
5. Analisis penggunaan sumber daya dan batasan kritis
6. Antarmuka pengguna yang intuitif dengan desain modern

## Teknologi yang Digunakan
- **Backend**: Python, Flask
- **Optimasi**: SciPy (linprog dengan metode HiGHS)
- **Visualisasi**: Matplotlib
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Tampilan**: Glassmorphism design

## Persyaratan
- Python 3.8 atau yang lebih baru
- Flask 2.3.3
- NumPy 1.24.3
- SciPy 1.10.1
- Matplotlib 3.7.2

## Cara Instalasi
1. Clone repository ini:
   ```
   git clone https://github.com/v0xtcode/Optimasi_Produksi_LP.git
   cd Optimasi_Produksi_LP
   ```

2. Buat virtual environment (opsional tetapi direkomendasikan):
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Install dependensi yang diperlukan:
   ```
   pip install -r requirements.txt
   ```

## Cara Menjalankan Aplikasi
1. Setelah instalasi selesai, jalankan aplikasi dengan perintah:
   ```
   python app.py
   ```

2. Buka browser dan akses alamat `http://127.0.0.1:5000/`
3. Aplikasi akan menampilkan halaman beranda, klik "Aplikasi" pada navbar untuk memulai penggunaan

## Studi Kasus Default
Aplikasi ini dilengkapi dengan nilai default untuk memudahkan pengujian:
- Keuntungan: Produk A (Rp 5.000), Produk B (Rp 7.000)
- Kebutuhan Bahan A: Produk A (2 unit), Produk B (1 unit)
- Kebutuhan Bahan B: Produk A (1 unit), Produk B (2 unit)
- Kebutuhan Tenaga Kerja: Produk A (3 jam), Produk B (2 jam)
- Ketersediaan: Bahan A (100 unit), Bahan B (80 unit), Tenaga Kerja (120 jam)

Solusi optimal untuk studi kasus ini adalah memproduksi 20 unit Produk A dan 30 unit Produk B, dengan total keuntungan Rp 310.000.

## Pengembang
Dikembangkan oleh Kelompok 5 - Universitas Hasyim Asyari

## Lisensi
MIT License - Silakan gunakan dan modifikasi kode dengan bebas dengan menyertakan atribusi yang sesuai. 