ulang = 10
for i in range(ulang) :
    print("Perulangan ke-" + str(i))

for i in range(2,10) :
    print(f"halo {i}")

for i in range(2,10,2) :
    print(f"halo {i}")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung = hitung + 1
    jawab = input("Ulang lagi tidak?")
    print(f"Total perulangan: {hitung}")

while True:
    print("halo")

hitung = 0
while True:
    hitung += 1
    ulang = input("Masih Ingin Mengulang? ")
    if ulang == "tidak" or ulang =="Tidak":
        break

print(f"Total Perulangan: {hitung}")

while True:
    print("halo")
    break

print("Daftar bilangan ganjil dari 1-10")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

kelasC = ["nazla", 2409106108]

for i in range(len(kelasC)):
    print(f"{i+1}. {kelasC[i]}")
print(kelasC)