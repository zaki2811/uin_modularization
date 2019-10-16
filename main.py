nama = 'zakiyyallah mushoffa'
program = 'Usaha'

print(f'Program {program} oleh {nama}')


def hitung_usaha(gaya, jarak):
    usaha = gaya * jarak
    print(f'gaya = {gaya}N pada jarak = {jarak}m')
    print(f'Sehingga usaha = {usaha} joule')
    return usaha


usaha = hitung_usaha(100, 5)
usaha = hitung_usaha(300, 70)

