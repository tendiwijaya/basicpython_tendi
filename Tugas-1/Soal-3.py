submit_nilaiujianteori = float(input("Nilai Ujian Teori: "))
submit_nilaiujianpraktek = float(input("Nilai Ujian Praktek: "))

if submit_nilaiujianteori >= 70 and submit_nilaiujianpraktek >= 70:
    print("Selamat, anda lulus!")
elif submit_nilaiujianteori >= 70 and submit_nilaiujianpraktek <= 70:
    print("Anda harus mengulang ujian praktek.")
elif submit_nilaiujianteori <= 70 and submit_nilaiujianpraktek >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")