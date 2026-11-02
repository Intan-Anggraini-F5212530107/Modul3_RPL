print("1. File jalan")

from models.anggota_model import AnggotaModel
print("2. Import berhasil")

model = AnggotaModel()
print("3. Model berhasil dibuat")

print("=== Menambah Data Anggota ===")
model.create_anggota("Intan", "Palu")
print("4. Data berhasil ditambahkan")

print("\n=== Daftar Anggota ===")
daftar_anggota = model.get_all_anggota()
print("5. Data berhasil diambil")

for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")