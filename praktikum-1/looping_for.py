print ( " - - - - - Cetak angka 1 sd 5- - - -")

angka= 100
for no in range(20 , angka):
    no = no + 1
    print("Angka", no)
    
print ( " - - - - - Cetak angka 1 sd 20- - - -")
for i  in range (0, 20):
    i += 1 
    print(i)

print ( " - - - - - Cetak angka 1 sd 20 genap- - - -")
for i  in range (0, 20):
    i += 1 
    if(i % 2 == 0):
        print(i)
        
print ( " - - - - - Cetak angka 1 sd 20 ganjil - - - -")
for i  in range (0, 20):
    i += 1 
    if(i % 2 == 1):
        print(i)
        
print ( " - - - - - Cetak angka 1 sd 20 ketemu 13 bakal berenti - - - -")
for i  in range (0, 20):
    i += 1 
    if(i == 13):
        break
    print(i)