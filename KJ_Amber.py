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
l=100     #parametry listy-ilosc zagniezdzen
x=100    #parametry listy- ilosc zmiennych(str) w zagniezdzeniu
State=[]
for s in range(l):
    sub_list=[""]
    for y in range(x):

        sub_list.append(int(y))

        State.append(sub_list)

n=-1  #zmienna odpow. za poruszanie po bazie


#State=[[" "," "],[" "," "]]





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


        self.lbl_filter_gasket = Label(self, text ="Filtry i uszczelki ")
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


########################################################################################################################################################################################


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
        messagebox.showinfo("Check window", contens1+";"+contens2+";"+ contens3+";"+id1+";"+id2)
        cur.execute('INSERT INTO tab VALUES (NULL,?,?,?,?,?);',(contens1,contens2,contens3,id1,id2))

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
            SELECT ID,nr_fabr,kod_prod, nr_zlec,identyfikacja,filtry_uszczelki FROM tab

            """)
        State_Train = cur.fetchall()
        State=State_Train[self.n:]


        self.grid_remove()

        app1 = Application(root,State,self.n)
        return State,app1,n


#nr_fabr,nr_zlec,identyfikacja,filtry_uszczelki





# czesc glowna


root = Tk()
root.title("KJ Ambery")
root.geometry("400x200")



app = Application(root,State,n)



root.mainloop()

