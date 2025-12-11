# LATIHAN PRATIKUM 8
Nama : Nabila Fawwaz Nurliah

NIM : 312510255

Kelas : TI.25.A.2

Pratikum : 8

MATKUL : Pengantar Pemograman

Dosen : Agung Nugroho, S.Kom., M.Kom.

## LATIHAN MANDIRI
1. Latihan 1 : Kalkulator Aman
2. Latihan 2 : Validasi Daftar Nilai


Dalam Python, kesalahan saat program berjalan disebut runtime error, misalnya pembagian dengan nol atau akses indeks list yang salah.
Untuk mencegah program berhenti tiba-tiba, Python menyediakan mekanisme Exception Handling menggunakan blok:
```
try:
    # kode yang berpotensi error
except JenisError:
    # penanganan error
else:
    # berjalan jika tidak ada error
finally:
    # selalu dijalankan
```
Pendekatan ini disebut EAFP (Easier to Ask for Forgiveness than Permission): coba dulu, jika error baru ditangani.

# Percobaan Praktikum
## Percobaan 1 – Mengamati Runtime Error
Melihat bagaimana program berhenti saat terjadi error pembagian dengan nol.

Kode

Program meminta dua input, lalu melakukan pembagian.

Hasil & Analisis

Ketika pengguna memasukkan pembagi 0, muncul pesan:
```
ZeroDivisionError: division by zero
```

Program berhenti langsung (crash) karena tidak ditangani.

## Percobaan 2 – Penanganan Error Sederhana
Menghindari crash menggunakan try-except.

Hasil & Analisis

Pembagian dengan nol kini tidak membuat program berhenti, karena error ditangani:
```
Error: Tidak bisa membagi bilangan dengan nol.
```
## Percobaan 3 – Menangani Berbagai Tipe Eksepsi

Menangani beberapa jenis error sekaligus:

- ValueError untuk input bukan angka

- ZeroDivisionError

- Exception untuk error lain yang tidak diketahui

Hasil & Analisis

- Input huruf → tertangkap ValueError

- Input 0 → tertangkap ZeroDivisionError

- Input benar → program berjalan normal

## Percobaan 4 – Menggunakan else dan finally
Memahami eksekusi blok else dan finally.

Hasil

- Jika input benar → blok else berjalan.

- Jika input salah → blok except berjalan.

- Blok finally selalu berjalan apa pun kondisi error.

## Percobaan 5 – Mengakses Objek Eksepsi

Menampilkan pesan error asli dari Python menggunakan as e.

Hasil

- Saat mengakses indeks salah (misal 5), pesan asli ditampilkan:
```
list index out of range
```
## Percobaan 6 – Memicu Eksepsi (raise)
Membuat error secara manual dengan raise.

Hasil

Jika user memasukkan level < 1:
```
Peringatan: Level tidak valid! Harus minimal 1.
```
Artinya eksepsi custom berhasil ditangkap.

# Latihan Mandiri
## Latihan 1 – Kalkulator Aman
Membuat kalkulator sederhana dengan penanganan:

- ValueError (input bukan angka)

- ZeroDivisionError (pembagian nol)

- raise untuk operator tidak valid

Analisis

Program berjalan dengan aman walaupun terjadi kesalahan input karena semua error sudah ditangani.

## Latihan 2 – Validasi Daftar Nilai
Menghitung rata-rata nilai dari list yang berisi data campuran angka & huruf.

Analisis

- Elemen non-angka seperti 'A' dan 'B' dilewati menggunakan try-except.

- Program tidak berhenti meskipun ada data salah.

- Hanya nilai valid yang dihitung rata-ratanya.

# Kesimpulan

1. Exception Handling sangat penting untuk mencegah program berhenti tiba-tiba.

2. Blok try-except memungkinkan program tetap berjalan walaupun ada error.

3. Penggunaan beberapa jenis except membuat penanganan lebih spesifik dan aman.

4. Klausa else digunakan ketika tidak ada error, sedangkan finally selalu berjalan.

5. Programmer dapat membuat eksepsi sendiri menggunakan raise untuk validasi.

6. Latihan membuktikan bahwa program dapat lebih robust dan user-friendly saat error ditangani dengan baik.
