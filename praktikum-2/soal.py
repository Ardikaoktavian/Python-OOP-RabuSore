hasil_akhir = [
    {'nama' : 'Reza', 'nilai' : 70},        #index ke -0
    {'nama' : 'Ciut', 'nilai' : 63},           #index ke -1
    {'nama' : 'Dian', 'nilai' : 80},        #index ke -2
    {'nama' : 'Badu', 'nilai' : 40}         #index ke -3
]

def lulus_saja(data):
    # apa yang akan kita lakukan ?
    # pengecekan nilainya
    for hasil in data:
        # yang mau di cek apa ?
        # melakukan pengkondisian
        if hasil['nilai'] > 65:
            print(hasil['nama'])

lulus_saja(hasil_akhir)