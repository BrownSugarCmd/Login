from tkinter import*
import tkinter as tk
from tkinter import messagebox as mbox
from tkinter import ttk

katalog_plastik=[
    ["Gelas Plastik Bening", "Gelas Plastik Warna", "Gelas Plastik Warna", "Gelas Plastik Warna", "Gelas Plastik Warna", "Botol Plastik", "PET Kotor", "PET Warna Bersih/Pisah", "PET Warna Bersih/Pisah", "Plastik Campur", "Plastik Campur", "Plastik Campur", "Plastik Campur", "Tutup Botol", "Tutup Galon", "Plastik Daun", "Plastik Daun", "Refill, Sachet", "Refill, Sachet"],
    ["Aqua tanpa label", "Ale-ale", "Montea", "Teh gelas", "Tanpa label dan disusun", "Botol Ades tanpa penutup dan label", "Segala jenis PET yang masih ada label dan penutup", "PET tanpa penutup dan label", "Warna hijau atau biru", "Baskom", "Gelas", "Piring", "Tanpa damar", "Tutup botol campur", "Tutup galon warna campur", "Pembungkus bening campur", "Seperti plastik di nasi kotak", "Refill minyak goreng", "Pembungkus sachet"],
    [4000, 3500, 3500, 3500, 3500, 5000, 1000, 1800, 1800, 1800, 1800, 1800, 1800, 2500, 3500, 1000, 1000, 500, 500],
    ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18"]
    ]
katalog_logam=[
    ["Besi Tebal", "Besi Tebal", "Besi Tipis", "Besi Tipis", "Kaleng", "Kaleng", "Kaleng", "Kuningan", "Tembaga", "Aluminium Tebal", "Aluminium Tipis", "Aluminium Tipis", "Aluminium Tipis", "Aluminium Tipis", "Aluminium Siku", "Aluminium Campur", "Besi Seng", "Perunggu", "Perunggu"],
    ["Besi cor", "Besi plat", "Drum", "Rak piring", "Kaleng makanan", "Kaleng susu", "Tidak dipress", "Kuningan piala", "Tembaga dari kabel", "Box mesin motor", "Kaleng minuman", "Fanta", "Sprite", "Wajan", "Alma dekor", "Aluminium campur besi", "Seng bekas", "Kran air", "Kepala regulator"],
    [2800, 2800, 1800, 1800, 1400, 1400, 1400, 38000, 60000, 10000, 8000, 8000, 8000, 8000, 14000, 6000, 1000, 6000, 6000],
    ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17", "B18"]
    ]
katalog_kertas=[
    ["Kertas Putih", "Kertas Putih", "Kertas Campur/Warna", "Kertas Campur/Warna", "Kertas Buram", "Kardus(Dos)", "Kertas Semen", "Kertas Mikel", "Koran", "Karton Rak Telur", "Cones"],
    ["Buku tulis", "Kertas foto copy", "Majalah", "Karton warna", "Kertas kelabu/buram", "Karton coklat box", "Kertas semen tonasa", "Kertas pembungkus coklat", "Koran berita", "Rak untuk susun telur", "Kertas gulungan"],
    [2000, 2000, 500, 500, 1500, 1700, 1500, 1000, 1500, 400, 800],
    ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"]
    ]
katalog_kaca=[
    ["Botol Markisa Bensin", "Botol Kecap/Bir", "Botol Marjan", "Botol Soda", "Botol Bir Guinness"],
    ["Botol leher pendek bening", "Botol leher panjang tebal", "Botol tebal", "Botol tebal", "Botol tebal"],
    [1000, 7000, 6000, 5000, 6000],
    ["D0", "D1", "D2", "D3", "D4"]
    ]

riwayat=[
    [],
    [],
    [],
    [],
    []
]


