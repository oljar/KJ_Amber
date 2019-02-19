#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from tkinter import *
from tkinter import messagebox

# git
# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('plan.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()



# lista zagnieżdzona przekazywania stanow kontrolek
l=200     #parametry listy-ilosc zagniezdzen
x=200    #parametry listy- ilosc zmiennych(str) w zagniezdzeniu
State=[]
for s in range(l):
    sub_list=[""]
    for y in range(x):

        sub_list.append(int(y))

        State.append(sub_list)

n=-1  #zmienna odpow. za poruszanie po bazie






# Klasa okna glownego
class Application(Frame):
    """Aplikacja GUI , sekret długowiecznosci"""
    def __init__(self,master,State,n):
        """Inicjuję ramkę"""
        super(Application,self).__init__(master)
        self.grid()
        self.nr_fab(State)
        self.kod_prod(State)
        self.nr_zlec(State)
        self.identyfikacja(State)
        self.filtry_uszczelki(State)
        self.wymiennik_szczel_dokrec(State)
        self.prowadz_konc_przew(State)
        self.montaz_nag_wt(State)
        self.montaz_rozdz(State)
        self.dzial_wentyl(State)
        self.montaz_czujnikow(State)



        self.btn_akcept()

        self.n=n



########################################################################################################################################################################################

    # poziom lini nr fabryczny


    def nr_fab(self,State):
        """numer fabryczny"""

        # utworz etykiete z zapytniem o nr fabryczny
        self.lbl_dist_0=Label(self)
        self.lbl_dist_0.grid(row = 0, column = 0 , padx=6)                               #dystans col 0

        self.lbl_nr_fab = Label(self, text ="Podaj nr fabryczny")
        self.lbl_nr_fab.grid(row = 0, column = 1 , sticky = W )

        self.lbl_dist_2=Label(self)
        self.lbl_dist_2.grid(row = 0, column = 2 , padx=5)                               #dystans  col  2

        self.lbl_dist_3=Label(self)
        self.lbl_dist_3.grid(row = 0, column = 3 , padx=1)                               #dystans   col 3



        # utworz widzet Entry do przyjecia nr_fab

        var1=StringVar()    # zmienna pomocnicza - ukrywanie wywswl - zera

        if State[0][1]==0 :
            var1.set("")
        else:
            var1.set(State[0][1])


        self.ent_nr_fab= Entry(self,textvariable=var1)
        self.ent_nr_fab.grid(row=0, column = 4)



        self.lbl_dist_5=Label(self)
        self.lbl_dist_5.grid(row = 0, column = 5 , padx=4)                               #dystans col  5

        #utworz przyciski 'archiwum'0

        self.btn_up = Button(self,text= "UP", command=self.arch_UP )
        self.btn_up.grid(row = 0, column=6 , sticky=E)

        self.btn_up = Button(self,text= "DN", command=self.arch_DOWN )
        self.btn_up.grid(row = 0, column=7 , sticky=W)




        self.lbl_dist_8=Label(self)
        self.lbl_dist_8.grid(row = 0, column = 5 , padx=4)                               #dystans col  8


########################################################################################################################################################################################

    #poziom lini kod produktu

    def kod_prod(self,State):


        self.lbl_kod_prod = Label(self, text ="Podaj kod produktu")
        self.lbl_kod_prod.grid(row = 1, column = 1 , sticky = W )

    #utworz widzet Entry do przyjecia nr_fab

        var1=StringVar()    # zmienna pomocnicza - ukrywanie wywswl - zera

        if State[0][1]==0 :
            var1.set("")
        else:
            var1.set(State[0][2])
        self.ent_kod_prod= Entry(self,textvariable=var1)
        self.ent_kod_prod.grid(row=1, column = 4)









########################################################################################################################################################################################



    #poziom lini nr_zlecenia


    def nr_zlec(self,State):

        # utworz etykiete z zapytniem o zlecenie
        self.lbl_nr_zlec = Label(self, text ="Podaj nr zlecenia")
        self.lbl_nr_zlec.grid(row = 2, column = 1 , columnspan = 1, sticky = W )


        # utworz widzet Entry do przyjecia zlecenia


        var2=StringVar()    # zmienna pomocnicza - ukrywanie wywswl - zera

        if State[0][1]==0 :
            var2.set("")
        else:
            var2.set(State[0][3])


        self.ent_nr_zlec= Entry(self,textvariable=var2)
        self.ent_nr_zlec.grid(row=2, column = 4)





