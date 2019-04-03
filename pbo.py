#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Kubus:
    def __init__(self,s):
        self.sisi = s
    def tampilkansisi(self):
        print(self.sisi)
    def luas(self):
        print("Luas : ",self.sisi**2)
    def luaspermukaan(self):
        print("Luas permukaan :",self.sisi**2*6)
    def volume(self):
        print("volume :",self.sisi**3)

kubus1 = Kubus(4)
kubus1.tampilkansisi()
kubus1.luas()
kubus1.luaspermukaan()
kubus1.volume()


# In[11]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year

class Pegawai:
    def __init__(self,n,j,g,lahir):
        self.nama = n
        self.jabatan = j
        self.gaji = g
        self.tahunlahir = lahir
    def tampilkan(self):
        print(self.nama,",",self.jabatan,",",self.gaji*30)
    def tampilkanumur(self):
        print("Umur :",tahun - self.tahunlahir)
        
p1 = Pegawai("m.fahriz zain jannan","Direktur",500000,2000)
p1.tampilkan()
p1.tampilkanumur()


# In[3]:


class Mahasiswa:
    def __init__(self,n,no,ip):
        self.nama = n
        self.nim = no
        self.ipk = ip
    def ceklayak(self):
        if(self.ipk<3):
            print(self.nama,"tidak layak bidikmisi")
        else:
            print("Anda layak Bidikmisi")
    def datamhs(self):
        print(self.nama,",",self.nim,",",self.ipk)
        
m1 = Mahasiswa("M.fahriz zain jannan","180441100075",2.75)
m1.datamhs()
m1.ceklayak()
m2 = Mahasiswa("Siapa dia?","180441100030",3.5)
m2.datamhs()
m2.ceklayak()
print(m1==m2)


