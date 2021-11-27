nilai=[]
perulangan = True

while perulangan:
   nama=input('masukkan nama:')
   nim=input('masukkan nim:')
   tugas=input('masukkan nilai tugas:')
   UTS=input('masukkan nilai UTS:')
   UAS=input('masukkan nilai UAS:')
   nilaiakhir=(int(tugas)*.30) + (int(UTS)*.35) + (int(UAS)*.35)
   
   nilai.append([nama, nim, tugas, UTS, UAS, int(nilaiakhir)])
   if(input('tambah data (y/t)?') == 't'):
       perulangan = False

i=0
for item in nilai:
    i+= 1
    print("|{no:2d}|{nama:12s}|{nim:9s}|{tugas:5d}|{UTS:5d}|{UAS:5d}|{nilaiakhir:6.2f}|"
        .format(no=i, nama=item[0], nim=item[1], tugas=item[2], UTS=item[3], UAS=item[4], nilaiakhir=item[5]))

