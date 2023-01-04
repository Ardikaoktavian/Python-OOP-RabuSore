# membuat  dictionary 
#  ( key :  value)

data = {"nama" : "Ferdy Simba Purnomo"}
#                key    :       value

# akses value menggunakan key
print(data["nama"])

#mengakses value dengan function values()
nilai = { 'Firda':89, 'Inaya':80, 'Fawwaz':95, 'Rahmah':100 }

#mencetak valuenya saja dapat menggunakan fungsi value()
for skor in nilai.values():
    print(skor)
    
#mencetak keynya saja dapat menggunakan fungsi value()
for nama in nilai.keys():
    print(nama)
    
#mencetak key dan value dapat menggunakan fungsi items()
for nama,nilai in nilai.items():
    print(nama, ":", nilai)