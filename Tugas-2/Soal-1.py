contact = {}

print("Selamat datang! \n\n --- Menu --- \n \n 1. Daftar Kontak \n 2. Tambah Kontak \n 3. Keluar")
selection=int(input("Pilih menu: "))

while selection != 3 :
    if selection==1:
        for k, v in contact.items():
            print("Nama: {} \n No. Telepon: {}".format(k, v))
        selection=int(input("Pilih menu: "))
    elif selection==2:
        nama = input("Input Nama: ")
        telepon = input("Input No. Telepon: ")
        contact[nama] = telepon
        print("Contact sukses ditambahkan! \n\n")
        selection=int(input("Pilih menu: "))
    else:
        print("Menu tidak tersedia!")
        selection=int(input("Pilih menu: "))
        
print("Program selesai, sampai jumpa!")
