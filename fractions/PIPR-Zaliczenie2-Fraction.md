# PIPR laboratorium
## Zaliczenie 2 - Fraction

Opracować klasę Fraction reprezentującą ułamek o liczniku i mianowniku będącym liczbą całkowitą. Klasa powinna umożliwiać wykonywanie następujących operacji:
* Konstruktor z dwoma parametrami (wartość licznika i wartość mianownika np. 15 i 5).
* Operacje: +, -, *, / na dwóch ułamkach – wynikiem ma być nowy ułamek.
* Operacje dodawania do ułamka liczby całkowitej – wynikiem ma być nowy ułamek.
* Pobranie wartości licznika.
* Pobranie wartości mianownika.
* Ustawienie wartości ułamka (podajemy dwa parametry: wartość licznika i wartość mianownika np. 8 i 2).
* Pobranie wartości ułamka jako liczbę rzeczywistą.
* Pobranie reprezentacji tekstowej (metoda __str__) ułamka np. „-5/8”.

Rozwiązanie zadania (pliki z kodem źródłowym) mają być umieszone w repozytorium przed końcem zaliczenia.

### Dodatkowe wymagania:
* Ułamek ma być zawsze przechowywany w postaci znormalizowanej. Ułamek jest w postaci znormalizowanej jeśli największy wspólny dzielnik modułu licznika i modułu mianownika jest równy 1.
Przykładowo wynikiem operacji dodawania dwóch ułamków 2/8 i 1/4 będzie ułamek 16/32 a po normalizacji 1/2.
Wskazówka: zaimplementować i wykorzystać funkcję GCD obliczającą największy wspólny dzielnik dwóch liczb.
* Ma być jedna wewnętrzna reprezentacja ułamka o wartości 0 (ułamek o wartości 0 ma mieć tylko jedną reprezentację wewnętrzną).
* Ma być jedna wewnętrzna reprezentacja ułamków o wartości ujemnej (ułamek o konkretnej wartości ujemnej ma mieć tylko jedną reprezentację wewnętrzną).
* W przypadku kiedy nie można wykonać operacji – sytuacja błędna ma to być sygnalizowane przez zgłoszenie wyjątku.
* Należy unikać powielania tego samego kodu.
* Proszę pamiętać o testach do każdej z operacji.

### Słownik:
* ułamek – fraction,
* licznik – numerator,
* mianownik – denominator,
* dodaj – add,
* odejmij – subtract,
* pomnóż – multiply,
* podziel – divide,
* największy wspólny dzielnik NWD – greatest common divisor GCD.

### Wskazówka:
Algorytm obliczania największego wspólnego dzielnika dwóch liczb.

    int GCD( int a, int b)
    {
        while( b != 0 )
            c = a % b;
            a = b;
            b = c;
        return a;
    }