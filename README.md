# PRAKTIKUM 4 - PERTEMUAN 9
## LATIHAN

Berikut ini adalah tugas  dari Latihan, bisa dilihat pada gambar berikut:<p>
![gambar1](ss/ss1.png.png)

### PENJELASAN

Berikut ini source code dari tugas Latihan<p>
![gambar2](ss/ss2.png.png)

![gambar3](ss/ss3.png.png)

Berikut hasil (output)dari souce code tugas Latihan<p>
![gambar4](ss/ss4.png.png)

## LAB1

Berikut ini adalah tugas dari Pertemuan 9, bisa dilihat pada gambar berikut:<p>
![gambar5](ss/ss5.png.png)

dan berikut ini hasil yang diharapkan setelah program berjalan :<p>
![gambar6](ss/ss6.png.png)

### PENJELASAN 

Berikut source code dari program sederhana Data Nilai Mahasiswa<p>
![gambar7](ss/ss7.png.png)

Didalam source code atau soal tersebut menunjukkan bahwa sistem harus menampilkan data sebanyak-banyaknya jika pengguna menginputkan Y pada pilihan Tambah Lagi ? . Sedangkan hasilnya juga harus sama, menampilkan data sebanyak yang diinputkan pengguna. Dan harus terbentuk dalam Tabel.<p>

Berikut hasil setelah saya menginputkan 2 Data Nila Mahasiswa:
![gambar8](ss/ss8.png.png)

- Pertama kita membuat variable list kosong. data = [] ulang = True<p>
Variable ulang = True digunakan untuk mengontrol perulangan<p>

- Lalu kita membuat kondisi perulangan dan statement yang akan dijalankan ketika perulangan terjadi<p>
while True: nama = input("Masukkan Nama: ") nim = input("Masukkan NIM: ") tugas = int(input("Masukkan Nilai Tugas: ")) uts = int(input("Masukkan Nilai UTS: ")) uas = int(input("Masukkan Nilai UTS: ")) nilaiakhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)<p>

data.append([nama, nim, tugas, uts, uas, int(akhir)])<p>
Dari statement diatas, kita akan diminta untuk menginput nama, nim, nilai tugas, nilai uts, dan nilai uas,lalu system akan menjumlahkan nilai-nilai tersebut dan menghasilkan nilai akhir. Setelah menginput berbagai data atau item, inputan item tersebut akan masuk ke dalam list 'nilai'<p>

- Setelah membuat perulangan, kita membuat statement untuk menghentikan atau keluar dari perulangan yang terjadi.<p>
 lagi = input ("Tambah lagi (y/t)?")<p>
   if(lagi =="t"):<p>
    break<p>

Untuk keluar dari perulangan kita hanya perlu menginputkan t apabila diminta pada saat program dijalankan.t akan membuat variable True menjadi lagi = break yang mana akan menghentikan perulangan yang terjadi.<p>

- Terakhir kita akan mencetak hasil dari program yang telah dibuat.<p>
print ("========================|=======DATA MAHASISWA==========|==============================")<p>
print ("=======================================================================================")<p>
print ("| No |	 Nama 	|    NIM    |  TUGAS  |   UTS  |  UAS  |  NILAI AKHIR    |")<p>
print ("=======================================================================================")<p>
i=0<p>
for x in data:<p>
	i+=1 <p>
	print("|{no:4d}| {nama:8s} | {nim:7s} | {tugas:7d} | {uts:6d} | {uas:5d} | {nilaiakhir:15.5f} |"<p>
		.format(no=i, nama=x[0], nim=x[1], tugas=x[2], uts=x[3], uas=x[4], nilaiakhir=x[5]))<p>
print ("=======================================================================================")<p>







