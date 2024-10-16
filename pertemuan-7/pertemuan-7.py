def salam():
    print ("Selamat Pagi, FT Muda")
def kali():
    x = 6*4
    print(x)

# Membuat fungsi dengan parameter (panjang, lebar)
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print ("Luas persegi panjang:", luas)


luas_persegi_panjang(4, 6)

def luas_persegi(sisi):
    luas = sisi * sisi
    jumlah = sisi + sisi
    return luas, jumlah

hasil = luas_persegi(4) + luas_persegi(2)
print(hasil)

def mhs (nama, nim, **arr):
    print(nama)
    print(nim)
    print(arr)

mhs ("ucup", "20", data = 2, data2 = 3 )

def nilai(angka):
    if angka >= 10:
        print("1")
        # return 
    else: 
        print("2")
        # return 
    print("3")

data = 10 

def nilai():
    data = 20
    print(data)

nilai()
print(data)

def data(kumpulan):
    print(kumpulan)

value = [1,2,3,4,5]
data(value)

def mhs(nama1, nama2, nama3):
    print(nama3)
mhs(nama3 = "ucup", nama2 = "saipul", nama1 = "michael")

