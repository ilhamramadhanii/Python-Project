# # print("Hello SMAN Tanjungsari")
# # Ini komen, catatan buat besok

# TIPE DATA
# # Tipe Data Boolean
# print(True)
# print(type(True))

# # Tipe Data String
# print("Hello SMAN Tanjungsari")
# print(type("Coba"))

# # Tipe Data Integer
# print(11)
# print(type(11))

# # Tipe Data Float
# print(11.5)
# print(type(11.5))

# # Tipe Data List
# list1 = ['1', 12.2, 4, 'Test']
# print(list1)
# print(type(list1))

# VARIABLE
# namaDepan = "Ilham"
# namaBelakang = "Ramadhani"
# umur = 16
# hobi = "Badminton"
# kelas = 12
# print(namaDepan, namaBelakang, umur, hobi, kelas)

# OPERATOR ARITMATIKA

# TAMBAH
# bilangan1 = 7
# bilangan2 = 9
# total = bilangan1 + bilangan2
# print(total)

# # PENGURANGAN
# bilangan1 = 10
# bilangan2 = 2
# total = bilangan1 - bilangan2
# print(total)

# # PERKALIAN
# bilangan1 = 9
# bilangan2 = 9
# total = bilangan1 * bilangan2
# print(total)

# # PEMBAGIAN
# bilangan1 = 100
# bilangan2 = 5
# total = bilangan1 + bilangan2
# print(total)

# # SISA BAGI / MODUL %
# bilangan1 = 14
# bilangan2 = 5
# total = bilangan1 % bilangan2
# print(total)

# nilai = input("Masukan Nilai : ")

# if( nilai == "A" ):
#     print("Sangat bagus")
# elif( nilai == "B" ):
#     print("Bagus")
# elif( nilai == "C" ):
#     print("Lumayan")
# elif( nilai == "D" ):
#     print("Perlu belajar")
# else:
#     print("Gagal")

# hitung = 0

# while( hitung <= 5 ):
#     print("Perulangan ke - ", hitung)
#     hitung = hitung + 1


# buah = ["jeruk", "apel", "tomat"]
# for makanan in buah:
#     print("Saya suka makan buah", makanan)

# print("========ANGKA GANJIL========")
# hitung = 1
# while(hitung <= 100):
#     print(hitung)
#     hitung = hitung + 2

# print("========ANGKA GENAP========")
# hitung = 2
# while(hitung <= 100):
#     print(hitung)
#     hitung = hitung + 2


# angka = []
# for i in range(1, 101):
#     angka.append(1)

# ganjil = []
# genap = []

# for x in angka:
#     if( x % 2 == 0 ):
#         genap.append(x)
#     else:
#         ganjil.append(x)

# def salam(nama):
#     print("Hallo", nama)

# salam("Ganteng!")

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

print("Pilih operasi 1. Tambah, 2. Kurang, 3. Kali, 4. Bagi")
pilih = input("Masukan pilihan (1/2/3/4) : ")
a = float(input("Masukan angka pertama : "))
b = float(input("Masukan angka kedua : "))

if pilih == "1":
    print("Hasil ", tambah(a, b))
elif pilih == "2":
    print("Hasil ", kurang(a, b))
elif pilih == "3":
    print("Hasil ", kali(a, b))
elif pilih == "4":
    print("Hasil ", bagi(a, b))