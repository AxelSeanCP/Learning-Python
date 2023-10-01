#----variabel
#penulisan variabel langsung, tidak pake int, bool, float, dll
#nama = "Axel"

#----input
'''
nama = input("Masukkan nama anda : ")
print(nama)
'''

#----data type (primitive)
'''
gaji = 1000
print(type(gaji))
#output : <class 'int'>

#print multi line
tes = """halo apakah
saya goblok
mungkin saja iya"""
print(tes)
'''

#----print input
#name = "axel" #input("Masukkan nama anda : ")

#print(f"Nama saya adalah, {name}") #formatted string
#print("Nama saya adalah, %s" % (name)) #%-formatting
#print("Nama saya adalah, {}" .format(name)) #str.format()
#print("Nama saya adalah, " + name) #format from java

#----data type(collection)

#--list (data tidak harus sama -> int,float,string,dll)
#myList = [1,"Meltryllis",True]
#print(myList[1])
#list bersifat mutable -> bisa diubah isinya
"""
myList[0] = "aku"
myList[1] = "suka"
myList[2] = "meltryllis"
print(myList)
"""

#indexing
#myList[-1] #-> True

#slicing -> sequence[start:stop:step]
"""
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0:5:2]) #ambil mulai dari start terus lompat 2, pas lompatan ke 2 ambil
print(x[1:]) #ambil mulai dari 1 sampai selesai
print(x[:3]) #ambil semua sampai 3
"""


#--tuple (sama seperti list tapi isi tidak dapat diubah / const)
#variable_tuple = (1, "Meltryllis", 2.1) #tuple pake kurung ()
#dapat indexing + slicing di tuple

#--set (unordered jadi tidak bisa indexing karena tidak punya index, set bersifat unik jadi tidak ada data yang double)
'''
variable_set = {1,2,3,5,13,2,5,10,1}
print(variable_set)
"""set adalah himpunan dalam matematika. 
Ini maknanya Anda dapat melakukan operasi union (gabungan) dan intersection (irisan) pada set. 
Python menyediakan method “.union()” dan “.intersection()” untuk tipe data set."""

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set1.union(set2)
print("Union: ", union)

intersection = set1.intersection(set2)
print("Intersection: ", intersection)
'''

#--dictionary (pasangan key: value)
'''
"""dictionary didefinisikan kurawal {}
, setiap pasangan dipisahkan koma (,)
, key dan value dipisahkan titik dua (:) 
, key dan value dapat berupa variabel/objek apapun"""

x={'nama': 'Axel Sean', 'umur': 20, 'pacarnyaMeltryllis': True}
print(x['nama']) #panggilnya begini

x['pekerjaan'] = "Web Developer" #buat nambah data
del x['pekerjaan'] #buat hapus data
x['nama'] = "Ghost Axel" #buat ganti data
'''


#----Konversi antar tipe data
#float -> int = int(5.0)
#int -> float = float(5)
#int/float -> string = str(25) / str(25.6)
#string -> int/float = int("25") / float("25.6")
#konversi ke string harus valid

#--konversi kumpulan data
#-> set = set([1,2,3,2,3]) => {1,2,3}
#-> tuple = tuple({5,6,7}) => (5,6,7)
#-> list = list('hello') => ['h','e','l','l','o']
#-> dictionary = dict([[key,value], [key2,value2]]) => {key: value, key2: value2}


#----transformasi string
#str -> string ("axel".method())
#str.upper() -> jadi uppercase
#str.lower() -> jadi lowercase
#str.rstrip() -> hapus whitespace di kanan string
#str.lstrip() -> hapus whitespace di kiri string
#str.strip() -> hapus whitespace di awal dan akhir string
#str.strip("code") -> hapus kata "code" di string
#str.startswith('Meltryllis') -> cek apakah string dimulai dengan 'Meltryllis'
#str.endswith('Meltryllis') -> cek apakah string diakhiri dengan 'Meltryllis'
#str.join() -> join banyak string jadi 1 => print(" ".join(["aku","punya","ini"])) print("123".join(["aku","punya","ini"])) " " adalah delimiter
#str.split() -> buat memisahkan string jadi list => print("aku punya ini".split()) -> ["aku","punya","ini"]
#str.split('\n') -> sama tapi per baris
#str.replace("old","new") -> ganti kata di dalam string (case sensitive)

#--pengecekan string
#.isupper() -> cek apakah uppercase
#.islower() -> cek apakah lowercase
#.isalpha() -> cek apakah semuanya huruf alfabet
#.isalnum() -> cek apakah semuanya alfanumerik
#.isdecimal() -> cek apakah semuanya angka
#.isspace() -> cek apakah hanya whitespace
#.istitle() -> cek apakah setiap huruf pertama kapital

#--formatting string
#zfill(5) -> menambah angka 0 hingga panjang yg ditentukan (5)
"""teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number) #0Code"""

#rjust(20) -> buat jadi rata kanan sesuai panjang (20)
"""print('Dicoding'.rjust(20))
print('Dicoding'.rjust(20, '!'))"""

#ljust(20) -> buat jadi rata kiri sesuai panjang (20)
#center(10, '-') -> buat string jadi di tengah, tambah whitespace/karakter lain di kanan dan kiri string

