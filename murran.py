print("=====NILAI SISWA=====")

Nilai_siswa = int(input("Masukan nilai siswa : "))
print("")
if Nilai_siswa >=95 and Nilai_siswa <100:
    print("Maka nilai kriteria siswa adalah : A+ ")
elif Nilai_siswa >=90 and Nilai_siswa <95:
    print("Maka nilai kriteria siswa adalah : -A ")
elif Nilai_siswa >=85 and Nilai_siswa <90:
    print("Maka nilai kriteria siswa adalah : B+ ")
elif Nilai_siswa >=80 and Nilai_siswa <85:
    print("Maka kriteria nilai siswa adalah : B ")
elif Nilai_siswa >=70 and Nilai_siswa <75:
    print("Maka nilai kriteria siswa adalah :  D ")

#tugas 1
down = 0
up = 100

for i in range(1,10):
    guessed_egde = (int(up + down )/ 2)
    answer = input("are you" + str(guessed_egde))
    if answer == "correct":
        print("nice")
    elif answer == 'less':
        up = guessed_egde
    elif answer == 'more':
        down = guessed_egde
    else:
        print("wrong answer")

#tugas 2
#Bilangna genap
def contains_even_number(i):
    for ele in i:
        if ele % 2 == 0:
            print("list berisi tentang bilangan genap")
            break
    else:
        print("list tidak berisi bilangan genap")

print("for list 1 : ")
contains_even_number([1, 9, 8])
print(" \n for :list 2 : ")
contains_even_number([1, 3, 5])

#tugas 3
#menginput angka
angka = int(input("masukan angka : "))

#jika habis di bagi 0,maka genap
if (angka % 2) == 0:
    print("{0} adalah bilangan genap".format(angka))
#jika tidak habis dibagi 2 maka habis
else:
    print("{0} adalah bilangan ganjil".format(angka))

#tugas 4
#menginput nilai tugas , uts dan uas
tugas = float(input("Masukan nilai tinggi : "))
uts = float(input("masukan nilai uts : "))
uas = float(input("masukan nilai uas : "))
#menghitung nilai tugas, uts dan uaa
nilai = (0,15 * tugas) + (0,35 * tugas) + (0,50 * uas)
#menghitung keseluruhan
if nilai > 100:
    grade = 'A'
elif nilai > 90:
    grade = 'B'
elif nilai > 80:
    grade = 'C'
elif nilai > 70:
    grade = 'D'
else:
    grade = 'e'

#menentukkan status kelulusan berdasarkan nilai akhir
if nilai > 60:
    status = 'lulus'
else:
    status = 'tidak lulus'
#menampilakan nilai akhir
print("nilai akhir 0,2f" % nilai)
print("grade: {}".format(grade))
print("status {}".format(grade))





