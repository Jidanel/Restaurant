from tkinter import *
from PIL import ImageTk, Image #gerer le contenaire d'affichage de limage: imagetk ainsi que l'image
from tkinter import messagebox, ttk
import os #pour gerer l'impression
import math, random  

class restaurant:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Jodysoft")
        self.root.resizable(False,False)
        self.root.geometry("1366x768+0+0")

        title= Label(self.root, bg="blue",fg="white", relief=RAISED, text="RESTAURANT JIDANEL", bd=4, font=("Times New Roman",14,"bold" ))
        title.place(x=0, y=0, width=1366)

        '''self.logo= ImageTk.PhotoImage(Image.open("C:/Users/Jidanel/AppData/Local/Programs/Python/Python311/Projects/Restaurant/images/Logo justlike.jpg"))
        self.logoposition = Label(image=self.logo)
        self.logoposition.place(x=60,y=0) #pour placer un logo '''

        #variables
       
        self.nomclient = StringVar()
        self.phoneclient = IntVar()
        self.recherche_fact= StringVar()
        self.qtepain=IntVar()
        self.qteomelette=IntVar()
        self.cuilmayo=IntVar()
        self.cuilbeurre=IntVar()
        self.demibtesardine=IntVar()
        self.tasselait=IntVar()
        self.platsalade=IntVar()
        self.jambon=IntVar()
        self.okok=IntVar()
        self.eru=IntVar()
        self.tripes=IntVar()
        self.ndole=IntVar()
        self.fritespommes=IntVar()
        self.fritesplantmur=IntVar()
        self.waterfufu=IntVar()
        self.batonsmanioc=IntVar()
        self.jus=IntVar()
        self.l33=IntVar()
        self.kadji=IntVar()
        self.magnan=IntVar()
        self.mutzig=IntVar()
        self.origin=IntVar()
        self.dopel=IntVar()
        self.beaufortlite=IntVar()
        self.totalpdej=StringVar()
        self.totaldej=StringVar()
        self.totalboisson=StringVar()
        self.taxe=StringVar()
        self.tht=StringVar()
        self.ttcpdej=StringVar()
        self.tttcdej=StringVar()
        self.tttcboisson=StringVar()
        self.ttc=StringVar()
        self.taxes=0.1925


        
        #Frame principal
        Main_Frame= LabelFrame(self.root, bd=5, bg="lightgreen", relief=GROOVE)
        Main_Frame.place(x=0,y=40, width=1366, height=710 )
        
        #Categorie client
        Client_frame = LabelFrame(Main_Frame, bd=5, text="Client", font=("Algerian", 12, "bold"), bg ="silver", fg="black")
        Client_frame.place(x=0, y=3, width=1360, height=70)
        self.lblclient=Label(Client_frame, fg="black", font=("Times new roman",12), text="Nom du client :",width=10, bg="silver")
        self.lblclient.grid(row=0, columnspan=2)

        self.txtclient= Entry(Client_frame,textvariable=self.nomclient, relief=SUNKEN, width=25, foreground="black", font=("Times new roman",12))
        self.txtclient.grid(row=0,column=2,columnspan=2)
        

        self.lblphone = Label(Client_frame, bd=5, font=("Times new roman", 12), fg="black", width=20, text="Numéro de Telephone :", bg="silver")
        self.lblphone.grid(row=0, column=5, columnspan=2)

        self.txtphone = Entry(Client_frame, width=25, textvariable=self.phoneclient, relief=SUNKEN, foreground="black", font=("Times new roman",12))
        self.txtphone.grid(row=0,column=7, columnspan=2)
        

        self.lblrecherche = Label(Client_frame, bg="silver", text="Numéro de Facture :", width=20, font=("Times new roman",12), fg="black")
        self.lblrecherche.grid(row=0, column=9, columnspan=3)

        self.txtrecherche = Entry(Client_frame, textvariable=self.recherche_fact, width=30, background="white", relief=SUNKEN, foreground="black", font=("Times new roman",12))
        self.txtrecherche.grid(row=0, column=12, columnspan=5)

        self.lblespace = Label(Client_frame, bg="silver", width=10)
        self.lblespace.grid(row=0, column=17)

        self.btnrecherhe = Button(Client_frame, text="Rechercher", font=("Times new roman",12), command="", width=20 , height=1, cursor="hand2", bg= "silver", fg="black" )
        self.btnrecherhe.grid(row=0, column=18, columnspan=2)

        #Rubrique petit dejeuner
        Petit_dej_frame=LabelFrame(Main_Frame, bg="silver", bd=2, text="Petit Dejeuner",fg="black", font=("Algerian",12,"bold"))
        Petit_dej_frame.place(x=0, y=75, width=320, height=429)

        #plats
        #Pains

        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=0, column=0)
        self.lblpain = Label(Petit_dej_frame, text="Nombres de pain(s) :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblpain.grid(row=1, column=0, sticky=W)
        self.txtpain = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.qtepain, width= 8, font=("Arial",12))
        self.txtpain.grid(row=1, column=1, sticky=W)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=2, column=0)

        #Omelettes

        self.lblomelette = Label(Petit_dej_frame, text="Nombre d'omellettes :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblomelette.grid(row=3, column=0, sticky=W)
        self.txtomelette = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.qteomelette, width= 8, font=("Arial",12))
        self.txtomelette.grid(row=3, column=1)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=4, column=0)

        #Cuillères de mayonnaise

        self.lblmayonnaise = Label(Petit_dej_frame, text="Cuillères de mayonnaise :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblmayonnaise.grid(row=5, column=0, sticky=W)
        self.txtmayonnaise = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.cuilmayo, width= 8, font=("Arial",12))
        self.txtmayonnaise.grid(row=5, column=1)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=6, column=0)

        #Cuillères de beurres
        
        self.lblbeurre = Label(Petit_dej_frame, text="Cuillères de beurre :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblbeurre.grid(row=7, column=0, sticky=W)
        self.txtbeurre = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.cuilbeurre, width= 8, font=("Arial",12))
        self.txtbeurre.grid(row=7, column=1)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=8, column=0)

        #Boites de sardines

        self.lbldbtesardine = Label(Petit_dej_frame, text="Demi boite de sardine :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbldbtesardine.grid(row=9, column=0, sticky=W)
        self.txtdbtesardine = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.demibtesardine, width= 8, font=("Arial",12))
        self.txtdbtesardine.grid(row=9, column=1)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=10, column=0)

        #Tasses de lait

        self.lbltassedelait = Label(Petit_dej_frame, text="Tasses de lait :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbltassedelait.grid(row=11, column=0, sticky=W)
        self.txttassedelait = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.tasselait, width= 8, font=("Arial",12))
        self.txttassedelait.grid(row=11, column=1)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=12, column=0)

        #Plats de salade

        self.lblplatssalade = Label(Petit_dej_frame, text="Plats de salade :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblplatssalade.grid(row=13, column=0, sticky=W)
        self.txtplatssalade = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.platsalade, width= 8, font=("Arial",12))
        self.txtplatssalade.grid(row=13, column=1)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=14, column=0)

        #Jambons

        self.lbljambon = Label(Petit_dej_frame, text="Tranches de jambon :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbljambon.grid(row=15, column=0, sticky=W)
        self.txtjambon = Entry(Petit_dej_frame, relief=SUNKEN , bd=5,  textvariable=self.jambon, width= 8, font=("Arial",12))
        self.txtjambon.grid(row=15, column=1)
        self.lblespace = Label(Petit_dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=16, column=0)

        #Rubrique dejeuner
        dej_frame= LabelFrame(Main_Frame, bd=2, fg= "black", bg="silver", text="Dejeuner", font=("Algerian", 12,"bold"))
        dej_frame.place(x=330,y=75, width=320, height=429)

        #plats
        #Okok

        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=0, column=0)
        self.lblokok = Label(dej_frame, text="Plats d'Okok :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblokok.grid(row=1, column=0, sticky=W)
        self.txtokok = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.okok, width= 8, font=("Arial",12))
        self.txtokok.grid(row=1, column=1, sticky=W)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=2, column=0)

        #eru

        self.lbleru = Label(dej_frame, text="Plats de Eru :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbleru.grid(row=3, column=0, sticky=W)
        self.txteru = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.eru, width= 8, font=("Arial",12))
        self.txteru.grid(row=3, column=1)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=4, column=0)

        #tripes

        self.lbltripes = Label(dej_frame, text="Plats de tripes :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbltripes.grid(row=5, column=0, sticky=W)
        self.txttripes = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.tripes, width= 8, font=("Arial",12))
        self.txttripes.grid(row=5, column=1)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=6, column=0)

        #ndolè
        
        self.lblndole = Label(dej_frame, text="Plats de ndole :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblndole.grid(row=7, column=0, sticky=W)
        self.txtndole = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.ndole, width= 8, font=("Arial",12))
        self.txtndole.grid(row=7, column=1)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=8, column=0)

        #BFrites de pommes

        self.lblfritespommes = Label(dej_frame, text="Frites de pommes :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblfritespommes.grid(row=9, column=0, sticky=W)
        self.txtfritespommes = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.fritespommes, width= 8, font=("Arial",12))
        self.txtfritespommes.grid(row=9, column=1)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=10, column=0)

        #TFrites de plantain mur

        self.lblfrptm = Label(dej_frame, text="Plantain mur frits :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblfrptm.grid(row=11, column=0, sticky=W)
        self.txtfrptm = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.fritesplantmur, width= 8, font=("Arial",12))
        self.txtfrptm.grid(row=11, column=1)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=12, column=0)

        #waterfufu

        self.lblwaterfufu = Label(dej_frame, text="Boules de Waterfufu :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblwaterfufu.grid(row=13, column=0, sticky=W)
        self.txtwaterfufu = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.waterfufu, width= 8, font=("Arial",12))
        self.txtwaterfufu.grid(row=13, column=1)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=14, column=0)

        #Batons de manioc

        self.lblbaton = Label(dej_frame, text="Batons de manioc :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblbaton.grid(row=15, column=0, sticky=W)
        self.txtbaton = Entry(dej_frame, relief=SUNKEN , bd=5,  textvariable=self.batonsmanioc, width= 8, font=("Arial",12))
        self.txtbaton.grid(row=15, column=1)
        self.lblespace = Label(dej_frame, bg="silver", width=30)
        self.lblespace.grid(row=16, column=0)


        #Rubrique boisson
        boisson_frame = LabelFrame(Main_Frame, text="Boissons", font=("Algerian", 12, "bold"), fg="black", bg="silver", bd=2)
        boisson_frame.place(x=660,y=75,width=320, height=429)

        #boissons
        #Jus brasseries

        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=0, column=0)
        self.lbljus = Label(boisson_frame, text="Jus de brasserie :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbljus.grid(row=1, column=0, sticky=W)
        self.txtjus = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.jus, width= 8, font=("Arial",12))
        self.txtjus.grid(row=1, column=1, sticky=W)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=2, column=0)

        #33 export

        self.lbll33 = Label(boisson_frame, text="33 Export :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbll33.grid(row=3, column=0, sticky=W)
        self.txtl33 = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.l33, width= 8, font=("Arial",12))
        self.txtl33.grid(row=3, column=1)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=4, column=0)

        #Kadji

        self.lblkadji = Label(boisson_frame, text="Kadji Beer :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblkadji.grid(row=5, column=0, sticky=W)
        self.txtkadji = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.kadji, width= 8, font=("Arial",12))
        self.txtkadji.grid(row=5, column=1)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=6, column=0)

        #magnan
        
        self.lblmagnan = Label(boisson_frame, text="Magnan :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblmagnan.grid(row=7, column=0, sticky=W)
        self.txtnmagnan = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.magnan, width= 8, font=("Arial",12))
        self.txtnmagnan.grid(row=7, column=1)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=8, column=0)

        #Mutzig

        self.lblmutzig = Label(boisson_frame, text="Mutzig :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblmutzig.grid(row=9, column=0, sticky=W)
        self.txtmutzig = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.mutzig, width= 8, font=("Arial",12))
        self.txtmutzig.grid(row=9, column=1)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=10, column=0)

        #Origin

        self.lblorigin = Label(boisson_frame, text="Origin :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblorigin.grid(row=11, column=0, sticky=W)
        self.txtorigin = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.origin, width= 8, font=("Arial",12))
        self.txtorigin.grid(row=11, column=1)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=12, column=0)

        #Dopel

        self.lbldopel = Label(boisson_frame, text="Dopel :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lbldopel.grid(row=13, column=0, sticky=W)
        self.txtdopel = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.dopel, width= 8, font=("Arial",12))
        self.txtdopel.grid(row=13, column=1)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=14, column=0)

        #Beaufort lite

        self.lblbeauflite = Label(boisson_frame, text="Beaufort Lite :", width=20, font=("Times new roman", 11), bg="silver", fg="black" )
        self.lblbeauflite.grid(row=15, column=0, sticky=W)
        self.txtbeauflite = Entry(boisson_frame, relief=SUNKEN , bd=5,  textvariable=self.beaufortlite, width= 8, font=("Arial",12))
        self.txtbeauflite.grid(row=15, column=1)
        self.lblespace = Label(boisson_frame, bg="silver", width=30)
        self.lblespace.grid(row=16, column=0)


        #Zone d'affichage de la facture
        facture_frame=LabelFrame(Main_Frame, bd=3, fg="black", bg="white")
        facture_frame.place(x=990,y=75, width=360, height=500)
        scroll_y=Scrollbar(facture_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.txtarea= Text(facture_frame,font=("Times new roman", 12),bd=5, bg="white", fg="black",yscrollcommand= scroll_y.set)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)



        titre_fact= Label(facture_frame, font=("Arial black",14,"bold"), bd=5, relief=GROOVE, text="FACTURATION")
        titre_fact.place(x=0,y=0, width=360)

        #Menu du bas de page
        bas_frame=LabelFrame(Main_Frame, text="Menu", font=("Algerian",12,"bold"),bd=5, bg="silver", fg="black")
        bas_frame.place(x=0,y=505, width=980, height=255)

        #THT
        self.lblpdej = Label(bas_frame, bg = "silver", text="Prix du Petit Dejeuner HT :", font=("Times new roman",12), width=20,fg="black")
        self.lblpdej.grid(row=0, column=0, sticky=W)
        self.txtpdej= Entry(bas_frame, textvariable=self.totalpdej, font=("Times new roman",12), width= 20, state="readonly")
        self.txtpdej.grid(row=0, column=1, sticky=W)
        self.lblespace = Label(bas_frame, bg="silver", width=20)
        self.lblespace.grid(row=1, column=0)


        self.lbldej = Label(bas_frame, bg = "silver", text="Prix du Dejeuner HT :", font=("Times new roman",12), width=20,fg="black")
        self.lbldej.grid(row=2, column=0, sticky=W)
        self.txtdej= Entry(bas_frame, textvariable=self.totaldej, font=("Times new roman",12), width= 20, state="readonly")
        self.txtdej.grid(row=2, column=1, sticky=W)
        self.lblespace = Label(bas_frame, bg="silver", width=20)
        self.lblespace.grid(row=3, column=0)

        self.lblboisson = Label(bas_frame, bg = "silver", text="Prix de la boisson HT :", font=("Times new roman",12), width=20,fg="black")
        self.lblboisson.grid(row=4, column=0, sticky=W)
        self.txtboisson= Entry(bas_frame, textvariable=self.totalboisson, font=("Times new roman",12), width= 20, state="readonly")
        self.txtboisson.grid(row=4, column=1, sticky=W)
        self.lblespace = Label(bas_frame, bg="silver", width=10)
        self.lblespace.grid(row=5, column=0)
        
        self.lbltotalht = Label(bas_frame, bg = "silver", text="Total HT :", font=("Times new roman",12), width=20,fg="black")
        self.lbltotalht.grid(row=6, column=0, sticky=W)
        self.txttotalht= Entry(bas_frame, textvariable=self.tht, font=("Times new roman",12), width= 20, state="readonly")
        self.txttotalht.grid(row=6, column=1, sticky=W)

        #TTC
        self.lblttpdej = Label(bas_frame, bg = "silver", text="Prix du Petit Dejeuner TTC :", font=("Times new roman",12), width=20,fg="black")
        self.lblttpdej.grid(row=0, column=2, sticky=W)
        self.txtttpdej= Entry(bas_frame, textvariable=self.ttcpdej, font=("Times new roman",12), width= 20, state="readonly")
        self.txtttpdej.grid(row=0, column=3, sticky=W)
        self.lblespace = Label(bas_frame, bg="silver", width=20)
        self.lblespace.grid(row=1, column=2)


        self.lblttdej = Label(bas_frame, bg = "silver", text="Prix du Dejeuner TTC :", font=("Times new roman",12), width=20,fg="black")
        self.lblttdej.grid(row=2, column=2, sticky=W)
        self.txtttdej= Entry(bas_frame, textvariable=self.tttcdej, font=("Times new roman",12), width= 20, state="readonly")
        self.txtttdej.grid(row=2, column=3, sticky=W)
        self.lblespace = Label(bas_frame, bg="silver", width=20)
        self.lblespace.grid(row=3, column=2)

        self.lblttcboisson = Label(bas_frame, bg = "silver", text="Prix de la boisson TTC :", font=("Times new roman",12), width=20,fg="black")
        self.lblttcboisson.grid(row=4, column=2, sticky=W)
        self.txtttcboisson= Entry(bas_frame, textvariable=self.tttcboisson, font=("Times new roman",12), width= 20, state="readonly")
        self.txtttcboisson.grid(row=4, column=3, sticky=W)
        self.lblespace = Label(bas_frame, bg="silver", width=10)
        self.lblespace.grid(row=5, column=2)
        
        self.lbltotalttc = Label(bas_frame, bg = "silver", text="Total TTC :", font=("Times new roman",12), width=20,fg="black")
        self.lbltotalttc.grid(row=6, column=2, sticky=W)
        self.txttotalttc= Entry(bas_frame, textvariable=self.ttc, font=("Times new roman",12), width= 20, state="readonly")
        self.txttotalttc.grid(row=6, column=3, sticky=W)

        #TVA
        self.lbltva = Label(bas_frame, bg = "silver", text="Taxe sur la valeur ajoutee :", font=("Times new roman",12), width=20,fg="black")
        self.lbltva.grid(row=6, column=4, sticky=W)
        self.txttva= Entry(bas_frame, textvariable=self.taxe, font=("Times new roman",12), width= 8, state="readonly")
        self.txttva.grid(row=6, column=5, sticky=W)



        #Bouton totaux
        btn_frame= LabelFrame(Main_Frame,bd=2, fg="black", bg="white")
        btn_frame.place(x=990,y=585, width=375, height=175)

        btntotal= Button(btn_frame, cursor="hand2", text= "Total ", bd=5, bg="blue", fg="black", width=18, command=self.total, font=("Arial black",10),height=1)
        btntotal.grid(row=0, column=0, sticky=W)

        btnfacture= Button(btn_frame, cursor="hand2", text= "Facture ", bd=5, bg="green", fg="black", width=18, command=self.generer_facture, font=("Arial black",10),height=1)
        btnfacture.grid(row=0, column=1, sticky=W)

        self.lblespace = Label(btn_frame, bg="white", width=30)
        self.lblespace.grid(row=1, column=0)

        btnreinit= Button(btn_frame, cursor="hand2", text= "Reinitialiser ", bd=5, bg="silver", fg="black", width=18, command=self.reinitialiser, font=("Arial black",10),height=1)
        btnreinit.grid(row=2, column=0, sticky=W)

        btnquit= Button(btn_frame, cursor="hand2", text= "Quitter ", bd=5, bg="red", fg="black", width=18, command=self.quitter, font=("Arial black",10),height=1)
        btnquit.grid(row=2, column=1, sticky=W)

    def total(self):
        
        #Calcul des prix totaux en fonction des quantités
        self.ppain=self.qtepain.get()*150
        self.pomelette=self.qteomelette.get()*300
        self.pmayo=self.cuilmayo.get()*100
        self.pbeurre=self.cuilbeurre.get()*50
        self.pbtesardine=self.demibtesardine.get()*250
        self.ptasselait=self.tasselait.get()*250
        self.psalade=self.platsalade.get()*500
        self.pjambon=self.jambon.get()*100
        self.pokok=self.okok.get()*1000
        self.peru=self.eru.get()*1000
        self.ptripes=self.tripes.get()*1500
        self.pndole=self.ndole.get()*1000
        self.pfritespommes=self.fritespommes.get()*1000
        self.pfritespmur=self.fritesplantmur.get()*1000
        self.pwaterfufu=self.waterfufu.get()*500
        self.pbatonmanioc=self.batonsmanioc.get()*100
        self.pjus=self.jus.get()*500
        self.p33=self.l33.get()*650
        self.pkadji=self.kadji.get()*700
        self.pmagnan=self.magnan.get()*500
        self.pmutzig=self.mutzig.get()*650
        self.porigin=self.origin.get()*700
        self.pdopel=self.dopel.get()*700
        self.pbeaufort=self.beaufortlite.get()*650
        taxe=0.1925
        self.totalht=IntVar()

        #Calcul des prix HT 
        self.totalpetitdej=int(self.ppain+self.pomelette+self.pmayo+self.pbeurre+self.pbtesardine+self.ptasselait+self.psalade+self.pjambon)
        self.totalpdej.set(str(f"{self.totalpetitdej} Fcfa"))
        self.taxe.set(str(0.1925))

        self.total_dej=int(self.pokok+self.peru+self.ptripes+self.pndole+self.pfritespommes+self.pfritespmur+self.pwaterfufu+self.pbatonmanioc)
        self.totaldej.set(str(f"{self.total_dej} Fcfa"))

        self.totalbsson=int(self.pjus+self.p33+self.pkadji+self.pmagnan+self.pmutzig+self.porigin+self.pdopel+self.pbeaufort)
        self.totalboisson.set(str(f"{self.totalbsson} Fcfa"))

        self.totalht=int(self.totalbsson+self.total_dej+self.totalpetitdej)
        self.tht.set(str(f"{self.totalht} Fcfa"))

        #Calcul des prix TTC
        x= float(self.totalpetitdej*1.1925)
        self.ttcpetitdej=round(x,2)
        self.ttcpdej.set(str(f"{self.ttcpetitdej} Fcfa"))

        k= float(self.total_dej*1.1925)
        self.ttc_dej=round(k,2) #arrondi à 2 chiffres après la virgule
        self.tttcdej.set(str(f"{self.ttc_dej} Fcfa"))

        m= float(self.totalbsson*1.1925)
        self.ttcboisson=round(m,2)
        self.tttcboisson.set(str(f"{self.ttcboisson} Fcfa"))

        z=float(self.ttcboisson+self.ttcpetitdej+self.total_dej)
        self.pttc=round(z,2)
        self.ttc.set(str(f"{self.pttc} Fcfa"))
        if self.totalht==0 or self.nomclient.get()=="":
            messagebox.showerror("Erreur", "Choisissez au moins un plat ou une boisson ou saisissez le nom du client")
            self.totalpdej.set(str(""))
            self.taxe.set(str(""))

            self.totaldej.set(str(""))
            self.totalboisson.set(str(""))
            self.tht.set(str(""))
            self.ttcpdej.set(str(""))
            self.tttcdej.set(str(""))
            self.tttcboisson.set(str(""))
            self.ttc.set(str(""))

    def generer_facture(self):
            z =random.randint(10000000,999999999)
            self.numfacture = StringVar()
            self.numfacture.set(z)
            #On se rassure qu'un meme numero de facture n'apparait pas 2 fois
            self.listenumfact=[]
            self.listenumfact.append(self.numfacture.get())

                    
            self.txtarea.delete(1.0, END)
            self.txtarea.insert(END,"\n\n**BIENVENUE AU RESTAURANT JIDANEL**")
            self.txtarea.insert(END,"****************************************")
            self.txtarea.insert(END, f"\n Numero Facture : {self.numfacture.get()} ")
            self.txtarea.insert(END, f"\n Nom du Client : {self.nomclient.get()}" )
            self.txtarea.insert(END, f"\n Numero de téléphone : {self.phoneclient.get()}\n")
            self.txtarea.insert(END, "****************************************")
            self.txtarea.insert(END,"\n Produits \t\t Quantité \t\t Prix \n")
            self.txtarea.insert(END, "****************************************")

            #petit dejeuner
            if self.qtepain.get()!=0:
               self.txtarea.insert(END,f"\n Nombres de pains \t\t {self.qtepain.get()} \t\t {self.ppain} \n") 
            if self.qteomelette.get()!=0: 
               self.txtarea.insert(END,f"\n Nombres d'omelettes \t\t {self.qteomelette.get()} \t\t {self.pomelette} \n")
            if self.cuilmayo.get()!=0:  
               self.txtarea.insert(END,f"\n Cuillères de mayonnaise \t\t {self.cuilmayo.get()} \t\t {self.pmayo} \n")  
            if self.cuilbeurre.get()!=0:
               self.txtarea.insert(END,f"\n Cuillère de beurre  \t\t {self.cuilbeurre.get()} \t\t {self.pbeurre} \n") 
            if self.demibtesardine.get()!=0: 
               self.txtarea.insert(END,f"\n Tranches de sardines \t\t {self.demibtesardine.get()} \t\t {self.pbtesardine} \n")
            if self.tasselait.get()!=0:  
               self.txtarea.insert(END,f"\n Tasses de lait \t\t {self.tasselait.get()} \t\t {self.ptasselait} \n")
            if self.platsalade.get()!=0:  
               self.txtarea.insert(END,f"\n Plats de salades \t\t {self.platsalade.get()} \t\t {self.psalade} \n")  
            if self.jambon.get()!=0:
               self.txtarea.insert(END,f"\n Tranches de Jambons \t\t {self.jambon.get()} \t\t {self.pjambon} \n")  
             
            #Dejeuner
            if self.okok.get()!=0:
               self.txtarea.insert(END,f"\n Plats Okok \t\t {self.okok.get()} \t\t {self.pokok} \n") 
            if self.eru.get()!=0:
               self.txtarea.insert(END,f"\n Plats Eru \t\t {self.eru.get()} \t\t {self.peru} \n") 
            if self.tripes.get()!=0:
               self.txtarea.insert(END,f"\n Plats tripes \t\t {self.tripes.get()} \t\t {self.ptripes} \n") 
            if self.ndole.get()!=0:
               self.txtarea.insert(END,f"\n Plats ndole \t\t {self.ndole.get()} \t\t {self.pndole} \n") 
            if self.fritespommes.get()!=0:
               self.txtarea.insert(END,f"\n Frites de pommes \t\t {self.fritespommes.get()} \t\t {self.pfritespommes} \n") 
            if self.fritesplantmur.get()!=0:
               self.txtarea.insert(END,f"\n Plantain mur \t\t {self.fritesplantmur.get()} \t\t {self.pfritespmur} \n") 
            if self.waterfufu.get()!=0:
               self.txtarea.insert(END,f"\n Boules waterfufu \t\t {self.waterfufu.get()} \t\t {self.pwaterfufu} \n") 
            if self.batonsmanioc.get()!=0:
               self.txtarea.insert(END,f"\n Batons de manioc \t\t {self.batonsmanioc.get()} \t\t {self.pbatonmanioc} \n")
            #Boisson
            if self.jus.get()!=0:
               self.txtarea.insert(END,f"\n Jus de Brasserie \t\t {self.jus.get()} \t\t {self.pjus} \n")
            if self.l33.get()!=0:
               self.txtarea.insert(END,f"\n 33 Export \t\t {self.l33.get()} \t\t {self.p33} \n")
            if self.kadji.get()!=0:
               self.txtarea.insert(END,f"\n Kadji Beer \t\t {self.kadji.get()} \t\t {self.pkadji} \n")
            if self.magnan.get()!=0:
               self.txtarea.insert(END,f"\n Magnan \t\t {self.magnan.get()} \t\t {self.pmagnan} \n")
            if self.mutzig.get()!=0:
               self.txtarea.insert(END,f"\n Mutzig \t\t {self.mutzig.get()} \t\t {self.pmutzig} \n")
            if self.origin.get()!=0:
               self.txtarea.insert(END,f"\n Origin \t\t {self.origin.get()} \t\t {self.porigin} \n")
            if self.dopel.get()!=0:
               self.txtarea.insert(END,f"\n Dopel \t\t {self.dopel.get()} \t\t {self.pdopel} \n")
            if self.beaufortlite.get()!=0:
               self.txtarea.insert(END,f"\n Beaufort Lite \t\t {self.beaufortlite.get()} \t\t {self.pbeaufort} \n")

            self.txtarea.insert(END, "\n")
            self.txtarea.insert(END, "****************************************\n")
            if self.totalpetitdej!=0:
               self.txtarea.insert(END,f"Total Petit Dejeuner HT : \t {self.totalpetitdej} \n")   
            if self.total_dej!=0:
               self.txtarea.insert(END,f"Total Dejeuner HT : \t {self.total_dej} \n")
            if self.totalboisson!=0:
               self.txtarea.insert(END,f"Total Boisson HT : \t {self.totalbsson} \n")                
            self.txtarea.insert(END,f"Total HT : \t {self.totalht} \n")
            self.txtarea.insert(END,f"TVA : \t {self.taxes} \n")
            self.txtarea.insert(END,f"Total TTC : \t {self.pttc} \n")
            op=messagebox.askyesno("Sauvegarder","Voulez vous vraiment sauvegarder cette facture?")
            if op==True:
                self.donneefacture=self.txtarea.get(1.0,END)
                f1=open("C:/Users/Jidanel/AppData/Local/Programs/Python/Python311/Projects/Restaurant/factures/"+str(self.numfacture.get())+".txt","w") #On ouvre le dossier image et on enregistre un fichier txt en mode ecriture avec comme nom le numero de la facture
                f1.write(self.donneefacture)
                messagebox.showinfo("Sauvegarde",f"La facture n° {self.numfacture.get()} a été enregistrée avec succès")
                f1.close()
    
    def reinitialiser(self):
       k=messagebox.askyesno("Reinitialisation","Voulez vous reinitialiser la page ?")
       if k==True:
            self.nomclient.set("")
            self.phoneclient.set(0)
            self.txtarea.delete(1.0, END)
            self.txtarea.insert(END,"\n\n**BIENVENUE AU RESTAURANT JIDANEL**")
            self.txtarea.insert(END,"****************************************")
            self.txtarea.insert(END, f"\n Numero Facture : {self.numfacture.get()} ")
            self.txtarea.insert(END, f"\n Nom du Client : {self.nomclient.get()}" )
            self.txtarea.insert(END, f"\n Numero de téléphone : {self.phoneclient.get()}\n")
            self.txtarea.insert(END, "****************************************")
            self.txtarea.insert(END,"\n Produits \t\t Quantité \t\t Prix \n")
            self.txtarea.insert(END, "****************************************")
            self.nomclient.set("")
            self.phoneclient.set(0)
            self.qtepain.set(0)
            self.qteomelette.set(0)
            self.cuilbeurre.set(0)
            self.cuilmayo.set(0)
            self.demibtesardine.set(0)
            self.tasselait.set(0)
            self.platsalade.set(0)
            self.jambon.set(0)
            self.okok.set(0)
            self.eru.set(0)
            self.tripes.set(0)
            self.ndole.set(0)
            self.fritespommes.set(0)
            self.fritesplantmur.set(0)
            self.waterfufu.set(0)
            self.batonsmanioc.set(0)
            self.jus.set(0)
            self.l33.set(0)
            self.kadji.set(0)
            self.mutzig.set(0)
            self.magnan.set(0)
            self.origin.set(0)
            self.dopel.set(0)
            self.beaufortlite.set(0)
            self.totalpdej.set(str(""))
            self.taxe.set(str(""))

            self.totaldej.set(str(""))
            self.totalboisson.set(str(""))
            self.tht.set(str(""))
            self.ttcpdej.set(str(""))
            self.tttcdej.set(str(""))
            self.tttcboisson.set(str(""))
            self.ttc.set(str(""))

    def quitter(self):
       k=messagebox.askyesno("Quitter","Voulez vous fermer le fenetre ?")
       if k==True:
          root.destroy()

            


        




root=Tk() 
obj= restaurant(root)
root.mainloop()       