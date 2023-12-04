Jesteś programistą w dużym zespole pracującym nad cyfrową wersją popularnej gry
planszowej Piwniczak. Z powodu złego zarządzania projektem i zbliżającymi się świętami musisz do końca deadline'u (16:00) dopisać moduł gry, który odpowiada za rzucanie kośćmi gracza. Przykładowe kości biorące udział w grze (zapis jest w konwencji `<liczba kości>x D<liczba ścian> R<liczba możliwych ponownych rzutów daną kością>`):

* 2x D4 R2
* 2x D6 R0
* 1x D6 R1
* 1x D6 R0
* 2x D8 R1
* 1x D10 R2
* 1x D12 R3

**Uwaga:**

1. powyższy zapis służy tylko do zrozumienia zadania, kości tworzone są przez odp. API w którym każdy parametr kości jest argumentem; kości nie są wczytywane z napisu tekstowego,
2. wyrzucona kość daje wartości z przedziału <1..liczba ścian> z równymi prawdopodobieństwami,
3. moduł powinien pracować z dowolnymi poprawnymi kośćmi (patrz niżej), ponieważ inne zespoły nadal pracują w pocie czoła nad dodawaniem nowych treści do gry.

Moduł pozwala na:

* stworzenie pojedynczej kości - zakładamy, że poprawna kość ma parzystą, większą od 2 liczbę ścian oraz liczbę ponownych rzutów większą bądź równą 0
* reprezentację zestawu kości w ręce - tworzoną na podstawie listy instancji kości, które będą brały udział w rzucie
* rzut kośćmi z ręki - pozwala programiście na dostęp do sekwencji wyrzuconych oczek z informacją na jakiej kości poszczególne wartości zostały wyrzucone
* ponowny rzut wybranymi kośćmi, które brały udział w rzucie (czyli zignorowanie wartości rzutu na danej kości i rzucenie nią jeszcze raz) zgodnie z liczbą możliwych ponownych rzutów danej kości
* podanie sumy wyrzuconych oczek
* porównanie rzutów dwóch graczy (tj. zwrócenie różnicy między sumą wyrzuconych oczek ze wskazaniem zwycięzcy)
* wygenerowanie raportu tekstowego z rzutu, przykładowy raport poniżej:

```
* D8: 4
* D6: 1
* D4: 2
* D4: 3
Total roll value: 10 / 22
```

Na potrzeby implementacji można korzystać tylko z biblioteki standardowej pythona i modułu `pytest`.

Podpowiedź:
funkcja `randint` z modułu `random`

Słowniczek:

* ręka - hand
* kość - dice
* rzut - roll
* ponowny rzut - reroll
* oczko - value
* gracz - player
