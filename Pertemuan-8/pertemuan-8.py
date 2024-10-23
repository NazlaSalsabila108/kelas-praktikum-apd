angka = int(input("Masukkan angka: "))
print(angka)

# index error
angka = [1,2,3,4,5]

for i in angka:
    print(i[6])
print(angka[6])

# key error 
sosmed = {
    "ig": "@nazlasalsabila",
    "fb": "nazla"
}

print(sosmed["wa"])

try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input yang anda masukkan bukan angka")
except IndexError:
    print("Input yang anda masukkan bukan angka")

try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input yang anda masukkan bukan angka")
else:
    print(f"Angka yang kamu input: {angka}")
finally:
    print("Program selesai")

try:
    nama = int (input("Hello, what's your name? "))
    if len(nama) > 5:
        raise ValueError("Nama tidak boleh lebih dari 5karakter")
except ValueError as e:
    print(e)

nama = input("Masukkan nama: ")
namabaru = nama.capitalize()

print(nama)
print(namabaru)

def nama ():
    return "nama"

namabaru = nama()
print(namabaru)