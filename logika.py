from tkinter import *
from tkinter import messagebox
from random import *
import random


#Funkcje programu:
def generuj_kod():
    """Funkcja, generujaca losowy kod, ktory gracz ma odgadnąć """
    return [choice('123456') for _ in range(4)]

def losuj_zasady_gry():
    """Funkcja, losujaca zestaw zasad gry """
    x= randint(0, 1)
    #print("zasady gry:",x)
    return x

def bledy_wejscia(odpowiedz):
    """Funkcja, wylapujaca błedy podczas wpisywania odpowiedzi przez gracza """
    if len(str(odpowiedz)) != 4:
        messagebox.showerror('zle dane','Odpowiedz musi skladac sie z 4 cyrf pisanych razem!')
        return False
    else:
        for i in str(odpowiedz):
            try:
                if int(i) < 1 or int(i) > 6:
                    messagebox.showerror('zle dane','Odpowiedz musi skldac sie z cyfr od 1 do 6')
                    return False
            except ValueError:
                messagebox.showerror('zle dane', 'dane musza byc liczbami od 1 do 6, pisanymi bez spacji')
                return False
        return True


class RegulyGry:
    """Klasa reguly gry, oraz inicjalizacja zmiennych """
    def __init__(self,root):
        self.root = root
        self.pole_teksowe = Entry()
        self.odpowiedzi = Label()
        self.sprawdz = Button()
        self.oszust = Button()
        self.reset = Button()
        self.kod = generuj_kod()
        self.podejscia = 0
        self.ustawienie_odpowiedzi = 1
        self.odpowiedz = ' '
        self.podpowiedz = ' '
        self.status_gry = Label()
        self.zasady_gry = 0
        self.wiadomosc_powitalna = Label()

    def czy_oszust(self):
        """Funkcja sprawdzająca na jakich zasadach jest toczona gra """
        if self.zasady_gry == 1:
            self.sprawdz['state'] = 'disabled'
            self.oszust['state'] = 'disabled'
            self.status_gry.config(text='Złapałeś/łas mnie!')
        elif self.zasady_gry ==0:
            self.sprawdz['state'] = 'disabled'
            self.oszust['state'] = 'disabled'
            opis = "Tere fere",self.kod
            self.status_gry.config(text=opis)

    def reset_gry(self):
        """Funkcja słóżąca do resetu gry, najlpierw czyści okno, później startuje gre od nowa """
        for widget in self.root.winfo_children():
            widget.destroy()
        self.kod.clear()
        self.kod = generuj_kod()
        self.podejscia = 0
        self.ustawienie_odpowiedzi = 1
        Okno.okno_gry(self)

class Logika_Gry(RegulyGry):
    def logika_gry(self,odp):
        """Klasa Logika_Gry, dziedzicząca po klasie RegułyGry, operuje całą logiką gry dla poprawnego zestawu zasad """
        self.odpowiedz = odp.get()
        assert bledy_wejscia(self.odpowiedz) is True
        czerwona_flaga = ""
        biala_flaga = ""
        zmienna = 0
        if zmienna != 4:
            """W tym miejscu następuje sprawdzenie odpowiedzi gracza i napisanie podpowiedzi R-czerwona_flaga W-biala_flaga """
            for i in range(4):
                if self.odpowiedz[i] == self.kod[i]:
                    zmienna +=1
                if self.odpowiedz[i] == self.kod[i]:
                    czerwona_flaga += "R"
                if self.odpowiedz[i] != self.kod[i] and self.odpowiedz[i] in self.kod:
                    biala_flaga += "W"

            self.podpowiedz = czerwona_flaga + biala_flaga
            podpowiedz_mix = list(self.podpowiedz)
            random.shuffle(podpowiedz_mix)
            self.podpowiedz = podpowiedz_mix
            #print(self.podpowiedz)
        """Wyswietlenie odpwowiedzi gracza w oknie """
        odpowiedzi_gracza = self.ustawienie_odpowiedzi,self.odpowiedz,self.podpowiedz
        odpowiedz_gracza = Label(self.root, text=odpowiedzi_gracza)
        odpowiedz_gracza.pack()
        """Po każdej odpowiedzi następuje zwiększenie licznika podejść jak i licznika liczącego podejscie """
        self.ustawienie_odpowiedzi = self.ustawienie_odpowiedzi+1
        self.podejscia = self.podejscia +1

        if zmienna == 4:
            """Jeżeli kod który podał gracz jest poprawny to w tym miejscu następuje ogłoszenie wygranej"""
            self.status_gry.config(text='Wygrana!',font=30, fg="green")
            self.sprawdz['state'] = 'disabled'
            self.oszust['state'] = 'disabled'
        elif self.podejscia >= 12:
            """Jeżeli gracz nie odgadnie kodu, następuje ogłoszenie przegarnej """
            opis = "Przegrana!,", self.kod
            self.sprawdz['state'] = 'disabled'
            self.oszust['state'] = 'disabled'
            self.status_gry.config(text=opis, font=30, fg="red")

