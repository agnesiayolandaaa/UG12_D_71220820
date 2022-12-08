print ("Table Matematika Nich")
print ("Pilihan Model Matematika")
print ("1. Perkalian")
print ("2. Pembagian")
model= int(input("Masukkan model matematika yang diinginkan 1/2:"))
table= int(input("Menampilkan table matematika dari angka:"))

if (model==1) :
 for i in range(1, 11):
    print(table, 'x', i, '=', table*i)
elif (model==2):
 for i in range(50,66):
    print(i, ':', table, '=', i/table)
else:
    print("Pilihan tidak tersedia, jangan ngasal!")
