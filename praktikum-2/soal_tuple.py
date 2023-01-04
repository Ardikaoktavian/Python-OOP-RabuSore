#membuat tuple menggunakan buka tutup kurung  ("value",....)
gorengan = ('bakwan', 'combro', 'misro')                
sop = ('sop iga', 'sop buntut', 'sop kaki')
nasi = ('nasi uduk', 'nasi goreng', 'nasi remes')

# tuple di dalam tuple
makanan = (gorengan, sop, nasi)
# index               0              1       2

# cetak gorengan dari variable makanan dikeluarkan dari buka tutup kurung
for i in makanan[0] :
    print(i)
    
# cetak sop buntut
print(makanan[1] [1])
print(sop[1])

# cetak nasi remes
print(nasi[2])
print(makanan[2][2])

# cetak seluruh keluar dari tutup kurung
for i in makanan:
    for detail_makanan in i :
        print(detail_makanan)