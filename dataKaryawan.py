nama = input("Nama Karyawan : ")
golongan = input("Golongan : ")
jamKerjaSatu = int(input("Jumlah jam kerja 1 : "))
jamKerjaDua = int(input("Jumlah jam kerja 2 : "))
jamKerjaTiga = int(input("Jumlah jam kerja 3 : "))
jamKerjaEmpat = int(input("Jumlah jam kerja 4 : "))

if golongan == "A":
    upahPerJam = 5000
elif golongan == "B":
    upahPerJam = 7000
elif golongan == "C":
    upahPerJam = 8000
elif golongan == "D":
    upahPerJam = 10000

totalUpahSatu = jamKerjaSatu * upahPerJam
totalUpahDua = jamKerjaDua * upahPerJam
totalUpahTiga = jamKerjaTiga * upahPerJam
totalUpahEmpat = jamKerjaEmpat * upahPerJam

if(jamKerjaSatu - 48) > 0:
    totalUpahSatu = totalUpahSatu + ((jamKerjaSatu - 48)*4000)
elif(jamKerjaDua - 48) > 0:
    totalUpahDua = totalUpahDua + ((jamKerjaDua - 48)*4000)
elif(jamKerjaTiga - 48) > 0:
    totalUpahTiga = totalUpahTiga + ((jamKerjaTiga - 48)*4000)
elif(jamKerjaEmpat - 48) > 0:
    totalUpahEmpat = totalUpahEmpat + ((jamKerjaEmpat - 48)*4000)

totalSebulan = totalUpahSatu + totalUpahDua + totalUpahTiga + totalUpahEmpat

print(nama, "menerima upah Rp.",totalUpahSatu, "per minggu pertama")
print(nama, "menerima upah Rp.",totalUpahDua, "per minggu kedua")
print(nama, "menerima upah Rp.",totalUpahTiga, "per minggu ketiga")
print(nama, "menerima upah Rp.",totalUpahEmpat, "per minggu keempat")

print(nama, "menerima upah Rp.", totalSebulan, "per bulan")