#Kegiatan 3
# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai):
    return (nilai['UTS'] + nilai['UAS']) / 2

# Fungsi untuk menghitung semua nilai akhir
def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        data_nilai_akhir[nama] = hitung_nilai_akhir(nilai)
    return data_nilai_akhir

# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

# Program utama
def main():
    data_mahasiswa = {
        'Budi': {'UTS': 80, 'UAS': 85},
        'Ani': {'UTS': 90, 'UAS': 95},
        'Siti': {'UTS': 70, 'UAS': 75},
        # Tambahkan data mahasiswa lainnya jika diperlukan
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
