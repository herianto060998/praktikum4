print("Membuat List dengan 5 elemen")
daftar = [9, 7, 5, 6, 8]
print(daftar)
# Akses List
print("Menampilkan elemen ke 3")
print(daftar[2])

print("Ambil nilai elemen ke 2 sampai ke 4")
print(daftar[1:4])

print("Ambil nilai terakhir")
print(daftar[-1])

# Ubah element list
print("ubah elemen ke 4 dengan nilai lainnya")
daftar[3] = 2
print(daftar[3])

print("ubah elemen ke 4 sampai dengan elemen terakhir")
daftar[3:5] = [17, 19]
print(daftar)

# Tambah Element List
print("ambil 2 bagian dari list pertama(A) dan jadikan list ke2(B)")
baris = daftar[3:5]
print(baris)

print("tambah list B dengan nilai string")
baris.append("Heri")
print(baris)

print("Tambah list B dengan 3 nilai")
baris.append(["Simamora", 3, 2])
print(baris)

print("Menggabungkan list A dnegan List B")
gabung = daftar + baris
print(gabung)







   
