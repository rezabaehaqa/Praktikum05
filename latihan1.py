print('tugas pertemuan 10')
print('praktikum5')
print('nama\t: A. Reza Baehaqa Jamroni\nkelas\t: TI 21 C5\nNIM\t: 312110494\n')

a={'ari':'081267888','dina':'087677776'}
print('Kontak awal')
print('================================')
print('#    nama    |   nomor telepon')
print('================================')
print('#    ari     |   081267888','\n#    dina    |   087677776')

# tampilkan kontak ari
print('\nTampilkan Kontak Ari')
print('#    ari     |   ',a['ari'])
print('\nMenambah Kontak Riko')
a['riko']='087654544'
print('#    ari     |   ',a['ari'])
print('#    dina    |   ',a['dina'])
print('#    riko    |   ',a['riko'])
print('\nMengubah nomor Dina ke')
a['dina']='088999776'
print('#    ari     |   ',a['ari'])
print('#    dina    |   ',a['dina'])
print('#    riko    |   ',a['riko'])
print('\nMenampilkan semua nama')
print(a.keys())
print('\nMenampilkan semua nomor')
print(a.values())
print('\nMenampilkan semua nama dan nomor')
print(a)
print('\nMenghapus kontak dina')
del a['dina']
print(a,'\n')