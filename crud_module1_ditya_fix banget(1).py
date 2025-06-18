from tabulate import tabulate
from datetime import datetime

# List untuk menyimpan data pekerja yang mengalami kecelakaan
data_kecelakaan = [
    {"id": "P001", "nama": "Alex", "lokasi": "Gudang", "jenis": "Terjatuh dari tangga", "tingkat": "Sedang", "tanggal": "31-01-2020"},
    {"id": "P002", "nama": "Budi", "lokasi": "Pabrik", "jenis": "Tersengat listrik", "tingkat": "Berat", "tanggal": "14-02-2020"},
    {"id": "P003", "nama": "Citra", "lokasi": "Kantor", "jenis": "Tersandung kabel", "tingkat": "Ringan", "tanggal": "21-03-2021"},
    {"id": "P004", "nama": "Dewa", "lokasi": "Lapangan", "jenis": "Tertimpa material", "tingkat": "Berat", "tanggal": "18-04-2021"},
    {"id": "P005", "nama": "Eva", "lokasi": "Kantor", "jenis": "Pingsan","tingkat":"Ringan", "tanggal": "05-05-2022"},
    {"id": "P006", "nama": "Yana","lokasi": "Gudang", "jenis":"Tertabrak forklift", "tingkat": "Sedang", "tanggal": "22-06-2022"},
    {"id": "P007", "nama": "Dika","lokasi": "Lapangan", "jenis":"Terjatuh ke lubang galian", "tingkat": "Sedang", "tanggal": "19-03-2024"},
]

# List untuk menyimpan data yang dihapus untuk restore
data_terhapus = []

def menu():
    while True:
        print("    === ⛑️  Sistem Data K3  🦺 ===")
        print("    \tLaporan Kecelakaan Kerja       ")
        print("           PT.Jaya Makmur             ")
        print("1. Tampilan Data Laporan Kecelakaan 🖥️")
        print("2. Menambah Data Laporan Kecelakaan ➕")
        print("3. Edit Data Laporan Kecelakaan 📝")
        print("4. Hapus Data Laporan Kecelakaan 🗑️")
        print("5. Restore Data Laporan Kecelakaan ♻️")
        print("6. Keluar 🔚")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            menu_tampilan_data()
        elif pilihan == "2":
            tambah_kecelakaan()
        elif pilihan == "3":
            update_kecelakaan()
        elif pilihan == "4":
            hapus_kecelakaan()
        elif pilihan == "5":
            restore_kecelakaan()
        elif pilihan == "6":
            konfirmasi = input("Apakah Anda yakin ingin keluar? (Y/N): ").strip().lower()
            if konfirmasi == "y":
                print("Terima kasih! Program selesai.🙏")
                break
        
        else:
            print("Pilihan tidak valid, coba lagi! ❌")