# In[1]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class pegawai:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th
    def user(self):
        print("nama",self.nama,"nim",self.nim)
    def prediksi_umur(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

pg1 = pegawai("zein","180441100075","pamekasan",8,6,2000)
pg1.user()
pg1.prediksi_umur()


# In[5]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class orang:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th

    def perkenalkan_anda(self):
        print("hello,saya", self.nama,"Nim",self.nim,"lahir_di",self.tempat_lahir,self.tanggal_lahir,self.bulan_lahir,self.tahun_lahir)
    def prediksi_umur(self):
        print("prediksi_Umur :",tahun - self.tahun_lahir,"")
    def umur_sekarang(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

org1 = orang("zein","180441100075","pamekasan",8,6,2000)
org1.perkenalkan_anda()
org1.prediksi_umur()
org1.umur_sekarang()


# In[2]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month

class Mahasiswa:
    def __init__(self,nim,nm):
        self.npm = nim
        self.nama = nm
    def perkiraan_semester(self):
        self.angkatan = "20"+self.npm[:2]
        self.angkatan = int(self.angkatan)
        self.smt = tahun - self.angkatan
        if(bulan>=2 and bulan<=7):
            if(self.smt ==1):
                self.semester = "semester 2"
            elif(self.smt ==2):
                self.semester = "semester 4"
            elif(self.smt ==3):
                self.semester = "semester 6"
            elif(self.smt ==4):
                self.semester = "semester 8"
            else:
                self.semester = "semester tua"
        if(bulan<2 and bulan>7):
            if(self.smt ==1):
                self.semester = "semester 1"
            elif(self.smt ==2):
                self.semester = "semester 3"
            elif(self.smt ==3):
                self.semester = "semester 5"
            elif(self.smt ==4):
                self.semester = "semester 7"
            else:
                self.semester = "semester tua"
    def hasil(self):
        print("nama : ",self.nama)
        print("nim : ",self.npm)
        print("Sekarang : ",self.semester,"\n")

m1 = Mahasiswa("180441100075","zein")
m1.perkiraan_semester()
m1.hasil()

m2=Mahasiswa("160441100075","tama")
m2.perkiraan_semester()
m2.hasil()

m3=Mahasiswa("180441100065","galih")
m3.perkiraan_semester()
m3.hasil()


# In[3]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class mahasiswa:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th

    def perkenalan_saya(self):
        print("hello,saya", self.nama,"Nim",self.nim,"lahir_di",self.tempat_lahir,self.tanggal_lahir,self.bulan_lahir,self.tahun_lahir)
    def umur_sekarang(self):
        print("preiksi_Umur :",tahun - self.tahun_lahir)
    def prediksi_umur(self):
        print("umur_saya :",tahun - self.tahun_lahir,"tahun",bulan - self.bulan_lahir,"bulan",hari - self.tanggal_lahir,"hari")
mhs1 = mahasiswa("zein","180441100075","pamekasan",8,6,2000)
mhs1.perkenalan_saya()
mhs1.umur_sekarang()
mhs1.prediksi_umur()


# In[4]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class orang:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th

    def perkenalkan_anda(self):
        print("hello,saya", self.nama,"Nim",self.nim,"lahir_di",self.tempat_lahir,self.tanggal_lahir,self.bulan_lahir,self.tahun_lahir)
    def umur_sekarang(self):
        print("preiksi_Umur :",tahun - self.tahun_lahir)
    def prediksi_umur(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

org1 = orang("zein","180441100075","pamekasan",8,6,2000)
org1.perkenalkan_anda()
org1.umur_sekarang()
org1.prediksi_umur()


# In[5]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class pegawai:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th
    def user(self):
        print("nama",self.nama,"nim",self.nim)
    def prediksi_umur(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

pg1 = pegawai("zein","180441100075","pamekasan",8,6,2000)
pg1.user()
pg1.prediksi_umur()


# In[6]:


class shark():
    def swim(self):
        print("the shark is swim")
    def swim_backwards(self):
        print("the shark cannot swim backwars,but can sink backward")
    def skalaton(self):
        print("the shark skelaton is mode of cartilago")

class clamfish():
    def swim(self):
        print("the clam fish is swim")
    def swim_backwards(self):
        print("the clamfish can swim backwars,but can sink backward")
    def skalaton(self):
        print("the clamfish skelaton is mode of bone")
abc=shark()
abc.skalaton()

easy=clamfish()
easy.skalaton()

for fish in(abc,easy):
    fish.swim()
    fish.swim_backwards()
    fish.skalaton()


# In[7]:


class shark():
    def swim(self):
        print("the shark is swim")
    def swim_backwards(self):
        print("the shark cannot swim backwars,but can sink backward")
    def skalaton(self):
        print("the shark skelaton is mode of cartilago")

class clamfish():
    def swim(self):
        print("the clam fish is swim")
    def swim_backwards(self):
        print("the clamfish can swim backwars,but can sink backward")
    def skalaton(self):
        print("the clamfish skelaton is mode of bone")
abc=shark()
abc.skalaton()

easy=clamfish()
easy.skalaton()


# In[8]:


class user:
    def __init__(self,n):
        self._first_name=n
    def p(self):
        print ("hello",self._first_name)
class programer(user):
    def __init__(self,n,last):
        user.__init__(self,n)
        self.last_name=last
    def P(self):
        print ("hello",self._first_name+" "+self.last_name)
brian=programer("zein","baim")
brian.P()


# In[9]:


class binatanng:
    def __init__(self,nama):
        self.nama=nama
    def cara_berjalan(self):
        raise  NotImplementedError("sub class must implemented abstrak metho")
class kucing(binatanng):
    def cara_berjalan(self):
        return "berjalan merangkak"
    def bersuara(self):
        return "meong"
class anjing (binatanng):
    def cara_berjalan(self):
        return "berjalan merangkak"
    def bersuara(self):
        return  "gog"
class ular (binatanng):
    def cara_berjalan(self):
        return "merayap"
    def bersuara(self):
        return "essst"
binatanng=[anjing('bull'),
           kucing('anggora'),
           ular('cobra')]
for binatanng in binatanng:
    print(binatanng.nama,":",binatanng.bersuara(),":",binatanng.cara_berjalan())


# In[ ]:




