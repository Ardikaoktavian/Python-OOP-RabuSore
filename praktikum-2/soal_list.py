# list makanan dengan 2 dimensi
list_makanan = [
    [ 'bakwan', 'tempe', 'tahu' ],                                 #index0
    [ 'nasi uduk', 'nasi pecel',  'sate padang' ]          #index1
]

# bagaimana memprint nasi pecel ?
print(list_makanan[1] [1] )

# bagaimana memprint semua data ?
# sampai tidak ada di dalam kotak
for i in list_makanan:
    for detail_makanan in i :
        print(detail_makanan)
