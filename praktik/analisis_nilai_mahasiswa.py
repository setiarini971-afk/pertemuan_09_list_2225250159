def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []

    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)

    return lulus


def analisis_nilai(nilai):
    lulus = nilai_lulus(nilai)

    print("Data           :", nilai)
    print("Banyak data    :", len(nilai))
    print("Total          :", sum(nilai))
    print(f"Rata-rata      : {rata_rata(nilai):.2f}")

    if len(nilai) > 0:
        print("Minimum        :", min(nilai))
        print("Maksimum       :", max(nilai))
    else:
        print("Minimum        : Tidak ada data")
        print("Maksimum       : Tidak ada data")

    print("Nilai lulus    :", lulus)
    print("Jumlah lulus   :", len(lulus))
    print("Belum lulus    :", len(nilai) - len(lulus))


print("=== PROGRAM ANALISIS NILAI MAHASISWA ===")
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
analisis_nilai(nilai)


print("\n=== TEST CASE 1 ===")
data = [60, 70, 80]
print("Rata-rata, harapan 70.00:", f"{rata_rata(data):.2f}")
print("Minimum, harapan 60:", min(data))
print("Maksimum, harapan 80:", max(data))
print("Jumlah lulus, harapan 3:", len(nilai_lulus(data)))


print("\n=== TEST CASE 2 ===")
data = [59, 60, 61]
print("Nilai lulus, harapan [60, 61]:", nilai_lulus(data))
print("Jumlah lulus, harapan 2:", len(nilai_lulus(data)))


print("\n=== TEST CASE 3 ===")
data = []
print("Rata-rata list kosong, harapan 0:", rata_rata(data))