class Logika_Gry_oszust(RegulyGry):
    """Klasa Logika_Gry_oszust, dziedzicząca po klasie RegułyGry, operuje logiką gry dla niepoprawnego zestawu zasad """
    def logika_gry_oszust(self,odp):
        self.odpowiedz = odp.get()
        assert bledy_wejscia(self.odpowiedz) is True
        czerwona_flaga = ""
        zmienna = 0
        """W tym miejscu generowana jest losowa podpowiedź, niezgodna z prawdą """
        if zmienna != 4:
            lista_bledow = ["R", "W", ""]
            for i in range(4):
                if self.odpowiedz[i] == self.kod[i]:
                    zmienna+=1
                if self.odpowiedz[i] == self.kod[i]:
                    czerwona_flaga += random.choice(lista_bledow)
                if self.odpowiedz[i] != self.kod[i]:
                    czerwona_flaga += random.choice(lista_bledow)

            self.podpowiedz = czerwona_flaga
            podpowiedz_mix = list(self.podpowiedz)
            random.shuffle(podpowiedz_mix)
            self.podpowiedz = podpowiedz_mix
            #print(self.podpowiedz)
        """Wyswietlenie odpwowiedzi gracza w oknie """
        odpowiedzi_gracza = self.ustawienie_odpowiedzi,self.odpowiedz,self.podpowiedz
        odpowiedz_gracza = Label(self.root, text=odpowiedzi_gracza)
        odpowiedz_gracza.pack()
        """Po każdej odpowiedzi następuje zwiększenie licznika podejść jak i licznika liczącego podejscie """
        self.ustawienie_odpowiedzi = self.ustawienie_odpowiedzi+1
        self.podejscia = self.podejscia +1

        """Jeżeli gracz wylosował zestaw reguł niepoprawnych, w takim przypadku nie ma możliwości zwycięstwa """
        if self.podejscia >=12:
            opis = "Przegrana! byłem oszustem a kod to:,", self.kod
            self.sprawdz['state'] = 'disabled'
            self.oszust['state'] = 'disabled'
            self.status_gry.config(text=opis,font=30, fg="red")

class Okno(RegulyGry):
    """Klasa dziedzicząca po klasie RegulyGry, w tej klasie znajduje sie funkcja do wyświetlania pól w oknie """
    def okno_gry(self):
        """Funkcja ma za zadanie wyświetlenie okna gry wraz z wszystkimi potrzebnymi polami """
        #print(self.kod)

        self.wiadomosc_powitalna = Label(self.root, text='Witaj w grze Mastermind! \nPodaj odpowiedz bez spacji np:1234, 5621 (liczby od 1 do 6)')
        self.wiadomosc_powitalna.pack()
        x= losuj_zasady_gry()
        """W tym miejscu losowane są zasady gry, tuż przed rozpoczęciem samej gry """
        self.zasady_gry = x
        #print("zasady gry:", x)
        odpowiedz = StringVar()
        self.textBox = Entry(self.root, width=10, textvariable=odpowiedz)
        self.textBox.pack()
        if x == 0:
            self.sprawdz = Button(self.root,text='Sprawdz', command=lambda odp=odpowiedz: Logika_Gry.logika_gry(self,odp))
            self.sprawdz.pack()
        elif x == 1:
            self.sprawdz = Button(self.root, text='Sprawdz', command=lambda odp=odpowiedz: Logika_Gry_oszust.logika_gry_oszust(self,odp))
            self.sprawdz.pack()
        self.reset = Button(self.root, text='Reset', command=self.reset_gry)
        self.reset.pack()
        self.oszust = Button(self.root, text='Oszust!', command=self.czy_oszust)
        self.oszust.pack()
        self.status_gry = Label(self.root, text=' ')
        self.status_gry.pack()

