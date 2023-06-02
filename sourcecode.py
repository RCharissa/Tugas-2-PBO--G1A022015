class Mahasiswa:
    def _init_(self, nama, NPM, jurusan):
        self.Nama = nama
        self.NPM = NPM
        self.Jurusan = jurusan

    def tampilkan_info(self):
        print('-----------------------------------')
        print('Nama Mahasiswa :', self.Nama)
        print('NPM Mahasiswa :', self.NPM)
        print('Jurusan :', self.Jurusan)


class Jurusan:
    def _init_(self, nama_jurusan):
        self.namaJurusan = nama_jurusan
        self.daftarMahasiswa = []

    def tambah_Mahasiswa(self, mahasiswa):
        self.daftarMahasiswa.append(mahasiswa)

    def tampilkan_Data(self):
        print('Daftar Mahasiswa di jurusan', self.namaJurusan)
        for i, mahasiswa in enumerate(self.daftarMahasiswa, start=1):
            print(f"{i}. Nama: {mahasiswa.Nama}")
            print(f"   NPM : {mahasiswa.NPM}")
            print()


class Universitas:
    def _init_(self, nama_universitas):
        self.namaUniversitas = nama_universitas
        self.daftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.daftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.namaUniversitas)
        for i, jurusan in enumerate(self.daftarJurusan, start=1):
            print(f"{i}. {jurusan.namaJurusan}")
        print()


