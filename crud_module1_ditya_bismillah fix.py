from tabulate import tabulate

# List untuk menyimpan data pekerja yang mengalami kecelakaan
data_kecelakaan = [
    {"id": "P001", "nama": "Alex", "lokasi": "Gudang", "jenis": "Terjatuh dari tangga", "tingkat": "Sedang"},
    {"id": "P002", "nama": "Budi", "lokasi": "Pabrik", "jenis": "Tersengat listrik", "tingkat": "Berat"},
    {"id": "P003", "nama": "Citra", "lokasi": "Kantor", "jenis": "Tersandung kabel", "tingkat": "Ringan"},
    {"id": "P004", "nama": "Dewa", "lokasi": "Lapangan", "jenis": "Tertimpa material", "tingkat": "Berat"},
    {"id": "P005", "nama": "Eva", "lokasi": "Kantor", "jenis": "Pingsan","tingkat":"Ringan"},
    {"id": "P006", "nama": "Yana","lokasi": "Gudang", "jenis":"Tertabrak dari forklift", "tingkat": "Sedang"},
    {"id": "P007", "nama": "Dika","lokasi": "Lapangan", "jenis":"Terjatuh dari lubang galian", "tingkat": "Sedang"}
]

# List untuk menyimpan data yang dihapus untuk restore
data_terhapus = []

