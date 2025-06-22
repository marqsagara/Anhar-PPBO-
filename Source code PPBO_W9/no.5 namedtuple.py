from collections import namedtuple

# Membuat namedtuple dengan nama Mobil dan field: merk, model, tahun
Mobil = namedtuple("Mobil", "merk model tahun")

# Membuat beberapa instance dari namedtuple Mobil
mobil1 = Mobil("Toyota", "Avanza", 2018)
mobil2 = Mobil("Honda", "Civic", 2020)
mobil3 = Mobil("Suzuki", "Ertiga", 2016)

# Menyimpan semua mobil dalam list
daftar_mobil = [mobil1, mobil2, mobil3]

# Menampilkan data semua mobil
print("Daftar Mobil Showroom:")
for mobil in daftar_mobil:
    print(f"Merk        : {mobil.merk}")
    print(f"Model       : {mobil.model}")
    print(f"Tahun Rilis : {mobil.tahun}")
    print("-" * 30)
