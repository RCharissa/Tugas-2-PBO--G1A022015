# 1. Implementasikan kelas Mahasiswa, Jurusan, dan Universitas
# telah tertera diatas


# 2. Buat objek Universitas dengan nama "XYZ University"
xyz_university = Universitas("XYZ University")

# 3. Buat objek Jurusan dengan nama "Teknik Informatika" dan tambahkan ke dalam Universitas XYZ
teknik_informatika = Jurusan("Teknik Informatika")
xyz_university.tambah_jurusan(teknik_informatika)

# 4. Buat objek Mahasiswa dengan nama "Kalian masing", NIM "Kalian masing", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa_1 = Mahasiswa(
    "Raden Charissa Prima Oktavia", "G1A022015", teknik_informatika)
teknik_informatika.tambah_Mahasiswa(mahasiswa_1)


# 5. Buat objek Jurusan dengan nama "Teknik Komputer" dan tambahkan ke dalam Universitas XYZ
teknik_komputer = Jurusan("Teknik Komputer")
xyz_university.tambah_jurusan(teknik_komputer)

# 6. Buat objek Mahasiswa dan tambahkan ke dalam Jurusan Teknik Komputer di Universitas XYZ
mahasiswa_2 = Mahasiswa("Charissa", "G1A022005", teknik_komputer)
teknik_komputer.tambah_Mahasiswa(mahasiswa_2)

mahasiswa_3 = Mahasiswa("Prima", "G1A022055", teknik_komputer)
teknik_komputer.tambah_Mahasiswa(mahasiswa_3)

mahasiswa_4 = Mahasiswa("Oktavia", "G1A022555", teknik_komputer)
teknik_komputer.tambah_Mahasiswa(mahasiswa_4)

# 8. Tampilkan daftar jurusan yang ada di Universitas XYZ
xyz_university.tampilkan_daftar_jurusan()

# 7. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Komputer di Universitas XYZ
teknik_komputer.tampilkan_Data()


# 9. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
teknik_informatika.tampilkan_Data()

# 10. Objek-objek yang telah dibuat sebelumnya
print('\n')
print('Data Mahasiswa')
mahasiswa_1.tampilkan_info()
mahasiswa_2.tampilkan_info()
mahasiswa_3.tampilkan_info()
mahasiswa_4.tampilkan_info()