def menu(): # Menu utama
    while True:
        print("\n=== Sistem Data K3 (Laporan Kecelakaan Kerja) ===")
        print("              PT.Jaya Makmur                     ")
        print("1. Tampilan Data Laporan Kecelakaan")
        print("2. Menambah Data Laporan Kecelakaan")
        print("3. Edit Data Laporan Kecelakaan")
        print("4. Hapus Data Laporan Kecelakaan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            menu_tampilan_data()
        elif pilihan == "2":
            tambah_kecelakaan()
        elif pilihan == "3":
            update_kecelakaan()
        elif pilihan == "4":
            hapus_kecelakaan()
        elif pilihan == "5":
            konfirmasi = input("Apakah Anda yakin ingin keluar? (Y/N): ").strip().lower()
            if konfirmasi == "y":
                print("Terima kasih! Program selesai.")
                break
        else:
            print("Pilihan tidak valid, coba lagi.")

def menu_tampilan_data(): # Menu tampilan data
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
            print("Pilihan tidak valid, coba lagi.")

def tampilkan_seluruh_kecelakaan(): # Sub-menu untuk menampilkan semua laporan kecelakaan
    if not data_kecelakaan:
        print("\nTidak ada laporan kecelakaan.\n")
        return

    tabel = [[data['id'], data['nama'], data['lokasi'], data['jenis'], data['tingkat']] for data in data_kecelakaan]
    print(tabulate(tabel, headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat"], tablefmt="grid"))
    
def tampilkan_kecelakaan_by_id(): # Sub-menu untuk menampilkan laporan kecelakaan berdasarkan ID
    id_pekerja = input("Masukkan ID pekerja: ").strip().upper()

    if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit() or id_pekerja == "P000": # Validasi ID pekerja
        print("ID Karyawan tidak valid! ID harus dimulai dengan 'P' diikuti oleh 3 angka, dan tidak boleh 'P000'.")
        return  # Kembali ke submenu jika ID tidak valid

    id_ditemukan = False         # Penanda untuk mengecek apakah ID yang dicari ditemukan dalam data
    laporan_ditemukan = None     # Variabel untuk menyimpan data laporan yang sesuai dengan ID (jika ditemukan)

    # Cari laporan berdasarkan ID pekerja
    for laporan in data_kecelakaan:
        if laporan['id'] == id_pekerja:
            laporan_ditemukan = laporan
            id_ditemukan = True
            break  # Keluar dari loop jika ditemukan

    if not id_ditemukan: # Jika ID tidak ditemukan
        print("\nLaporan dengan ID tersebut tidak ditemukan.\n")
        return  # Kembali ke submenu edit jika tidak ditemukan
    
    # Menampilkan laporan jika ditemukan
    tabel = [[laporan_ditemukan['id'], laporan_ditemukan['nama'], laporan_ditemukan['lokasi'], laporan_ditemukan['jenis'], laporan_ditemukan['tingkat']]]
    print(tabulate(tabel, headers=["ID", "Nama", "Lokasi", "Jenis", "Tingkat"], tablefmt="grid"))

def tambah_kecelakaan(): # Menu tampilan data
    while True:
        print("\n=== Menu Tambah Laporan Kecelakaan ===")
        print("1. Tambah Laporan Kecelakaan Baru")
        print("2. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            while True:  # loop untuk terus tambah data jika user mau
                while True:
                    id_pekerja = input("Masukkan ID pekerja: ").strip().upper()
                    if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit() or id_pekerja == "P000":
                        print("ID Karyawan tidak valid! ID harus dimulai dengan 'P' diikuti oleh 3 angka, dan tidak boleh 'P000'.")
                        continue
                    break

                cek_id = False
                for laporan in data_kecelakaan:
                    if laporan['id'] == id_pekerja:
                        cek_id = True
                        break
                if cek_id:
                    print(f"Data dengan ID {id_pekerja} sudah terdaftar!")
                    continue

                while True:
                    nama = input("Masukkan nama pekerja: ").title()
                    valid = True
                    for char in nama:
                        if char.isdigit():
                            print("Nama tidak boleh mengandung angka.")
                            valid = False
                            break
                    if valid and len(nama) > 25:
                        print("Nama tidak boleh lebih dari 25 karakter.")
                        valid = False
                    if valid:
                        break

                while True:
                    lokasi = input("Masukkan lokasi kecelakaan (Gudang/Kantor/Pabrik/Lapangan): ").capitalize()
                    valid = True
                    for char in lokasi:
                        if char.isdigit():
                            print("Lokasi tidak boleh mengandung angka.")
                            valid = False
                            break
                    if valid and lokasi not in ["Gudang", "Kantor", "Pabrik", "Lapangan"]:
                        print("Lokasi tidak valid! Pilih antara 'Gudang', 'Kantor', 'Pabrik' atau 'Lapangan'.")
                        valid = False
                    if valid:
                        break

                while True:
                    jenis = input("Masukkan jenis kecelakaan: ").title()
                    valid = True
                    for char in jenis:
                        if char.isdigit():
                            print("Jenis kecelakaan tidak boleh mengandung angka.")
                            valid = False
                            break
                    if valid and len(jenis) > 40:
                        print("Jenis kecelakaan tidak boleh lebih dari 40 karakter.")
                        valid = False
                    if valid:
                        break

                while True:
                    tingkat = input("Masukkan tingkat keparahan (Ringan/Sedang/Berat): ").capitalize()
                    if tingkat not in ["Ringan", "Sedang", "Berat"]:
                        print("Tingkat keparahan tidak valid. Harus memilih antara 'Ringan', 'Sedang', atau 'Berat'.")
                        continue
                    break

                # ==== Preview  ====
                headers = ["ID", "Nama", "Lokasi", "Jenis", "Tingkat"]
                data_preview = [[id_pekerja, nama, lokasi, jenis, tingkat]]
                print("\nPreview Laporan yang Akan Ditambahkan:\n")
                print(tabulate(data_preview, headers=headers, tablefmt="grid"))

                # Konfirmasi
                confirm = input(f"\nApakah Anda yakin ingin menambahkan laporan untuk ID {id_pekerja}? (Y/N): ").strip().lower()
                if confirm == "y":
                    data_kecelakaan.append({
                        "id": id_pekerja,
                        "nama": nama,
                        "lokasi": lokasi,
                        "jenis": jenis,
                        "tingkat": tingkat
                    })
                    print("\nLaporan kecelakaan berhasil ditambahkan!\n")
                else:
                    print("\nProses menambah laporan dibatalkan.\n")

                # Tanya apakah ingin tambah data lagi
                lanjut = input("Apakah Anda ingin menambahkan laporan lain? (Y/N): ").strip().lower()
                if lanjut != "y":
                    break
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def update_kecelakaan():
    headers = ["ID", "Nama", "Lokasi", "Jenis", "Tingkat"]
    data_list = [[laporan['id'], laporan['nama'], laporan['lokasi'], laporan['jenis'], laporan['tingkat']] for laporan in data_kecelakaan]
    print(tabulate(data_list, headers=headers, tablefmt="grid"))

    id_pekerja = input("Masukkan ID pekerja yang datanya ingin diperbarui: ").strip().upper()

    laporan_ditemukan = None
    for laporan in data_kecelakaan:
        if laporan['id'] == id_pekerja:
            laporan_ditemukan = laporan
            break

    if not laporan_ditemukan:
        print(f"Data dengan ID {id_pekerja} tidak ditemukan.")
        return

    data_lama = laporan_ditemukan

    print(f"\nData Lama untuk ID {data_lama['id']}:")
    data_lama_preview = [[data_lama['id'], data_lama['nama'], data_lama['lokasi'], data_lama['jenis'], data_lama['tingkat']]]
    print(tabulate(data_lama_preview, headers=headers, tablefmt="grid"))

    while True:
        kolom = input("Masukkan Nama kolom yang ingin diubah (Nama/Lokasi/Jenis/Tingkat): ").strip().lower()

        if kolom == "selesai":
            konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan dan keluar? (Y/N): ").strip().lower()
            if konfirmasi == 'y':
                print("\nData berhasil diperbarui.")
                print("\nData Baru Setelah Diperbarui:")
                data_baru_preview = [[data_lama['id'], data_lama['nama'], data_lama['lokasi'], data_lama['jenis'], data_lama['tingkat']]]
                print(tabulate(data_baru_preview, headers=headers, tablefmt="grid"))
                break
            else:
                print("Perubahan belum disimpan")
                continue

        elif kolom == "nama":
            while True:
                nama = input("Masukkan nama pekerja baru: ").title()
                if nama.isdigit():
                    print("Nama tidak boleh hanya berupa angka.")
                    continue
                valid = True
                for char in nama:
                    if char.isdigit():
                        print("Nama tidak boleh mengandung angka.")
                        valid = False
                        break
                if valid and len(nama) > 25:
                    print("Nama tidak boleh lebih dari 25 karakter.")
                    valid = False
                if valid:
                    data_lama['nama'] = nama
                    print("Nama berhasil diperbarui.")
                    break

        elif kolom == "lokasi":
            while True:
                lokasi = input("Masukkan lokasi baru (Gudang/Kantor/Pabrik/Lapangan): ").capitalize()
                valid = True
                for char in lokasi:
                    if char.isdigit():
                        print("Lokasi tidak boleh mengandung angka.")
                        valid = False
                        break
                if lokasi not in ["Gudang", "Kantor", "Pabrik", "Lapangan"]:
                    print("Lokasi tidak valid! Pilih antara Gudang, Kantor, Pabrik, atau Lapangan.")
                    valid = False
                if valid:
                    data_lama['lokasi'] = lokasi
                    print("Lokasi berhasil diperbarui.")
                    break

        elif kolom == "jenis":
            while True:
                jenis = input("Masukkan jenis kecelakaan baru: ").title()
                valid = True
                for char in jenis:
                    if char.isdigit():
                        print("Jenis kecelakaan tidak boleh mengandung angka.")
                        valid = False
                        break
                if valid and len(jenis) > 40:
                    print("Jenis kecelakaan tidak boleh lebih dari 40 karakter.")
                    valid = False
                if valid:
                    data_lama['jenis'] = jenis
                    print("Jenis kecelakaan berhasil diperbarui.")
                    break

        elif kolom == "tingkat":
            while True:
                tingkat = input("Masukkan tingkat keparahan baru (Ringan/Sedang/Berat): ").capitalize()
                if tingkat in ["Ringan", "Sedang", "Berat"]:
                    data_lama['tingkat'] = tingkat
                    print("Tingkat keparahan berhasil diperbarui.")
                    break
                else:
                    print("Tingkat keparahan tidak valid. Pilih antara Ringan, Sedang, atau Berat.")

        else:
            print("Nama kolom tidak dikenal. Coba lagi.")

        # konfirmasi edit lagi atau tidak
        lanjut = input("Apakah Anda ingin mengubah kolom lain? (Y/N): ").strip().lower()
        if lanjut != 'y':
            break


def hapus_kecelakaan():
    while True:
        print("\n=== Menu Hapus Data Laporan Kecelakaan ===")
        print("1. Hapus Data Berdasarkan ID Karyawan")
        print("2. Hapus Semua Data Laporan")
        print("3. Restore Data Berdasarkan ID")
        print("4. Restore Semua Data yang Dihapus")
        print("5. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_seluruh_kecelakaan()
            while True:
                id_pekerja = input("Masukkan ID pekerja yang ingin dihapus: ").strip().upper()
                if len(id_pekerja) != 4 or id_pekerja[0] != 'P' or not id_pekerja[1:].isdigit() or id_pekerja == "P000":
                    print("ID Karyawan tidak valid! Harus diawali 'P' dan 3 angka, tidak boleh 'P000'.")
                    continue
                break

            data_ditemukan = False
            for laporan in data_kecelakaan:
                if laporan['id'] == id_pekerja:
                    confirm = input(f"Yakin ingin menghapus laporan ID {id_pekerja}? (Y/N): ").strip().lower()
                    if confirm == "y":
                        data_kecelakaan.remove(laporan)
                        data_terhapus.append(laporan)
                        print("Laporan berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                    data_ditemukan = True
                    break

            if not data_ditemukan:
                print(f"Laporan dengan ID {id_pekerja} tidak ditemukan.")

        elif pilihan == "2":
            if data_kecelakaan:
                konfirmasi = input("Yakin ingin menghapus SEMUA data? (Y/N): ").strip().lower()
                if konfirmasi == "y":
                    data_terhapus.extend(data_kecelakaan)
                    data_kecelakaan.clear()
                    print("Semua data laporan telah dihapus.")
                else:
                    print("Penghapusan semua data dibatalkan.")
            else:
                print("Tidak ada data untuk dihapus.")

        elif pilihan == "3":
            if data_terhapus:
                id_restore = input("Masukkan ID karyawan yang ingin direstore: ").strip().upper()
                ditemukan = False
                for laporan in data_terhapus:
                    if laporan['id'] == id_restore:
                        data_kecelakaan.append(laporan)
                        data_terhapus.remove(laporan)
                        print(f"Laporan dengan ID {id_restore} berhasil direstore.")
                        ditemukan = True
                        break
                if not ditemukan:
                    print(f"Tidak ditemukan laporan dengan ID {id_restore} dalam data terhapus.")
            else:
                print("Tidak ada data yang bisa direstore.")

        elif pilihan == "4":
            if data_terhapus:
                data_kecelakaan.extend(data_terhapus)
                data_terhapus.clear()
                print("Semua data yang dihapus telah dikembalikan.")
            else:
                print("Tidak ada data yang bisa direstore.")

        elif pilihan == "5":
            print("Kembali ke menu utama...\n")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")


# Menjalankan program
menu()
