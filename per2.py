angka1 = int (input('masukkan angka pertama : '))  
angka2 = int (input('masukkan angka kedua   : '))
print('operator :\n1.penjumlahan \n2.pengurangan \n'
        '3.perkalian \n4.pembagian')
pilih = int(input('Masukkan operator : '))
if pilih == 1:
    tambah = angka1+angka2
    print('Hasilnya Adalah ',tambah)
elif pilih == 2:
    kurang = angka1-angka2
    print('Hasilnya adalah', kurang)
elif pilih ==3:
    kali = angja1*angka2
    print('hasinya adalah ',kali)
elif pilih ==4:
    bagi = angka1/angka2
    print('Hasilnya adalah ',bagi)
else:
    priint(' Operator yang akan di masukkan tidak ada')
