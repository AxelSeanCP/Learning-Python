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

#print input
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


#note : ctrl+k+s (set shortcut custom) -> run python file -> shift+` (29/09/2023) 