########################################################################################################################################################################################


    #poziom lini identyfikacja


    def identyfikacja(self,State):


        self.lbl_identity = Label(self, text ="Identyfikacja")
        self.lbl_identity.grid(row = 3, column = 1,sticky = W )
        self.identity = StringVar()
        self.identity.set(State[0][4])



        Radiobutton(self,
                    text =  "Tak",
                    variable = self.identity,
                    value = "Pozytyw",
                    ).grid(row = 3, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.identity,
                    value = "Negatyw",
                    ).grid(row = 3, column = 4, sticky=E)



    # Wyswietlanie stanu   z bazy
        if State[0][1]!=0 :
            self.lbl_identyity_info = Label(self,text=State[0][4] )
            self.lbl_identyity_info.grid(row = 3, column = 7)

#######################################################################################################################################################################################





    #poziom lini filtry uszczelka
    def filtry_uszczelki(self,State):


        self.lbl_filter_gasket = Label(self, text ="Filtry-Uszczelki-Silikon-Dławice ")
        self.lbl_filter_gasket.grid(row = 4, column = 1,sticky = W )

        self.filter_gasket = StringVar()

        self.filter_gasket.set(State[0][5])


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.filter_gasket,
                    value = "Pozytyw",
                   # command = self.update_text
                    ).grid(row = 4, column = 4,sticky=W)

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.filter_gasket,
                    value = "Negatyw",
                   #command = self.update_text
                    ).grid(row = 4, column = 4,sticky=E)


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_filter_gasket_info = Label(self,text=State[0][5])
            self.lbl_filter_gasket_info.grid(row = 4, column = 7)


        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 100, column = 5 , pady=2)                               #dystans col  9





#######################################################################################################################################################################################





    #poziom lini szczelnosc wymiennika
    def wymiennik_szczel_dokrec(self,State):


        self.lbl_czynnosc = Label(self, text ="Wymiennik-Szczelność-Dokręcenie")                   #change
        self.lbl_czynnosc.grid(row = 5, column = 1,sticky = W )                                    #change

        self.szczel_wymien = StringVar()                                                           #change

        self.szczel_wymien.set(State[0][6])                                                        #change


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.szczel_wymien,                                                 #change
                    value = "Pozytyw",
                    ).grid(row = 5, column = 4,sticky=W)                                           #change

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.szczel_wymien,                                                 #change
                    value = "Negatyw",
                    ).grid(row = 5, column = 4,sticky=E)                                           #change


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][6])                                   #change
            self.lbl_czynnosc_info.grid(row = 5, column = 7)                                        #change





#######################################################################################################################################################################################





    #poziom lini Silikonowanie  i dławice
    def prowadz_konc_przew(self,State):                                                            #change


        self.lbl_czynnosc = Label(self, text ="Prowadzenie i końcówki przewodów ")                 #change
        self.lbl_czynnosc.grid(row = 6, column = 1,sticky = W )                                    #change

        self.prow_kon_przew = StringVar()                                                          #change

        self.prow_kon_przew.set(State[0][7])                                                       #change


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.prow_kon_przew,                                                #change
                    value = "Pozytyw",
                    ).grid(row = 6, column = 4,sticky=W)                                           #change

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.prow_kon_przew,                                                #change
                    value = "Negatyw",
                    ).grid(row = 6, column = 4,sticky=E)                                           #change


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][7])                                  #change
            self.lbl_czynnosc_info.grid(row = 6, column = 7)                                       #change


########################################################################################################################################################################################



    #poziom lini Poprawność montażu NW
    def montaz_nag_wt(self,State):                                                              #change


        self.lbl_czynnosc = Label(self, text ="Mont. nagrzewnicy wtórnej " )                       #change
        self.lbl_czynnosc.grid(row = 7, column = 1,sticky = W )                                    #change

        self.mon_NW = StringVar()                                                             #change

        self.mon_NW.set(State[0][8])                                                          #change


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.mon_NW,                                                  #change
                    value = "Pozytyw",
                    ).grid(row = 7, column = 4,sticky=W)                                          #change

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.mon_NW,                                                  #change
                    value = "Negatyw",
                    ).grid(row = 7, column = 4,sticky=E)                                          #change


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][8])                                  #change
            self.lbl_czynnosc_info.grid(row = 7, column = 7)                                       #change


        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 100, column = 5 , pady=2)                                       #dystans col  9




########################################################################################################################################################################################



    #poziom lini Poprawność motażu układu sterownia - wart. zabezp. nadprąd.
    def montaz_rozdz(self,State):                                                                    #change


        self.lbl_czynnosc = Label(self, text ="Mont. rozdzielnicy, zabezp. nadprądowe." )             #change
        self.lbl_czynnosc.grid(row = 8, column = 1,sticky = W )                                   #change

        self.mon_roz = StringVar()                                                          #change

        self.mon_roz.set(State[0][9])                                                       #change


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.mon_roz,                                                #change
                    value = "Pozytyw",
                    ).grid(row = 8, column = 4,sticky=W)                                          #change

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.mon_roz,                                                #change
                    value = "Negatyw",
                    ).grid(row = 8, column = 4,sticky=E)                                          #change


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][9])                                  #change
            self.lbl_czynnosc_info.grid(row = 8, column = 7)                                       #change



########################################################################################################################################################################################



    #poziom lini Działanie wentylatorów i presostatów.
    def dzial_wentyl(self,State):                                                              #change


        self.lbl_czynnosc = Label(self, text ="Działanie wentylatorów i presostatów" )             #change
        self.lbl_czynnosc.grid(row = 9, column = 1,sticky = W )                                   #change

        self.dzial_went = StringVar()                                                          #change

        self.dzial_went.set(State[0][10])                                                       #change


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.dzial_went,                                                #change
                    value = "Pozytyw",
                    ).grid(row = 9, column = 4,sticky=W)                                          #change

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.dzial_went,                                                #change
                    value = "Negatyw",
                    ).grid(row = 9, column = 4,sticky=E)                                          #change


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][10])                                  #change
            self.lbl_czynnosc_info.grid(row = 9, column = 7)                                       #change



########################################################################################################################################################################################



    #poziom lini montaż czujniki
    def montaz_czujnikow(self,State):                                                              #change


        self.lbl_czynnosc = Label(self, text ="Montaż czujników" )             #change
        self.lbl_czynnosc.grid(row = 10, column = 1,sticky = W )                                   #change

        self.mon_czujn = StringVar()                                                          #change

        self.mon_czujn.set(State[0][11])                                                       #change


        Radiobutton(self,
                    text =  "Tak",
                    variable = self.mon_czujn,                                                #change
                    value = "Pozytyw",
                    ).grid(row = 10, column = 4,sticky=W)                                          #change

        Radiobutton(self,
                    text =  "Nie",
                    variable = self.mon_czujn,                                                #change
                    value = "Negatyw",
                    ).grid(row = 10, column = 4,sticky=E)                                          #change


# Wyswietlanie stanu  z bazy

        if  State[0][1]!=0 :
            self.lbl_czynnosc_info = Label(self,text=State[0][11])                                  #change
            self.lbl_czynnosc_info.grid(row = 10, column = 7)                                       #change


        self.lbl_dist_9=Label(self)
        self.lbl_dist_9.grid(row = 100, column = 5 , pady=2)                                       #dystans col  9



#######################################################################################################################################################################################


    #poziom lini przycisk akceptuj

    def btn_akcept(self):
        #utworz przycisk - akceptuj- poziom
        self.submit_bttn = Button(self, text ="Akceptuj", command = self.akcept)
        self.submit_bttn.grid(row = 101, column = 1)




    # funkcja przycisku akeptuj
    def akcept (self):
        """Wyswietl komunikat zależny od poprawnosci hasla"""
        contens1 = str(self.ent_nr_fab.get())
        contens2 = str(self.ent_kod_prod.get())
        contens3 = str(self.ent_nr_zlec.get())
        id1 = self.identity.get()
        id2 = self.filter_gasket.get()
        id3 = self.szczel_wymien.get()
        id4 = self.prow_kon_przew.get()                                                                                                   #add
        id5 = self.mon_NW.get()
        id6 = self.mon_roz.get()
        id7 = self.dzial_went.get()
        id8 = self.mon_czujn.get()

        messagebox.showinfo("Check window", contens1+";"+contens2+";"+ contens3+";"+id1+";"+id2+";"+id3+ ";" + id4+";"+id5+";"+id6+";"+id7+";"+id8)      #add
        cur.execute('INSERT INTO tab VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?);',(contens1,contens2,contens3,id1,id2,id3,id4,id5,id6,id7,id8))                    #add

        con.commit()

    #  funkcja zwiększająca zmeinną sterującą bazą
    def arch_UP(self):
        self.n+=1
        self.arch(n)

    #  funkcja zmniejszająca zmeinną sterującą bazą
    def arch_DOWN(self):
        self.n-=1
        self.arch(n)




########################################################################################################################################################################################

    # funkcja przycisku archiwizacja - THE END
    def arch (self,n):
        State=[]


        cur.execute(
            """
            SELECT ID,nr_fabr,kod_prod, nr_zlec,identyfikacja,filtry_uszczelki,szczel_wymien,prowadz_przew_kon, mon_NW, mon_roz, dzial_went,mon_czujn FROM tab

            """)
        State_Train = cur.fetchall()
        State=State_Train[self.n:]


        self.grid_remove()

        app1 = Application(root,State,self.n)
        return State,app1,n







# czesc glowna


root = Tk()
root.title("KJ Ambery")
root.geometry("520x500")



app = Application(root,State,n)



root.mainloop()

