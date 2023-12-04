# Dostawa

Zarządzasz firmą transportową z siedzibą w Warszawie, która posiada ciężarówkę i rozwozi towary do pięciu miast w Polsce: Krakowa, Gdańska, Poznania, Rzeszowa i Terespola. Po uzyskaniu zlecenia ciężarówka wyrusza do wybranego miasta, rozładowuje towar w miejscu docelowym i wraca do siedziby firmy. Ciężarówka porusza się z szybkością 80 km/h. Kierowca może jechać bez przerwy przez maksymalnie 3 godziny, następnie musi odpocząć co najmniej 3 godziny i może ruszać w dalszą drogę. W momencie dotarcia do miasta docelowego lub siedziby firmy kierowca jest wymieniany, więc wtedy czas odpoczynku nie musi być zachowany. Napisz klasę dostawy (Delivery), która przechowuje:
- aktualny cel podróży (nazwę miasta docelowego podczas podróży „w tamtą stronę”, nazwę miasta siedziby podczas podróży „z powrotem” lub None w przypadku braku zlecenia)
- dystans w kilometrach do aktualnego celu podróży
- liczbę godzin jazdy od ostatniego odpoczynku (liczba naturalna, w trakcie odpoczynku jest ustawiona na wartość None)
- liczbę godzin odpoczynku (liczba naturalna, w czasie jazdy jest ustawiona na wartość None)

| Miasto docelowe | Dystans w jedną stronę |  
| ———————— | ———————————— |  
| Kraków | 290 km |  
| Gdańsk | 340 km |  
| Poznań | 312 km |  
| Rzeszów | 330 km |  
| Terespol | 197 km |  

W pliku klasy zainicjalizowany jest słownik miast docelowych (destination_dictionary), który przyporządkowuje miastu docelowemu dystans w jedną stronę z siedziby (z wpisanymi wartościami z tabelki powyżej). Oprócz niego zainicjalizowana jest stała nazwy miasta siedziby (home_name), ustawiona na Warszawę.

Klasa dostawy obsługuje następujące metody:
- wyślij zlecenie (submit_order), która przyjmuje jako argument nazwę miasta docelowego. Metoda ustawia aktualny cel podróży, dystans w kilometrach oraz inicjalizuje czas jazdy na 0 i czas odpoczynku na None. Metoda zwraca błąd, jeżeli aktualny cel podróży jest już ustawiony oraz jeżeli firma nie obsługuje kursów do podanego miasta.
- jedź (drive), która przyjmuje jako argument liczbę godzin jazdy (liczba naturalna). Metoda ustawia dystans w kilometrach do aktualnego celu podróży na podstawie podanej liczby godzin i szybkości ciężarówki (80 km/h), a także liczbę godzin jazdy od ostatniego odpoczynku. Jeżeli w podanym czasie ciężarówka dojechała już do aktualnego celu podróży, jako cel ustawiana jest siedziba firmy (jeżeli nie jechaliśmy jeszcze „z powrotem”) lub zgłoszenie jest zerowane (jeśli właśnie wróciliśmy do siedziby). Metoda zwraca błąd, jeżeli kierowca jest w trakcie odpoczynku i nie powinien jeszcze ruszać w dalszą drogę (nie minęły 3 godziny) oraz jeżeli kierowca jest w trakcie jazdy i przekroczyłby limit jazdy bez przerwy, gdyby jechał jeszcze podaną liczbę godzin.
- odpoczywaj (rest), która przyjmuje jako argument liczbę godzin odpoczynku (liczba naturalna). Jeżeli kierowca był w trakcie jazdy, to metoda zeruje liczbę godzin jazdy i ustawia podaną liczbę godzin odpoczynku. Jeżeli kierowca jest w trakcie odpoczynku, metoda zwiększa liczbę godzin odpoczynku.
- ustaw siedzibę jako cel (start_returning_home) - metoda wewnętrzna, która jest wywoływana przez metodę drive(), gdy ciężarówka dojedzie do miasta docelowego (nie siedziby)
- wyzeruj podróż po powrocie (reset_after_return) - metoda wewnętrzna, która jest wywoływana przez metodę drive(), gdy ciężarówka dojedzie „z powrotem” do siedziby firmy.
- __str__, która wypisuje wszystkie aktualne informacje o stanie dostawy.

Należy przygotować testy uwzględniające przypadki standardowe i brzegowe oraz podanie nieprawidłowych danych. Należy zwrócić uwagę na styl przesłanego kodu.

 
