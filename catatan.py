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

#--try except
"""z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi dengan angka 0")"""

"""var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")"""

#--raise exception
"""var = -1
if var < 0:
    raise ValueError("Bilangan negatif ga boleh")
else:
    for i in range(var):
        print(i+1)"""

#----array
#--nilai default
#myList = [0 for i in range(10)] #deklarasi array panjang 10 semua isinya 0

#--sequence di array
"""var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1 #indeks suksesor
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")"""

#latihan cari nilai terbesar di array
"""myList = [1,7,2,89,3]

leftPointer = myList[0]

for i in range(1, len(myList)):
    rightPointer = myList[i]

    if rightPointer > leftPointer:
        leftPointer = rightPointer

print(leftPointer)"""

#----matriks
"""import numpy #library python biasa buat bikin array
matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriks)"""

#--deklarasi biasa
#matriks bersifat homogen(cuma 1 jenis int atau float dst)
#matriks = [[1,2,3],[4,5,6],[7,8,9]]

#--deklarasi default
"""matriks = [[0 for j in range(3)] for i in range(3)]
print(matriks)"""

#--akses elemen matriks
#matriks[indexkolom][indexbaris]

#--operasi pada matriks (kali konstanta)
#cara biasa
"""matriks = [[5,0],[1,-2]]

hasil = [[0 for j in range(len(matriks[i]))] for i in range(len(matriks))]

for i in range(len(matriks)):
    for j in range(len(matriks[0])):
        hasil[i][j] = matriks[i][j] * 2

print(hasil)"""
#cara numpy
"""import numpy as np
matriks = np.array([[5,0],[1,-2]])

print(matriks*2)"""

#----function
"""def luasPersegi(panjang, lebar): #(panjang, lebar) merupakan parameter
    '''ini namanya docstring (documentation string)
    Fungsi ini dibuat untuk menghitung luas persegi panjang

    Args: 
        Panjang(int): panjang persegi panjang
        lebar(int): lebar persegi panjang
    Returns:
        int: Luas persegi panjang hasil perhitungan'''
    

    luas = panjang * lebar
    return luas

persegiPertama = luasPersegi(2,4) #(2,4) merupakan argumen
print(persegiPertama)

luasPersegi(panjang=2, lebar=4) #keyword argumen, yg tadi positional
def penjumlahan(a,b, /): #positional only parameter
def greeting(*, nama, pesan): #keyword only parameter
def hitung_total(*args): #var positional parameter, semua jadi tuple
def cetak_info(**kwargs): #var keyword parameter, semua jadi dictionary"""

#--lambda expression
#func = lambda args: ret_val
"""luasPersegi = lambda panjang, lebar: panjang*lebar
print(luasPersegi(2,2))"""

#--scope
#global
"""a=10
def hitung(b):
    return a+b
print(hitung(5))"""
#lokal
"""def hitung(b):
    a=10
    return a+b
print(hitung(5))"""

#----panggil modul
"""import hello
#from hello import mencari_luas_persegi_panjang, nama #ga perlu pake hello.
persegiPanjang = hello.mencari_luas_persegi_panjang(5,10)
print(persegiPanjang)
print(hello.nama)"""

#----procedure
"""def greeting():
    print("Hello World")

greeting()"""

#----Object Oriented Programming(oop)
"""class  Mobil:
    #atribut
    warna = "Merah"

bmwM3 = Mobil()
bmwM3.warna = "hitam"
print(bmwM3.warna)"""

#mengubah atribut kelas
"""class Mobil:
    warna = "Merah"
mobil1 = Mobil()
mobil2 = Mobil()
print(mobil1.warna, mobil2.warna)
#mobil1.warna = "Hitam" #ganti yang aman
Mobil.warna = "Hitam" #ketika ganti warna lewat kelasnya langsung, maka semua keganti
print(mobil1.warna, mobil2.warna)"""

#--constructor
"""class Mobil:
    #constructor
    def __init__(self, warna, merek, tipe): #self === this di javascript
        self.warna = warna
        self.merek = merek
        self.tipe = tipe

bmwM4 = Mobil("Biru", "BMW", "Sport")
print(bmwM4.tipe)"""

#decorator -> cari sendiri di google, intinya buat nambahin fungsi sebelum dan sesudah sebuah fungsi dijalankan
#--method
"""class Mobil:
    #constructor
    def __init__(self, warna, merek, kecepatan): #self === this di javascript
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambahKecepatan(self):
        self.kecepatan += 10

bmwM4 = Mobil("Biru", "BMW", 140)
print(bmwM4.kecepatan)
bmwM4.tambahKecepatan()
print(bmwM4.kecepatan)
#Mobil.tambahKecepatan() #error karena methodnya punya objek"""

#--static method & class method
"""class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    #static method
    @staticmethod
    def introMobil():
        print("Ini adalah static method dari kelas Mobil")
    
    #class method, otomatis menambahkan kelas sebagai atribut pertama
    @classmethod
    def introMobil2(cls):
        print("Ini adalah class method dari kelas Mobil")
    
Mobil.introMobil()
Mobil.introMobil2()
mobil1 = Mobil("BMW")
mobil1.introMobil()
mobil1.introMobil2()"""

#----inheritance
"""class Mobil:
    def __init__(self, warna, merek, kecepatan): #self === this di javascript
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambahKecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil): #inheritance dengan memasukkan class parent ke parameter
    def turbo(self):
        self.kecepatan += 50
    
    def tambahKecepatan(self): #overriding
        self.kecepatan += 20

#kelas mobil dasar
kijangInova = Mobil("Biru", "Toyota", 140)
print(kijangInova.kecepatan)

#kelas mobil sport
r34 = MobilSport("Hitam","Nissan", 160)
print(r34.kecepatan)
r34.turbo()
r34.tambahKecepatan()
print(r34.kecepatan)"""

#--super
"""class Mobil:
    def __init__(self, warna, merek, kecepatan): #self === this di javascript
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambahKecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil): #inheritance dengan memasukkan class parent ke parameter
    def turbo(self):
        self.kecepatan += 50
    
    def tambahKecepatan(self): #overriding
        super().tambahKecepatan()
        print("Kecepatan anda meningkat, Hati hati")

#kelas mobil sport
r34 = MobilSport("Hitam","Nissan", 160)
print(r34.kecepatan)
r34.tambahKecepatan()
print(r34.kecepatan)"""

#----python style guide
#di terminal install pycodestyle -> pip install pycodestyle => pycodestyle kalkulator.py (buat cek ada error)
#di terminal install black -> pip install black => black kalkulator.py (buat format kode)

#install anaconda -> https://www.anaconda.com/download.