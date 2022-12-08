print ("Table Matematika Nich")
print ("Pilihan Model Matematika")
print ("1. Perkalian")
print ("2. Pembagian")
model= int(input("Masukkan model matematika yang diinginkan 1/2:"))
table= int(input("Menampilkan table matematika dari angka:"))

num = int(input("Tabel perkalian: "))
 
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

table= int(input("Menampilkan table matematika dari angka:"))

num = int(input("Tabel pembagian: "))
 
for i in range(50,66):
    print(i, ':', num, '=', i/num)