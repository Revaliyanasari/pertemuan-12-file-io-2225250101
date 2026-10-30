NILAI_MINIMUM_LULUS = 70


def baca_data(nama_file):
    data = []

    with open(nama_file, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris:
                continue

            bagian = baris.split(",")
            if len(bagian) != 2 or not bagian[0].strip():
                print(f"Baris {nomor_baris} diabaikan: format data tidak valid.")
                continue

            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor_baris} diabaikan: nilai bukan angka.")
                continue

            if not 0 <= nilai <= 100:
                print(f"Baris {nomor_baris} diabaikan: nilai harus antara 0 dan 100.")
                continue

            data.append(nilai)

    return data


def tulis_rekap(nama_file, data):
    if not data:
        raise ValueError("Tidak ada data nilai yang valid untuk direkap.")

    jumlah_data = len(data)
    rata_rata = sum(data) / jumlah_data
    nilai_minimum = min(data)
    nilai_maksimum = max(data)
    jumlah_lulus = sum(nilai >= NILAI_MINIMUM_LULUS for nilai in data)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_minimum:.2f}\n")
        file.write(f"Maksimum: {nilai_maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

if __name__ == "__main__":
    try:
        data = baca_data(input_file)
        tulis_rekap(output_file, data)
        print(f"Rekap berhasil ditulis ke {output_file}.")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {input_file}")
    except ValueError as error:
        print(error)