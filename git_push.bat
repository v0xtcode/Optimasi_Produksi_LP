@echo off
echo ===== Menginisialisasi Repository Git =====
git init

echo ===== Mengatur konfigurasi Git =====
git config --global user.email "abuyazid955@gmail.com"
git config --global user.name "v0xtcode"

echo ===== Menambahkan semua file ke staging area =====
git add .

echo ===== Membuat commit awal =====
git commit -m "Initial commit: Aplikasi optimasi produksi Linear Programming"

echo ===== Menambahkan remote repository =====
git remote add origin https://github.com/v0xtcode/Optimasi_Produksi_LP.git

echo ===== Menyiapkan branch main =====
git branch -M main

echo ===== Melakukan push ke GitHub =====
echo Push code ke GitHub (Anda akan diminta memasukkan kredensial GitHub)
echo Gunakan Personal Access Token sebagai password saat diminta
git push -u origin main

echo ===== Selesai =====
echo Jika tidak ada error, kode Anda telah berhasil di-push ke GitHub.
echo Silakan kunjungi https://github.com/v0xtcode/Optimasi_Produksi_LP
pause 