def menu_tampilan_data():
    while True:
        print("\n=== Menu Tampilan Data Laporan Kecelakaan ===")
        print("1. Tampilkan Seluruh Data")
        print("2. Tampilkan Data Berdasarkan ID")
        print("3. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            tampilkan_seluruh_kecelakaan()
        elif pilihan == "2":
            tampilkan_kecelakaan_by_id()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid, coba lagi! ❌")

def tampilkan_seluruh_kecelakaan():
    if not data_kecelakaan:
        print("\nTidak ada laporan kecelakaan.\n")
        return

    tabel = [[data['id'], data['nama'], data['lokasi'], data['jenis'], data['tingkat'], data['tanggal']] for data in data_kecelakaan]
    print(tabulate(tabel, headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat", "Tanggal"], tablefmt="grid"))
    
def tampilkan_kecelakaan_by_id():
    id_pekerja = input("Masukkan ID pekerja: ").strip().upper()

    if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit() or id_pekerja == "P000":
        print("ID Karyawan tidak valid! ID harus dimulai dengan 'P' diikuti oleh 3 angka, dan tidak boleh 'P000'.")
        return

    for laporan in data_kecelakaan:
        if laporan['id'] == id_pekerja:
            tabel = [[laporan['id'], laporan['nama'], laporan['lokasi'], laporan['jenis'], laporan['tingkat'], laporan['tanggal']]]
            print(tabulate(tabel, headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat", "Tanggal"], tablefmt="grid"))
            return
    
    print("\nLaporan dengan ID tersebut tidak ditemukan.\n")

def validasi_tanggal(tanggal_input):
    try:
        # parsing string ke objek datetime
        date_obj = datetime.strptime(tanggal_input, "%d-%m-%Y")
        
        # membatasi tahun 2020-2024 
        if not (2020 <= date_obj.year <= 2024):
            return None
            
        # Kembalikan string yang sudah dinormalisasi
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        return None

def tambah_kecelakaan():
    while True:
        print("\n=== Menu Tambah Laporan Kecelakaan ===")
        print("1. Tambah Laporan Kecelakaan Baru")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            # Input ID Pekerja
            while True:
                id_pekerja = input("\nMasukkan ID pekerja (format PXXX): ").strip().upper()
                
                # Validasi format ID
                if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit():
                    print("Format ID tidak valid! Harus diawali 'P' diikuti 3 angka (contoh: P001)")
                    continue
                
                # Validasi ID P000 tidak diperbolehkan
                if id_pekerja == "P000":
                    print("ID P000 tidak diperbolehkan!")
                    continue
                
                # Cek duplikasi ID
                id_terdaftar = False
                for pekerja in data_kecelakaan:
                    if pekerja['id'] == id_pekerja:
                        id_terdaftar = True
                        break
                
                if id_terdaftar:
                    print(f"ID {id_pekerja} sudah terdaftar!")
                    break  # Keluar dari loop input ID, kembali ke menu tambah
                
                break  # Keluar dari loop input ID jika valid
            
            if id_terdaftar:  # Jika ID duplikat, kembali ke menu tambah
                continue

            # Input Nama
            while True:
                nama = input("Masukkan nama pekerja: ").strip().title()
                if not nama:
                    print("Nama tidak boleh kosong!")
                    continue

                # Cek nama ada angka atau simbol
                if not all(char.isalpha() or char.isspace() for char in nama):
                    print("Nama hanya boleh mengandung huruf dan spasi!")
                    continue
                
                # Cek panjang nama
                if len(nama) > 25:
                    print("Nama tidak boleh lebih dari 25 karakter")
                    continue
                
                break

            # Input Lokasi
            while True:
                lokasi = input("Masukkan lokasi (Gudang/Kantor/Pabrik/Lapangan): ").strip().capitalize()
                if lokasi not in ["Gudang", "Kantor", "Pabrik", "Lapangan"]:
                    print("Pilihan lokasi tidak valid!")
                    continue
                break

            # Input Jenis Kecelakaan
            while True:
                jenis = input("Masukkan jenis kecelakaan: ").strip().title()
                if len(jenis) > 40:
                    print("Jenis kecelakaan maksimal 40 karakter")
                    continue
                if not jenis:
                    print("Jenis kecelakaan tidak boleh kosong!")
                    continue

                break

            # Input Tingkat Keparahan
            while True:
                tingkat = input("Masukkan tingkat keparahan (Ringan/Sedang/Berat): ").strip().capitalize()
                if tingkat not in ["Ringan", "Sedang", "Berat"]:
                    print("Pilihan tingkat keparahan tidak valid!")
                    continue
                break

            # Input Tanggal
            while True:
                tanggal_input = input("Masukkan tanggal kejadian (DD-MM-YYYY): ").strip()
                tanggal = validasi_tanggal(tanggal_input)
                if not tanggal:
                    print("Format tanggal tidak valid! Gunakan format DD-MM-YYYY")
                    continue
                break

            # Tampilkan preview data
            print("\n=== Preview Data ===")
            headers = ["ID", "Nama", "Lokasi", "Jenis", "Tingkat", "Tanggal"]
            data_preview = [[id_pekerja, nama, lokasi, jenis, tingkat, tanggal]]
            print(tabulate(data_preview, headers=headers, tablefmt="grid"))

            # Konfirmasi penyimpanan
            konfirmasi = input("\nSimpan data ini? (Y/N): ").strip().lower()
            if konfirmasi == 'y':
                data_kecelakaan.append({
                    "id": id_pekerja,
                    "nama": nama,
                    "lokasi": lokasi,
                    "jenis": jenis,
                    "tingkat": tingkat,
                    "tanggal": tanggal
                })
                print("Data berhasil ditambahkan 💾")
            else:
                print("Data tidak disimpan.")

        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1 atau 2")

def update_kecelakaan():
    if not data_kecelakaan:
        print("Tidak ada data untuk diupdate!")
        return

    while True:
        print("\n=== Menu Update Laporan Kecelakaan ===")
        print("1. Update Data Kecelakaan")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            # Input ID
            id_pekerja = input("\nMasukkan ID pekerja yang ingin diupdate (format PXXX): ").strip().upper()

            if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit() or id_pekerja == "P000":
                print("ID tidak valid! Format: P diikuti 3 angka (contoh: P001)")
                continue

            # Cek ID di data
            data_ditemukan = None
            for laporan in data_kecelakaan:
                if laporan['id'] == id_pekerja:
                    data_ditemukan = laporan
                    break

            if not data_ditemukan:
                print(f"Data dengan ID {id_pekerja} tidak ditemukan!")
                continue  # langsung kembali ke menu update

            # Tampilkan data yang akan diupdate
            print("\n=== Data Saat Ini ===")
            print(tabulate([[data_ditemukan['id'], data_ditemukan['nama'], data_ditemukan['lokasi'], data_ditemukan['jenis'], data_ditemukan['tingkat'], data_ditemukan['tanggal']]],
                           headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat", "Tanggal"], tablefmt="grid"))

            # Menu edit kolom
            while True:
                menu_edits = [
                    ["1. Nama", "3. Jenis Kecelakaan", "5. Tanggal Kejadian"],
                    ["2. Lokasi", "4. Tingkat Keparahan", "6. Selesai"]
                ]
                print("\nPilih Kolom yang Ingin Diedit:")
                print(tabulate(menu_edits, tablefmt="plain"))

                kolom = input("Pilihan (1-6): ").strip()

                if kolom == "1":
                    while True:
                        nama = input("Masukkan nama baru: ").strip().title()
                        if not nama:
                            print("Nama tidak boleh kosong!")
                            continue
                        # Cek nama ada angka atau simbol
                        if not all(char.isalpha() or char.isspace() for char in nama):
                            print("Nama hanya boleh mengandung huruf dan spasi!")
                            continue
                        if len(nama) > 25:
                            print("Nama tidak boleh lebih dari 25 karakter!")
                            continue
                        data_ditemukan['nama'] = nama
                        print("Nama berhasil diupdate!")
                        break

                elif kolom == "2":
                    while True:
                        lokasi = input("Masukkan lokasi baru (Gudang/Kantor/Pabrik/Lapangan): ").strip().capitalize()
                        if lokasi not in ["Gudang", "Kantor", "Pabrik", "Lapangan"]:
                            print("Lokasi tidak valid!")
                            continue
                        data_ditemukan['lokasi'] = lokasi
                        print("Lokasi berhasil diupdate!")
                        break

                elif kolom == "3":
                    while True:
                        jenis = input("Masukkan jenis kecelakaan baru: ").strip().title()
                        if not jenis:
                            print("Jenis kecelakaan tidak boleh kosong!")
                            continue
                        if len(jenis) > 40:
                            print("Jenis kecelakaan maksimal 40 karakter!")
                            continue
                        data_ditemukan['jenis'] = jenis
                        print("Jenis kecelakaan berhasil diupdate!")
                        break

                elif kolom == "4":
                    while True:
                        tingkat = input("Masukkan tingkat keparahan baru (Ringan/Sedang/Berat): ").strip().capitalize()
                        if tingkat not in ["Ringan", "Sedang", "Berat"]:
                            print("Tingkat keparahan tidak valid!")
                            continue
                        data_ditemukan['tingkat'] = tingkat
                        print("Tingkat keparahan berhasil diupdate!")
                        break

                elif kolom == "5":
                    while True:
                        tanggal_input = input("Masukkan tanggal baru (DD-MM-YYYY): ").strip()
                        tanggal = validasi_tanggal(tanggal_input)
                        if not tanggal:
                            print("Format tanggal tidak valid! Gunakan DD-MM-YYYY")
                            continue
                        data_ditemukan['tanggal'] = tanggal
                        print("Tanggal berhasil diupdate!")
                        break

                elif kolom == "6":
                    print("\n=== Data Setelah Diupdate ===")
                    print(tabulate([[data_ditemukan['id'], data_ditemukan['nama'], data_ditemukan['lokasi'], data_ditemukan['jenis'], data_ditemukan['tingkat'], data_ditemukan['tanggal']]],
                                   headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat", "Tanggal"], tablefmt="grid"))
                            # Update data lagi?
                    lanjut = input("\nUpdate data lain? (Y/N): ").strip().lower()
                    if lanjut == 'y':
                        break
                    else:
                        return  # keluar dari fungsi update_kecelakaan

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1 atau 2.")

def hapus_kecelakaan():
    while True:
        print("\n=== Menu Hapus Data ===")
        print("1. Hapus Data Berdasarkan ID")
        print("2. Hapus Semua Data")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            if not data_kecelakaan:
                print("Tidak ada data untuk dihapus!")
                continue

            id_pekerja = input("\nMasukkan ID yang akan dihapus: ").strip().upper()

            if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit() or id_pekerja == "P000":
                print("ID tidak valid! Format: P diikuti 3 angka (contoh: P001)")
                continue

            data = None
            for laporan in data_kecelakaan:
                if laporan['id'] == id_pekerja:
                    data = laporan
                    break

            if not data:
                print(f"Data dengan ID {id_pekerja} tidak ditemukan!")
                continue

            # Menampilkan data sebelum konfirmasi hapus
            print("\n--- Data yang Akan Dihapus ---")
            tabel = [[data['id'], data['nama'], data['lokasi'], data['jenis'], data['tingkat'], data['tanggal']]]
            print(tabulate(tabel, headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat", "Tanggal"], tablefmt="grid"))
            
            # Menampilkan submenu konfirmasi hapus
            print("\n--- Konfirmasi Penghapusan ---")
            confirm = input(f"Yakin hapus data ID {id_pekerja}? (Y/N): ").strip().lower()
            if confirm == 'y':
                data_kecelakaan.remove(data)
                data_terhapus.append(data)
                print("Data berhasil dihapus!")
            else:
                print("Data tidak jadi dihapus.")

        elif pilihan == "2":
            if not data_kecelakaan:
                print("Tidak ada data untuk dihapus!")
                continue

            confirm = input("Yakin hapus SEMUA data? (Y/N): ").strip().lower()
            if confirm == 'y':
                data_terhapus.extend(data_kecelakaan)
                data_kecelakaan.clear()
                print("Semua data berhasil dihapus!")
            else:
                print("Data tidak jadi dihapus.")

        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

def restore_kecelakaan():
    while True:
        print("\n=== Menu Restore Data ===")
        print("1. Restore Data Berdasarkan ID")
        print("2. Restore Semua Data")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            if not data_terhapus:
                print("Tidak ada data yang bisa direstore!")
                continue

            while True:
                id_pekerja = input("\nMasukkan ID yang akan direstore: ").strip().upper()

                if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit() or id_pekerja == "P000":
                    print("ID tidak valid! Format: P diikuti 3 angka (contoh: P001)")
                    continue

                data = None
                for laporan in data_terhapus:
                    if laporan['id'] == id_pekerja:
                        data = laporan
                        break

                if not data:
                    print(f"Data dengan ID {id_pekerja} tidak ditemukan di data terhapus!")
                    continue

                # Menampilkan data sebelum konfirmasi restore
                print("\nData yang terhapus:")
                tabel = [[data['id'], data['nama'], data['lokasi'], data['jenis'], data['tingkat'], data['tanggal']]
                     for data in data_terhapus]
                print(tabulate(tabel, headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat", "Tanggal"], tablefmt="grid"))
                
                confirm = input(f"Yakin restore data ID {id_pekerja}? (Y/N): ").strip().lower()
                if confirm == 'y':
                    data_terhapus.remove(data)
                    data_kecelakaan.append(data)
                    print("Data berhasil direstore!")
                break

        elif pilihan == "2":
            if not data_terhapus:
                print("Tidak ada data yang bisa direstore!")
                continue

            confirm = input("Yakin restore SEMUA data terhapus? (Y/N): ").strip().lower()
            if confirm == 'y':
                data_kecelakaan.extend(data_terhapus)
                data_terhapus.clear()
                print("Semua data berhasil direstore!")

        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
menu()