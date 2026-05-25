# Kumpulan Code Chia

Repositori ini berisi kumpulan skrip Python sederhana yang mencakup berbagai fungsi, mulai dari perhitungan matematika hingga grafika komputer menggunakan modul `turtle`.

## Daftar Isi
- [Angka Prima](#angka-prima.py)
- [Elips & Elips2](#elips--elips2.py)
- [Tracer](#tracer.pu)
- [Wilted Rose](#wilted-rose.py)

---

### Angka Prima (`angka-prima.py`)
Skrip ini digunakan untuk memeriksa apakah sebuah angka adalah bilangan prima dan menampilkan faktor-faktor pembaginya.
- **Fitur:** Menghitung faktor bilangan dan menentukan status prima.
- **Cara Menjalankan:** `python angka-prima.py`

### Elips & Elips2 (`elips.py`, `elips2.py`)
Ekstensi dari kelas `turtle.Turtle` untuk menggambar bentuk elips yang tidak tersedia secara default di modul `turtle`.
- **elips.py:** Implementasi dasar menggambar elips dengan kontrol `tracer`.
- **elips2.py:** Versi yang lebih canggih dengan tambahan parameter `steps` (untuk menggambar poligon dalam bentuk elips) dan metode `circle` yang terintegrasi.

### Tracer (`tracer.py`)
Skrip utilitas yang mendemonstrasikan cara memanipulasi fungsi `turtle.tracer()`. Ini berguna untuk mempercepat proses menggambar pada aplikasi `turtle` yang kompleks dengan mengontrol pembaruan layar secara manual.

### Wilted Rose (`wilted-rose.py`)
Skrip yang menggunakan grafika `turtle` untuk menggambar ilustrasi bunga mawar yang layu (wilted rose).
- **Cara Menjalankan:** `python wilted-rose.py`

## Persyaratan
- Python 3.x
- Modul `turtle` (biasanya sudah termasuk dalam instalasi standar Python).

## Cara Penggunaan
1. Clone repositori ini.
2. Jalankan skrip yang diinginkan menggunakan perintah:
   ```bash
   python nama_file.py
   ```
