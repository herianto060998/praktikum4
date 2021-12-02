data=[]

while True:
   nama =input('Masukkan nama             :')
   nim =input('Masukkan NIM              :')
   tugas=int(input('Masukkan nilai Tugas      :'))
   uts = int(input('Masukkan nilai UTS        :'))
   uas = int(input('Masukkan nilai UAS        :'))
   nilaiakhir= (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
   
   data.append([nama, nim, tugas, uts, uas, int(nilaiakhir)])
   lagi = input ("Tambah lagi (y/t)?")
   if(lagi =="t"):
    break

print ("========================|=======DATA MAHASISWA==========|==============================")
print ("=======================================================================================")
print ("| No |	 Nama 	|    NIM    |  TUGAS  |   UTS  |  UAS  |  NILAI AKHIR    |")
print ("=======================================================================================")
i=0
for x in data:
	i+=1
	print("|{no:4d}| {nama:8s} | {nim:7s} | {tugas:7d} | {uts:6d} | {uas:5d} | {nilaiakhir:15.5f} |"
		.format(no=i, nama=x[0], nim=x[1], tugas=x[2], uts=x[3], uas=x[4], nilaiakhir=x[5]))
print ("=======================================================================================")