class appsampah:
    def __init__(layar1,parent,title):
        layar1.parent = parent
        layar1.parent.title(title)
        layar1.parent.geometry("640x400")

        layar1.akun=(
            [],
            [],
            [],
            [])
        layar1.layerstate = (['login'])
        layar1.useraktif = StringVar()

        layar1.aturlayar()



    def aturlayar(layar1):
        layar1.guibackground = Frame(layar1.parent,bg="#ed892b")
        layar1.guibackground.pack(fill=BOTH, expand=YES,side =LEFT)
        if(layar1.layerstate[0] == "login"):
            layar1.loginpage()
        elif(layar1.layerstate[0] == "register"):
            layar1.registerpage()
        elif(layar1.layerstate[0] == "setor"):
            layar1.setorpage()
        elif(layar1.layerstate[0] == "katalog"):
            layar1.katalogpage()
        elif(layar1.layerstate[0] == "riwayat"):
            layar1.riwayatpage()
        else:
            layar1.mainpage()


    def refresh(layar1):
        print(layar1.layerstate)
        layar1.guibackground.destroy()
        layar1.aturlayar()

    def mainpage(layar1):
        layar1.parent.geometry("800x400")
        layar1.icon = PhotoImage(file='icon.png')
        layar1.iconstats=Label(layar1.guibackground, image=layar1.icon,bg='#ed892b')
        layar1.iconstats.pack()
        layar1.statusBar = Label(layar1.guibackground, height=2,
                                   text = "Aplikasi Setor Sampah",
                                   font = 'arial 15 bold',bd=2,bg='#ed892b')
        layar1.statusBar.pack()
        def keluar():
            keluar = mbox.askquestion('Notifikasi','Apakah anda yakin ingin keluar?')
            if (keluar == 'yes'):
                del layar1.layerstate[0]
                layar1.layerstate.insert(0,"login")
                layar1.refresh()
            else:
                quit
        def katalog():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,'katalog')
            layar1.refresh()
        def setor():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,'setor')
            layar1.refresh()
        def riwayat():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,'riwayat')
            layar1.refresh()
        layar1.menu = Label(layar1.guibackground, text="SILAHKAN PILIH MENU DIBAWAH INI",font='arial 10 bold', bd=2, bg='#ed892b')
        layar1.menu.pack()
        layar1.spasi = Label(layar1.guibackground, text = "", font ='arial 8 bold', bd=2,bg='#ed892b')
        layar1.spasi.pack()
        layar1.tombolsetor = Button(layar1.guibackground, text="Setor Sampah", width=20, command=setor)
        layar1.tombolsetor.pack()
        layar1.spasi = Label(layar1.guibackground, text = "", font ='arial 8 bold', bd=2,bg='#ed892b')
        layar1.spasi.pack()
        layar1.tombolkatalog = Button(layar1.guibackground, text='Katalog',width=20, command=katalog)
        layar1.tombolkatalog.pack()
        layar1.spasi = Label(layar1.guibackground, text = "", font ='arial 8 bold', bd=2,bg='#ed892b')
        layar1.spasi.pack()
        layar1.tombolriwayat = Button(layar1.guibackground, text='Riwayat',width =20,command=riwayat)
        layar1.tombolriwayat.pack()
        layar1.spasi = Label(layar1.guibackground, text = "", font ='arial 8 bold', bd=2,bg='#ed892b')
        layar1.spasi.pack()
        layar1.tombolkeluar = Button(layar1.guibackground, text='Keluar', width=20, command=keluar)
        layar1.tombolkeluar.pack()

    def setorpage(layar1):
        def tampil():
            layar1.totalharga = 0
            x = layar1.listsetor.get_children()
            for item in x:
                layar1.listsetor.delete(item)
            for i in range (len(pembayaran[0])):
                layar1.listsetor.insert("",'end',values=(pembayaran[0][i],pembayaran[1][i],pembayaran[2][i], pembayaran[3][i], (int(pembayaran[2][i])*pembayaran[3][i])))
                layar1.totalharga = (layar1.totalharga + (int(pembayaran[2][i])*pembayaran[3][i]))

            layar1.displaytotal = Label(layar1.guibackground, text="Total Harga :"+str(layar1.totalharga), bd=2, bg='#ed892b')
            layar1.displaytotal.place(x=850, y=400)
            layar1.tombolbayar = Button(layar1.guibackground, text="Bayar", bg='#0d0c04', fg='white', bd=2, width=15,command=bayar)
            layar1.tombolbayar.place(x=700, y=400)

        def bayar():
            ind = layar1.akun[0].index(layar1.useraktif)

            for i in range(len(pembayaran[0])):
                riwayat[0].append(pembayaran[1][i])
                riwayat[1].append(pembayaran[2][i])
                riwayat[2].append(int(pembayaran[2][i])*pembayaran[3][i])
                riwayat[3].append(layar1.akun[2][ind])
                riwayat[4].append(layar1.akun[3][ind])

            del layar1.layerstate[0]
            layar1.layerstate.insert(0, 'setor')
            layar1.refresh()
            mbox.showinfo('Notifikasi','Data telah ditambahkan')



        def tambah():
            if(layar1.sampahcode.get() in katalog_plastik[3]):
                index = katalog_plastik[3].index(layar1.sampahcode.get())
                pembayaran[0].append(katalog_plastik[3][index])
                pembayaran[1].append(katalog_plastik[1][index])
                pembayaran[2].append(layar1.sampahberat.get())
                pembayaran[3].append(katalog_plastik[2][index])
            elif(layar1.sampahcode.get() in katalog_kertas[3] ):
                index = katalog_kertas[3].index(layar1.sampahcode.get())
                pembayaran[0].append(katalog_kertas[3][index])
                pembayaran[1].append(katalog_kertas[1][index])
                pembayaran[2].append(layar1.sampahberat.get())
                pembayaran[3].append(katalog_kertas[2][index])
            elif(layar1.sampahcode.get() in katalog_logam[3] ):
                index = katalog_logam[3].index(layar1.sampahcode.get())
                pembayaran[0].append(katalog_logam[3][index])
                pembayaran[1].append(katalog_logam[1][index])
                pembayaran[2].append(layar1.sampahberat.get())
                pembayaran[3].append(katalog_logam[2][index])
            elif(layar1.sampahcode.get() in katalog_kaca[3] ):
                index = katalog_kaca[3].index(layar1.sampahcode.get())
                pembayaran[0].append(katalog_kaca[3][index])
                pembayaran[1].append(katalog_kaca[1][index])
                pembayaran[2].append(layar1.sampahberat.get())
                pembayaran[3].append(katalog_kaca[2][index])

            else:
                mbox.showinfo('Notifikasi','Kode Sampah tidak ditemukan')
            layar1.boxsampah.delete(0,END)
            layar1.boxberat.delete(0,END)
            tampil()
        def hapus():
            index = pembayaran[0].index(layar1.sampahcode.get())
            del pembayaran[0][index]
            del pembayaran[1][index]
            del pembayaran[2][index]
            del pembayaran[3][index]
            tampil()
            layar1.boxsampah.delete(0,END)
            layar1.boxberat.delete(0,END)
            layar1.tombolhapus.destroy()
        def selectitem(event):
            layar1.boxsampah.delete(0,END)
            layar1.boxberat.delete(0,END)
            index = layar1.listsetor.focus()
            ind = layar1.listsetor.item(index)
            frompembayaran = pembayaran[0].index(ind['values'][0])
            layar1.boxsampah.insert(END, pembayaran[0][frompembayaran])
            layar1.boxberat.insert(END, pembayaran[2][frompembayaran])

            layar1.tombolhapus = Button(layar1.guibackground, width=15, bg='#0d0c04', fg='white', text="Hapus", command=hapus)
            layar1.tombolhapus.place(x=240 , y=90)

        layar1.parent.geometry("1040x450")
        pembayaran = [[],[],[],[]]
        layar1.kodesampah = Label(layar1.guibackground, text="Kode Sampah", bd=2, bg='#ed892b')
        layar1.kodesampah.place(x=20, y=30)
        layar1.sampahcode = StringVar()
        layar1.boxsampah = Entry(layar1.guibackground, textvariable=layar1.sampahcode, width=30)
        layar1.boxsampah.place(x=120, y=30)
        layar1.sampahberat = StringVar()
        layar1.beratsampah = Label(layar1.guibackground, text="Berat Sampah(kg)", bd=2, bg='#ed892b')
        layar1.beratsampah.place(x=20, y=60)

        layar1.boxberat = Entry(layar1.guibackground,textvariable=layar1.sampahberat, width=30)
        layar1.boxberat.place(x=120, y=60)

        layar1.tomboltambah = Button(layar1.guibackground, text="Tambah", width =15,  bg='#0d0c04',fg='white', command=tambah)
        layar1.tomboltambah.place(x=120, y=90)

        cols = ['Kode Sampah','Sampah','Berat(kg)','Harga','Total Harga']
        layar1.listsetor = ttk.Treeview(layar1.guibackground, columns = cols,show='headings')
        scrollbar = ttk.Scrollbar(orient='vertical',command=layar1.listsetor.yview)
        layar1.listsetor.configure(yscrollcommand=scrollbar.set)
        for col in cols:
            layar1.listsetor.heading(col, text=col)
        layar1.listsetor.bind("<<TreeviewSelect>>",selectitem,"+")
        layar1.listsetor.place(x=20, y=140)

        def kembali():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,'dashboard')
            layar1.refresh()

        tombolback = Button(layar1.guibackground, text='Kembali', width=15, bg='#0d0c04', fg='white',command=kembali)
        tombolback.place(x=20, y=400)

    def riwayatpage(layar1):
        layar1.parent.geometry("1040x300")
        layar1.judul = Label(layar1.guibackground, text="Riwayat Penyetoran Sampah",bg='#ed892b',font='arial 15 bold')
        layar1.judul.pack()
        cols = ['Item','Berat(kg)','Total Harga','Alamat','No telpon']
        layar1.listriwayat = ttk.Treeview(layar1.guibackground, columns=cols,show="headings")
        scrollbar = ttk.Scrollbar(orient='vertical',command=layar1.listriwayat.yview)
        layar1.listriwayat.configure(yscrollcommand=scrollbar.set)
        for col in cols:
            layar1.listriwayat.heading(col, text=col)

        for i in range(len(riwayat[0])):
            layar1.listriwayat.insert("", "end", values=(riwayat[0][i],riwayat[1][i], riwayat[2][i], riwayat[3][i],riwayat[4][i]))
        layar1.listriwayat.pack()

        def kembali():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,'dashboard')
            layar1.refresh()

        layar1.tombolback = Button(layar1.guibackground, text="Kembali",width=15, bg='#0d0c04', fg='white', command=kembali)
        layar1.tombolback.place(x=20, y=270)

    def katalogpage(layar1):
        layar1.parent.geometry("820x330")
        layar1.statusBar = Label(layar1.guibackground, height=2, text="Data Sampah",font='arial 14 bold',bd=2, bg='#ed892b')
        layar1.statusBar.pack()
        cols = ['Kode Sampah','Sampah','Jenis Sampah','Harga Sampah']
        layar1.listbox = ttk.Treeview(layar1.guibackground, columns = cols, show='headings')
        scrollbar = ttk.Scrollbar(orient='vertical',command=layar1.listbox.yview)
        layar1.listbox.configure(yscrollcommand=scrollbar.set)
        for col in cols:
            layar1.listbox.heading(col, text=col)
        layar1.listbox.pack()
        for i in range (len(katalog_plastik[0])):
            layar1.listbox.insert("","end",values = (katalog_plastik[3][i], katalog_plastik[1][i], katalog_plastik[0][i],katalog_plastik[2][i]))
        for i in range (len(katalog_logam[0])):
            layar1.listbox.insert("","end",values = (katalog_logam[3][i], katalog_logam[1][i], katalog_logam[0][i],katalog_logam[2][i]))
        for i in range (len(katalog_kertas[0])):
            layar1.listbox.insert("","end",values = (katalog_kertas[3][i], katalog_kertas[1][i], katalog_kertas[0][i],katalog_kertas[2][i]))
        for i in range (len(katalog_kaca[0])):
            layar1.listbox.insert("","end",values = (katalog_kaca[3][i], katalog_kaca[1][i], katalog_kaca[0][i],katalog_kaca[2][i]))

        def kembali():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,'mainpage')
            layar1.refresh()

        layar1.tombolkembali = Button(layar1.guibackground, text='Kembali', width =15,  bg='#0d0c04',fg='white',command=kembali)
        layar1.tombolkembali.place(x=20, y=300)

    def loginpage(layar1):
        layar1.parent.geometry("640x400")
        layar1.icon = PhotoImage(file='icon.png')
        layar1.iconstats=Label(layar1.guibackground, image=layar1.icon,bg='#ed892b')
        layar1.iconstats.pack()
        layar1.statusBar = Label(layar1.guibackground, height=2,
                                       text = "Aplikasi Setor Sampah",
                                       font = 'arial 15 bold',bd=2,bg='#ed892b')
        layar1.statusBar.pack()

        layar1.username = Label(layar1.guibackground, text="Username",font='arial 12 bold', bd=2, bg='#ed892b')
        layar1.username.pack()
        layar1.masukkan_username = StringVar()
        layar1.boxusername = Entry(layar1.guibackground, textvariable = layar1.masukkan_username, width=30)
        layar1.boxusername.pack()

        layar1.password = Label(layar1.guibackground, text = "Password", font ='arial 12 bold', bd=2,bg='#ed892b')
        layar1.password.pack()
        layar1.masukkan_password = StringVar()
        layar1.boxpassword = Entry(layar1.guibackground, textvariable = layar1.masukkan_password,show='*' ,width =30)
        layar1.boxpassword.pack()

        layar1.spasi = Label(layar1.guibackground, text = "", font ='arial 8 bold', bd=2,bg='#ed892b')
        layar1.spasi.pack()

        def regist():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,"register")
            layar1.refresh()

        def loginaction():
            if(layar1.masukkan_username.get() in layar1.akun[0] and layar1.masukkan_password.get() in layar1.akun[1]):
                del layar1.layerstate[0]
                layar1.layerstate.insert(0,"dashboard")
                layar1.useraktif = layar1.masukkan_username.get()
                layar1.refresh()
            else:
                mbox.showinfo('Information','Username atau Password anda salah!')

        layar1.tombologin = Button(layar1.guibackground, relief=RAISED, text='LOGIN', width=30, bg='#0d0c04',fg='white',command=loginaction)
        layar1.tombologin.pack()

        layar1.spasi = Label(layar1.guibackground, text = "", font ='arial 8 bold', bd=2,bg='#ed892b')
        layar1.spasi.pack()

        layar1.tombolregister = Button(layar1.guibackground, relief = RAISED, text='REGISTER' , width = 30, bg='#0d0c04',fg='white', command=regist)
        layar1.tombolregister.pack()

    def registerpage(layar1):
        layar1.parent.geometry("300x300")
        layar1.judul = Label(layar1.guibackground, text="Form Registrasi", font='arial 20 bold', bg='#ed892b')
        layar1.judul.pack()

        layar1.username = Label(layar1.guibackground, text='Username', font='arial 12 bold',bg='#ed892b')
        layar1.username.place(x=10,y = 78)

        layar1.isiUser = StringVar()
        layar1.boxusername = Entry(layar1.guibackground, textvariable=layar1.isiUser, width=20)
        layar1.boxusername.place(x=120, y=80)

        layar1.password = Label(layar1.guibackground, text='Password', font='arial 12 bold',bg='#ed892b')
        layar1.password.place(x=10,y = 108)

        layar1.isiPassword = StringVar()
        layar1.boxpassword = Entry(layar1.guibackground, textvariable=layar1.isiPassword, show='*', width=20)
        layar1.boxpassword.place(x=120, y=110)

        layar1.alamat = Label(layar1.guibackground, text='Alamat', font='arial 12 bold',bg='#ed892b')
        layar1.alamat.place(x=10,y = 138)

        layar1.alamat = StringVar()
        layar1.boxalamat = Entry(layar1.guibackground, textvariable=layar1.alamat, width=20)
        layar1.boxalamat.place(x=120, y=140)

        layar1.notelpon = Label(layar1.guibackground, text='No Hp', font='arial 12 bold',bg='#ed892b')
        layar1.notelpon.place(x=10,y = 168)

        layar1.nomor = StringVar()
        layar1.boxnotelpon = Entry(layar1.guibackground, textvariable=layar1.nomor, width=20)
        layar1.boxnotelpon.place(x=120, y=170)

        def tambah():
            layar1.akun[0].append(layar1.isiUser.get())
            layar1.akun[1].append(layar1.isiPassword.get())
            layar1.akun[2].append(layar1.alamat.get())
            layar1.akun[3].append(layar1.nomor.get())
            mbox.showinfo("Notifikasi","Buat Akun Berhasil")
            layar1.boxusername.delete(0, END)
            layar1.boxpassword.delete(0,END)
            layar1.boxalamat.delete(0,END)
            layar1.boxnotelpon.delete(0,END)

        def keluar():
            del layar1.layerstate[0]
            layar1.layerstate.insert(0,"login")
            layar1.refresh()


        layar1.buttonregister = Button(layar1.guibackground, text="Register" , width =15,  bg='#0d0c04',fg='white', command=tambah)
        layar1.buttonregister.place(x=120, y=200)

        layar1.buttonback = Button(layar1.guibackground, text="Kembali" , width =15,  bg='#0d0c04',fg='white', command = keluar)
        layar1.buttonback.place(x=120, y=230)

root = Tk()
aplikasi = appsampah(root,"Aplikasi Setor Sampah")

root.mainloop()
