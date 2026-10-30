# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING

## Identitas Mahasiswa

* **Nama:** Reva Liyanasari
* **NIM:** 2225250101
* **Kelas:** 3A
* **Mata Kuliah:** Algoritma dan Pemrograman
* **Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.

## Tujuan Repositori

Repositori ini dibuat untuk memenuhi kegiatan praktik mata kuliah Algoritma dan Pemrograman pada Pertemuan 12 dengan materi File Input-Output (I/O) dan penanganan error dasar dalam Python.

Melalui praktik ini, mahasiswa diharapkan mampu:
- Membaca data dari file menggunakan Python.
- Menulis dan menambahkan data ke dalam file.
- Memvalidasi dan mengolah data yang dibaca dari file.
- Menangani kesalahan menggunakan `FileNotFoundError` dan `ValueError`.
- Menulis hasil pengolahan data ke dalam file output.
- Melakukan pengujian program berdasarkan test case yang ditentukan.

## Daftar Berkas

### Tugas - Rekap Nilai Mahasiswa

**`tugas/rekap_nilai_file.py`**

Program rekap nilai mahasiswa yang membaca data dari file `data/nilai.txt`, memvalidasi data, menghitung statistik nilai, dan menuliskan hasil rekap ke dalam file `data/hasil_rekap.txt`.

Program memproses data dalam format NIM dan nilai yang dipisahkan dengan tanda koma. Data nilai yang valid digunakan untuk menghitung jumlah data, rata-rata, nilai minimum, nilai maksimum, dan jumlah mahasiswa yang lulus dengan nilai minimal 60.

Program juga menerapkan penanganan error menggunakan `FileNotFoundError` ketika file input tidak ditemukan dan `ValueError` ketika terdapat data yang tidak dapat diproses. Baris yang tidak valid dilewati agar data lainnya tetap dapat diproses.

## Cara Menjalankan

1. Buka folder repositori melalui Visual Studio Code.
2. Buka terminal pada direktori utama repositori.
3. Pastikan file input `data/nilai.txt` tersedia.
4. Jalankan perintah berikut:

   ```bash
   python3 tugas/rekap_nilai_file.py
   ```

5. Periksa pesan yang ditampilkan pada terminal.
6. Buka file `data/hasil_rekap.txt` untuk melihat hasil rekap nilai.

## Format File Input

File input menggunakan format berikut:

```text
NIM,nilai
```

Contoh isi file `data/nilai.txt`:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Pada contoh tersebut, nilai `abc` merupakan data tidak valid yang digunakan untuk menguji penanganan `ValueError`. Baris tersebut dilewati, sedangkan data valid lainnya tetap diproses.

## Hasil Pengujian

| No. | Pengujian | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Membaca file input | File `data/nilai.txt` tersedia dan berisi data valid | Program berhasil membaca dan mengolah data | Program berhasil membaca dan mengolah data nilai mahasiswa | Berhasil |
| 2 | File tidak ditemukan | File input tidak tersedia | Program menampilkan pesan bahwa file tidak ditemukan | Program menampilkan pesan `File tidak ditemukan` | Berhasil |
| 3 | Nilai tidak valid | Terdapat nilai yang bukan angka, seperti `abc` | Baris tidak valid dilewati dan data lainnya tetap diproses | Program melewati baris yang tidak valid dan melanjutkan pemrosesan data lainnya | Berhasil |
| 4 | Membuat rekap nilai | Terdapat data nilai valid | Program menghasilkan file `data/hasil_rekap.txt` yang berisi jumlah data valid, rata-rata, minimum, maksimum, dan jumlah lulus | File `data/hasil_rekap.txt` berhasil dibuat dan berisi hasil rekap nilai | Berhasil |
| 5 | Data kosong atau tidak valid seluruhnya | Tidak terdapat data nilai valid | Program menampilkan pesan bahwa tidak ada data valid untuk direkap | Program menampilkan pesan bahwa tidak ada data valid untuk direkap | Berhasil |

## Refleksi

Melalui praktik ini, saya mempelajari cara membaca, memvalidasi, mengolah, dan menulis data menggunakan file dalam Python. Saya juga memahami bahwa penanganan error diperlukan agar program dapat memberikan informasi ketika terjadi kesalahan selama proses pengolahan data.

Salah satu error yang dipelajari adalah `ValueError`, yang dapat terjadi ketika program mencoba mengubah teks yang bukan angka, seperti `abc`, menjadi tipe data numerik. Dengan menggunakan `try-except`, program dapat melewati baris yang tidak valid dan melanjutkan pemrosesan data lainnya. Selain itu, `FileNotFoundError` digunakan untuk menangani kondisi ketika file input tidak ditemukan.

Praktik ini membantu saya memahami pentingnya validasi data dan penanganan error agar program lebih terstruktur dan mampu menghadapi berbagai kondisi input.

## Sumber

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 12, File Input-Output dan Penanganan Error Dasar.
- Python Software Foundation, dokumentasi Python 3 mengenai operasi file dan penanganan exception.