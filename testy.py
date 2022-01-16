from tkinter import Tk
from tkinter import messagebox
import logika
from logika import *
import unittest


class Testy(unittest.TestCase):
    root = Tk()
    logika1 = RegulyGry(root)
    logikagry = Logika_Gry(root)
    oknogry = Okno(root)
    oknogry.okno_gry()

    def test1(self):
        """Wyswietlenie w konsoli wylosowanego kodu, wpisanie odpowiedzi z bledymi cyframi - oczekiwana informacja o braku poprawnych trafien"""
        print("TEST 1 -----------------------------")
        self.logika1.kod = ['2', '2', '2', '2']
        print(self.logika1.kod)
        testowy_kod = StringVar(self.root, "1111")
        print(Logika_Gry.logika_gry(self.logikagry, testowy_kod))

    def test2(self):
        """Wyswietlenie wylosowanego kodu, wpisanie odpowiedzi z poprawymi vyrafmi w zlych miejsach - oczekiwana informacja o niepoprawnym polozeniu"""
        print("TEST 2 -----------------------------")
        self.logika1.kod = ['1', '2', '3', '4']
        print(self.logika1.kod)
        testowy_kod = "4321"
        czerwona_flaga = ""
        biala_flaga = ""
        for i in range(4):
            if testowy_kod[i] == self.logika1.kod[i]:
                czerwona_flaga += "R"
            if testowy_kod[i] != self.logika1.kod[i] and testowy_kod[i] in self.logika1.kod:
                biala_flaga += "W"
        podpowiedz = czerwona_flaga + biala_flaga
        print(podpowiedz)

    def test3(self):
        """Wyswietlenie wylosowanego kodu, wpisanie odpowiedzi z dwoma poprawnymi cyframi w dobrych miejscach i dwoma poprawnymi w zlych miejscach"""
        print("TEST 3 -----------------------------")
        self.logika1.kod = ['1', '2', '3', '4']
        print(self.logika1.kod)
        testowy_kod = "1243"
        czerwona_flaga = ""
        biala_flaga = ""
        for i in range(4):
            if testowy_kod[i] == self.logika1.kod[i]:
                czerwona_flaga += "R"
            if testowy_kod[i] != self.logika1.kod[i] and testowy_kod[i] in self.logika1.kod:
                biala_flaga += "W"
        podpowiedz = czerwona_flaga + biala_flaga
        print(podpowiedz)

    def test4(self):
        """Wyswietlenie wylosowanego kodu, wpisane poprawnej odpowiedzi - oczekiwana informacja o wygranej"""
        print("TEST 4 -----------------------------")
        self.logika1.kod = ['1', '2', '3', '4']
        print(self.logika1.kod)
        testowy_kod = "1234"
        czerwona_flaga = ""
        biala_flaga = ""
        zmienna=0
        for i in range(4):
            if testowy_kod[i] == self.logika1.kod[i]:
                zmienna += 1
            if testowy_kod[i] == self.logika1.kod[i]:
                czerwona_flaga += "R"
            if testowy_kod[i] != self.logika1.kod[i] and testowy_kod[i] in self.logika1.kod:
                biala_flaga += "W"
        podpowiedz = czerwona_flaga + biala_flaga
        print(podpowiedz)
        if zmienna == 4:
            print("Wygrana!")

    def test5(self):
        """Wpisanie 12 razy niepoprawnego kodu """
        print("TEST 5 -----------------------------")
        self.logika1.zasady_gry = 0
        self.logika1.kod = ['2', '2', '2', '2']
        print("kod: ",self.logika1.kod)
        self.logika1.podejscia =0
        testowy_kod = "1234"
        for i in range(12):
            print(testowy_kod)
            self.logika1.podejscia += 1
        if self.logika1.podejscia == 12:
            print("Przegrana!")

    def test6(self):
        """Próba wpisania niepoprawnego kodu do pola odpowiedzi (mniej lub wiecej niz 4 znaki, znaki nie będące cyframi od 1 do 6 """
        print("TEST 6 -----------------------------")
        self.logika1.zasady_gry = 0
        test = "7777"
        logika.bledy_wejscia(test)

    def test7(self):
        """Wciśnięcie przycisku "Oszust" przy poprawnych zasadach gry - oczekiwana informacja "tere fere" """
        print("TEST 7 -----------------------------")
        self.logika1.zasady_gry = 0
        self.logika1.czy_oszust()
        if  self.logika1.zasady_gry ==0:
            print("tere fere")

    def test8(self):
        """Wciśnięcie przycisku "Oszust" przy niepoprawnych zasadach gry - oczekiwana informacja "złapałeś mnie" """
        print("TEST 8 -----------------------------")
        self.logika1.zasady_gry = 1
        self.logika1.czy_oszust()
        if  self.logika1.zasady_gry ==1:
            print("złapałeś mnie")


if __name__ == '__main__':
    unittest.main()



