# nama = ["nazla", 108, True,] ["yuyun", 145], 3.96,[123,"ALVITO", False, 3.66],"rehan"
# matkul = [  "APD", 
#             "APL",
#             "WEB",
#             "JARKOM",
#             "BASDAT",
#             "STRUKDAT",
#             "PTI",
#             "KALKULUS",
#             "PROBAS"]

# print(matkul[6])

# makanan = ["Bakso","Sate","Soto", "nasi goreng", "mie ayam", "cumi bakar", "ayam bakar"]
# print("Sebelum: ")
# print(makanan[2:5])
# makanan.append ("Nasi Goreng")
# print("Sesudah: ")
# del makanan [5]
# data = makanan.pop(5)
# print(makanan)
# print(data)
# print(makanan)
# makanan.insert(3,"Nasi Goreng")
# makanan[0] = ["ayam goreng", "bebek goreng"]
# print(makanan)

# # minuman 6. 3(dihapus) 6(air putih) 1(jus tomat)

# minuman=["Pocari","Josu","Es teler","Es teh jumbo","Bintang","Minuman Anak-anak"]
# print("Sebelum: ")
# print(minuman)
# del minuman [2]
# print("Sesudah: ")
# print(minuman)
# minuman[4]="air putih"
# print(minuman)
# minuman.insert(0,"jus tomat")
# print(minuman)

# makanan = ["ayam", "ikan",["bakso","soto","sate","ikan","bebek"],
#            ["teh","kopi","air"]]

# for i in makanan:
#     for j in i :
#         print(j, end=", ")

# for i in makanan :
#     if isinstance(i, list):
#         for j in i :
#             print(j)
#     else:
#         print(i)

# for i in makanan:
#     for j in i :
#         print(i)

akuns = []

while True: 
    print("Halo! Selamat datang di aplikasi catatan")
    print("Silahkan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("_________________________")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username: #Memeriksa apakah username sudah ada 
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            password = input("Password: ")
            akuns.append([Username, Password,[]]) #Simpan username, password, dan catatan (sebagai list kosong)
            print(f"Akun anda berhasil terdaftar dengan ID: {Username}")