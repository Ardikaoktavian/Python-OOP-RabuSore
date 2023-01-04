# membuat  class mahasiswa
class Mahasiswa :
    # atribut
    # konstrukor
    def __init__(self, nim, nama, rombel) :
        # variabel objek
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
        
    # method 
    def lulus(self, nilai):
        if (nilai > 90):
            print("LULUS")
        else :
            print("TIDAK  LULUS")
            
# class mahasiswa memiliki 3 atribut dan 1 fungsi

    def cetak(self) :
        print("Nama :", self.nama)
        print("Nim :", self.nim)
        print("Rombel :", self.rombel)
        

# membuat objek 
mahasiswa1 = Mahasiswa("011021", "Sugianto", "TI-05")

# mencetak atribut
mahasiswa1.cetak( )
mahasiswa1.lulus(95)

print("\n")
# membuat objek ke 2
mahasiswa2 = Mahasiswa("012302", "Anjasmara","TI-14")

# mencetak atribut
mahasiswa2.cetak( )
mahasiswa2.lulus(85)

# print(help(mahasiswa1))