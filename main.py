nama = 'Ulung Markho Mayzebe'
program = 'Gerak Lurus'

print(f'Program {program} oleh {nama}')


def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'Sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

#jarak = 1000
#waktu = 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)

#Tugas: Buat fungsi  _APA_SAJA_YANG_KALIAN_TAHU
#DAN GUNAKAN