#--string literals
#--escape character
#str = 'jum\'at'
#\' single quote
#\" double quote
#\t tab
#\n newline
#\\ backslash

#--raw string -> print seadanya
#print(r'Dicoding\tindonesia')


#----operasi pada list,set, dan string
#--len -> menghitung panjang / jumlah pada list, set, dan string
#contoh:
"""listku = [1,2,4,5,3,7,5,9,7]
print(len(listku))"""

#--min / max 
"""listku = [1,5,12,17,20,30,44]
print(min(listku))
print(max(listku))"""

#--count -> menghitung sudah muncul berapa kali
"""genap = [2,4,4,6,6,6,6,8,8,8,10]
print(genap.count(6))

kalimat = "Belajar python itu menyenangkan ya gaes yak"
potong = "a"
print(kalimat.count(potong))
"""

#--in dan not in
"""kalimat = "Belajar python itu menyenangkan ya gaes yak"
print('Belajar' in kalimat) #apakah kata "Belajar" ada di kalimat -> true
print('Meltryllis' in kalimat) #apakah kata "Meltryllis" ada di kalimat -> false
print('Belajar' not in kalimat) #apakah kata "Belajar" tidak ada di kalimat -> false
print('Meltryllis' not in kalimat) #apakah kata "Meltryllis" tidak ada di kalimat -> true
"""

#--destructuring (memberikan nilai pada beberapa variabel)
"""data = ["hoodie", "biru", "M"]
jenis, warna, ukuran = data #jumlah variabel harus sama dengan panjang list
print(data, jenis, warna, ukuran)"""

#--sort
#sort tidak dapat mengurutkan list yang ada string & angka
#sort mengurutkan sesuai ASCII -> kapital dulu baru lowercase => Pesawat > motor
"""kendaraan = ["motor", "mobil", "Helikopter", "pesawat"]
kendaraan.sort() #disort secara asc sesuai huruf pertama
kendaraan.sort(reverse=True) #disort secara desc
print(kendaraan)"""


#----ekspresi
#result = 1+2 -> contoh ekspresi umum
"""angka = [2,4,6,8]
huruf = ['P','Y','T','H','O','N']
hasil = angka+huruf
print(hasil)

learn = ['P','Y','T','H','O','N']
replikasi = learn * 2
print(replikasi)"""

#--biner -> yg biasanya +,-,*,:,>,<,!
#--uner
"""a = True
a = not a
print(a)

b = 5
b += 1
print(b)

c = 8
c -= 1
print(c)

d = 10
print(-d)"""

#--operator
#+, -, *, //(pembagian bulat), /(pembagian ril), %, **(pangkat)

#--operator relasional
#== sama dengan
#!= tidak sama dengan
#> >= < <=

#--operator logika
# AND &
# OR |
# NOT

#--operator assignment
# +=, -=. *=, %=, /=

#----oneliner (kode 1 baris)
#tukar variabel
"""x = 1
y = 2
x, y = y, x
print(x, y)"""

#----if else
#--if & else
"""score = 100
if score == 100: #setelah if pake :
    print("Nilai yang sempurna") #indentasi penting untuk tau awal dan akhir block code
else:
    print("Nilai yang jelek :(")"""
#if score == 100: print("Nilai yang sempurna")
#python menganggap nilai 0 dan null false seperti javascript jadi ada value truthy dan non truthy

#--elif (else if)
"""nilai = 67

if nilai>=80:
    print("A")
elif nilai>=70:
    print("B")
elif nilai>=60:
    print("C")
else:
    print("D")"""

#--ternary operator
"""status = True
print("Selamat anda lulus") if status else print("Hiyaaa goblok amat jadi orang")"""

#----loopipng
#--for
#for <var> in <iterable>: <statement(s)>
#iterable -> yang bisa di buat loop seperti list, set, string
"""for i in range(10): #range(start,stop(eksklusif),step) #eksklusif -> nilai terakhir ga masuk
    print(i) #0-9 karena range mulai dari 0"""

#--while
"""counter = 1
while counter<=5:
    print(counter)
    counter+=1
"""

#--nested for
"""for i in range(1,3):
    for j in range(1,3):
        print(i,j)"""

#--break & continue
"""for i in range(1,3):
    for j in range(1,10):
        print(j)
        if j==4:
            continue #break"""

#--else setelah for
"""numbers = [1,2,3,4,5]

for num in numbers:
    if num==4:
        print("Angka telah ditemukan")
        break
else:
    print("Angka tidak ditemukan")"""
#if dan else berkaitan meskipun beda block, jika if jalan maka else ga jalan

#--else setelah while
"""count = 0

while count < 3:
    print("Meltryllis")
    count += 1
else: #bakal jalan kalo while false -> jadi kalau di break (while masih true) gajalan
    print("cantik")"""

#--pass
"""x = 10

if x > 5:
    pass #pass -> ga ngapa ngapain / skip
else:
    print("Nilai x tidak memenuhi kondisi")"""

#--list comprehension
#cara lama
"""angka = [1,2,3,4]
pangkat = []

for n in angka:
    pangkat.append(n**2)

print(pangkat)
#cara baru
#new_list = [expression for_loop_one_or_more_conditions]
pangkat = [n**2 for n in angka]
print(pangkat)"""