# Praktikum05
## Tugas pertemuan ke 10
```sh
Nama    : A. Reza Baehaqa Jamroni
Nim     : 312110494
Matkul  : Bahasa Perograman
```
### Latihan
• Buat Dictionary daftar kontak <p>
a={'ari':'081267888','dina':'087677776'}
• Tampilkan kontaknya Ari <p>
```sh
print('\nTampilkan Kontak Ari')
print('#    ari     |   ',a['ari'])
```
• Tambah kontak baru dengan nama Riko, nomor 087654544 <p>
```sh
print('\nMenambah Kontak Riko')
a['riko']='087654544'
```
• Ubah kontak Dina dengan nomor baru 088999776 <p>
```sh
print('\nMengubah nomor Dina ke')
a['dina']='088999776'
```
• Tampilkan semua Nama <p>
```sh
print(a.keys())
```
• Tampilkan daftar Nama dan nomornya <p>
```sh
print(a)
```
• Hapus kontak Dina <p>
```sh
del a['dina']
```
Berikut ini adalah tampilan visual studio codenya
![Gambar 1](screenshot/ss1.png)
Berikut output dari programnya yang kita bikin
![Gambar 1](screenshot/ss2.png)


### praktikum
Buat program sederhana yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan : <p>
• Program dibuat dengan menggunakan Dictionary <p>
sebelum membuat program tersebut kita perhatikan bagan flowchart berikut supaya memudahkan dalam membuatnya : 
![Gambar 1](screenshot/ss6.png)

• Tampilkan menu pilihan: (T)ambah Data, (U)bah Data, (H)apus Data, (T)ampilkan Data, (C)ari Data <p>
Disini saya menggunkan looping while agar program terus berjalan :
```sh
while True:
    c = input("\n(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")  
```
• Selanjutnya kita membuat format percabangan if, elif dan else untuk memasukan pilihan (L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")<p>
• Dengan catatan nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%) dan syntaxnya sebagai berikut :<p>

```sh
if (c.lower() == 't'):                                               
        print('\nTambah Data Mahasiswa Baru')
        nama= input("Masukkan Nama\t\t: ")                                        
        nim= input("Masukkan NIM\t\t: ")                                         
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                              
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))                                   
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))                                    
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)              
        daftar_nilai_Mhs[nama]= nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                         
        print("\nData Berhasil Ditambahkan!")
    elif (c.lower() == 'u'):                                                                    
        print('\nMengedit Data Mahasiswa')
        nama = input("Masukkan Nama: ")                                                         
        if nama in daftar_nilai_Mhs.keys():                              
            nim= input("Masukkan NIM Baru\t: ")                              
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                           
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))                           
            nilaiUas= int(input("Masukkan Nilai UAS\t: "))                           
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)          
            daftar_nilai_Mhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                      
            print("\nData Berhasil Di Update!")
        else:                                                                                    
            print("Data tidak ditemukan!")                                                       
    elif (c.lower() == 'c'):                                                                    
        print('\nCari Data Mahasiswa')
        nama = input("Masukan Nama:  ")                                                          
        if nama in daftar_nilai_Mhs.keys():                                                               
            print("\n                   DAFTAR NILAI MAHASISWA                   ")
            print("==============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==============================================================")
            print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(nama, nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir)) 
            print("==============================================================")
        else:
            print("Datanya {0} Tidak Ada ".format(nama))                                        
    elif (c.lower() == 'h'):                                                                    
        nama = input("Masukkan Nama:  ")                                                        
        if nama in daftar_nilai_Mhs.keys():                                                              
            del daftar_nilai_Mhs[nama]                                                                   
            print("Data Telah dihapus!")
        else:
            print("Data Mahasiswa Tidak Ada".format(nama))                                     
    elif (c.lower() == 'l'):                                                                    
        if daftar_nilai_Mhs.items():                                                                      
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in daftar_nilai_Mhs.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")         
    elif (c.lower() == 'k'):                                                                   
        print('\n')
        print(30*'=')
        print("Nama\t: A. Reza Baehaqa Jamroni\nKelas\t: TI.21.C5\nNIM\t: 312110494")
        print(30*'=')
```
• Terakhir saya menggunakan perintah break untuk mengkhiri perulangan pada suatu programnya<p>
Berikut ini adalah sebagian dari tampilan visual studio codenya
![Gambar 1](screenshot/ss3.png)
Berikut ini adalah contoh dari output programnya dengan pilihan (L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar
![Gambar 1](screenshot/ss4.png)
![Gambar 1](screenshot/ss5.png)
