# PROGRAM BMI

tinggi = int(input("Tinggi : "))
berat = int(input("Berat : "))

tinggi = tinggi / 100
bmi = berat / (tinggi * tinggi)
print("Hasil ", bmi)

if bmi > 0:
    if bmi <= 14:
        print("Terlalu kurus")
    elif bmi <= 16:
        print("Kurus")
    elif bmi <= 18:
        print("Normal")
    elif bmi <= 25:
        print("Gemuk")
    elif bmi <= 30:
        print("Terlalu Gemuk")
else:
    print("Coba Lagi!")