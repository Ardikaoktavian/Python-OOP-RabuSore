# membuat list ditandai dengan [ ]

buah = ["mangga", "melon", "jeruk", "apel"]
# indeks 0                      1            2              3

# Untuk mengakses menggunakan indeks
# Dan indeks dimulai dari 0

#cetak mangga
print(buah[0])

# manambah list  menggunakan append ("value")
buah.append("pisang")
print(buah)

# mengubah list
# variabel [index keberapa] = nilai baru
buah[0] = "jambu"
print(buah)

# menghapus list
# del buah[index yg mau dihapus]
del buah[1]
print(buah)

# mengambil data akhir menggunakan pop
print(buah.pop())

# mengetahui jumlah data dari list
# menggunakan len
print(len(buah))

# menyisipkan data sesuai index yg diinginkan
# menggunakan insert (index, value)
buah.insert(1, "duku")
print(buah)

# mengambil seluruh data di list
# menggunakan perulangan for
for i in buah:
    # apa yg dieksekusi ??
    print(i)