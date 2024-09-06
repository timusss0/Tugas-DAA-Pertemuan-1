angka_pertama = int(input("Masukkan angka pertama: "))

angka_kedua = int(input("Masukkan angka kedua: "))

if angka_pertama > angka_kedua:
    print("Angka terbesar adalah:", angka_pertama)
elif angka_kedua > angka_pertama:
    print("Angka terbesar adalah:", angka_kedua)
else:
    print("Kedua angka sama besar.")
