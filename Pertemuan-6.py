daftar_buku = {
"Buku1" : "Harry Potter",
"Buku2" : "Percy Jackson",
"Buku3" : "Twillight"
}
print(daftar_buku["Buku1"])
print(daftar_buku["Buku2"])
print(daftar_buku["Buku3"])


Biodata = {
"Nama" : "Aldy Ramadhan Syahputra",
"NIM" : 2109106079,
"KRS" : ["Program Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" :True,
"Social Media" : {
"Instagram" : "@aldyrmdhns_",
"Discord" : "\'Izanami#6848"
}
}

print(Biodata["KRS"][0])
print(Biodata["Social media"]["Email"])

Games = {
    "Game1" : "PUBG Mobile",
    "Game2" : "Mobile Legends",
    "Game3" : "COC"
}

games = dict(Sekiro = "Action", Pokemon = "Adventure",
Valorant = {"nama": {123 : "Informatika"}})
print(games['Valorant']['nama'][123])


Games = {
    "Game1" : "PUBG Mobile",
    "Game2" : "Mobile Legends",
    "Game3" : {
        "nama" : "COC",
        "genre" : "Strategy"
    }
}
    
print((Games.get('Games3')).get('genre'))

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#tanpa menggunakan items 
for i in Nilai: 
    print(i)
print("")

#menggunakan items
for mapel, nilai in Nilai.items():
    print(f"Nilai {i} anda adalah {nilai}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
#Sebelum Ditambah
print(Film)


Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller", 
             "Rush Hour" : "Comedy", 
             "Oblivion" : ["nazla",18]})

# Setelah Ditambah
print(Film)

# Penggunaan del 
del Film ['Avenger Endgame']
print(Film)

simpan = Film.pop('Oblivion')
# Film.clear()
print(simpan)
print(Film)

print("Jumlah Film = ", len(Film))

movies = Film.copy()
print(movies)
print("Jumlah Film = ", len(movies))

key = "apel", "jeruk", "mangga"
value = 1,2,3
buah = dict.fromkeys(key, value)
print(buah)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#menggunakan keys
for i in Nilai.keys():
    print(i)

print("")
#menggunakan value
for i in Nilai.values():
    print(i)


Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "TheParis"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
print("")


mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
for key_a, value_a in value.items():
    print (key_a, " : ", value_a)
print("")


nama_mata_pelajaran = {
    "Matematika" : 90,
    "Fisika" : 80,
    "Biologi" : 80,
    "Kimia" : 70

}

total_nilai = 0
for i in nama_mata_pelajaran.values():
    total_nilai += i
print(f"total nilai mata pelajaran{total_nilai}")
print(f"rata rata nilai adalah {total_nilai/4} ") 

angkatan = {
    "nama" : "nazla",
    "umur" : "18",
    "nim" : "2409106108",
    "jurusan" : "informatika",
    "angkatan" : "2024"
}

print(angkatan)
angkatan["fakultas"] = input("Masukkan Fakultas:")
print(angkatan)
ubah = input("ubah key:")
angkatan[ubah] = input("value baru: ")
print(angkatan)
hapus = input("hapus value: ")
del angkatan[hapus]
print(angkatan)