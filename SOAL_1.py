data_mahasiswa = []

while True :
    nim = input("masukan nim:")
    nama = input("masukan nama:")
    data_mahasiswa.append({"NIM": nim, "Nama": nama})
    tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").lower()
    if tambah_lagi == "tidak":
        break

print("\nData Mahasiswa:")
for mahasiswa in data_mahasiswa:
        print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")




