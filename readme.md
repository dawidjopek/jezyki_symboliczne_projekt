### Dawid Jopek
### Projekt z Języków Symbolicznych – dokumentacja

## Temat projektu

W tym projekcie prezentuje odmianę gry Mastermind (Mastermind (gra planszowa) – Wikipedia, wolna encyklopedia), Gra na początku losuje tajny kod składający się z 4 cyfr (np.1234, 5425), cyfry znajdują się w zakresie od 1 do 6. 

## Działanie gry

Gracz wpisuje cyfry bez spacji. Po nieprawnej odpowiedzi gracza, gra wyświetla na ekranie tą odpowiedź oraz podpowiedzi(flagi). Flaga czerwona (R) sygnalizuję, że gracz podał poprawną cyfrę na poprawnej pozycji. Flaga biała(W) sygnalizuje, że gracz podał poprawną liczbę na niepoprawnej pozycji. Brak Flagi oznacza, że gracz podał niepoprawną liczbę. Gracz ma 12 prób aby odgadnąć tajny kod. Wpisywanie kodu przez gracza potwierdza się przyciskiem „Sprawdź”. W grze występuje również przycisk „Reset”, który restartuje grę. Przed rozpoczęciem każdej gry, program losuje zestaw Reguł gry, program może oszukiwać gracza podając mu niepoprawne odpowiedzi, wtedy gracz może wcisnąć przycisk „Oszust”, jeżeli gracz miał racje program przyznaje się do oszustwa, jeżeli gracz się pomylił to przegrywa.
As [John Gruber] writes on the [Markdown site][df1]

## Klasy i funkcje w projekcie

### Funkcja main [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/main.py#L1)
Ma za zadanie wyświetlić okno gry, wraz z parametrami. Uruchamia program

### Klasa RegulyGry [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L35)
Ta klasa inicjalizuje zmienne oraz znajdują się w niej funkcje czy_oszust, która ma za zadanie sprawdzić 
na jakich zasadach toczona jest gra. Oraz funkcja reset_gry, która ma za zadanie resetowanie gry

### Klasa Logika_Gry [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L75)
Ta klasa dziedziczy po klasie RegulyGry. W tej klasie realizowana jest cała logika gry, przy poprawnych 
zasadach, w tej klasie sprawdzane są odpowiedzi gracza i generowane podpowiedzi.

### Klasa Logika_Gry_oszust [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L118)
Ta klasa dziedziczy po klasie RegulyGry. W tej klasie realizowana jest logika gry, przy niepoprawnych 
zasadach, w tej klasie program generuje losowo błędne podpowiedzi przez co gracz nie jest w stanie 
wygrać gry.

### Klasa Okno [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L156)
Ta klasa dziedziczy po klasie RegulyGry. W tej klasie znajduje się funkcja okno_gry, która odpowiada za 
wyświetlanie się wszystkich wymaganych pól w oknie.

### Funkcja wyjątków bledy_wejscia [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L18)
Funkcja ta ma za zadanie, wychwycić błędy w podanej odpowiedzi przez gracza. Np. gdy gracz poda 5 
liczb. Albo poda liczbę mniejszą od 1 lub większą od 6

### Lambda-wyrażenia [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L172)
Realizowane są w klasie Okno, w funkcji okno_gry, przypisane do przycisków, mające na celu 
uruchomienie odpowiednich zasad gry

### List comprehensions [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L86)
Realizowane np. w klasie Logika_Gry, w funkcji logika_gry, mają za zadanie sprawdzenie poprawnych 
odpowiedzi i wypisanie podpowiedzi.

### Moduły [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/5ccd63ddc6faf883b02db37f56ff76486b441184/logika.py#L1)
W projekcie zostały wykorzystanie moduły:
Tkinter, random, unitest

### Testy
Testy zrealizowane w pliku testy.py  [link](https://github.com/dawidjopek/jezyki_symboliczne_projekt/blob/main/testy.py)
