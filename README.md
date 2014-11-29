#KursyWalut

Aplikacja do wyświetlania i przeliczania aktualnych kursów walut do polskich złotych czyli:

Web scraping http://finanse.wp.pl/waluty.html

Under development... might be not stable!

##Co aktualnie może program?

- pobiera dane o aktualnych kursach dla walut EUR, CHF, USD i GBP ze strony http://finanse.wp.pl/waluty.html
- pobiera godzinę i datę kursów i dodaje je do listy dictów
- dodaje dane do listy dictów i wyświetla kursy w czytelnej formie
- w przypadku uruchomienia programu z podaną wartością w PLN jako parametr, przelicza dodatkowo podaną kwotę na wyżej wymienione waluty
- przelicza dowolną walutę na PLN (eg.: kursywalut 10 gbp)
- przelicza dowolną walutę na inną dowolną (eg. kursywalut 10 chf usd)

##Funkcje, które zostaną dodane w najbliższej przyszłości:

- praca w trybie daemona i gromadzenie danych w bazie SQLite3

##Dalsza przyszłość?

- web scraping stron banków w celu pobierania i gromadzenia danych o kursach spłaty (kredyty hipoteczne)
- pewnie pojawią się też inne pomysły - jestem otwarty na propozycje (mój email znajdziecie w moim profilu na GitHubie)

##Przykładowe działanie:

<pre><code>bart@wujeksamozuo:~$ kursywalut
$$$ KursyWalut 0.1 $$$

Pobieram dane...
Pobrałem dane!
Kursy z godz. 22:49, 14.11.2014 ze strony http://finanse.wp.pl/waluty.html:

Forex|EUR|4.22
Forex|CHF|3.52
Forex|USD|3.37
Forex|GBP|5.29
NBP  |EUR|4.23
NBP  |CHF|3.52
NBP  |USD|3.39
NBP  |GBP|5.32

bart@wujeksamozuo:~$ kursywalut 125
$$$ KursyWalut 0.1 $$$

Pobieram dane...
Pobrałem dane!
Kursy z godz. 22:49, 14.11.2014 ze strony http://finanse.wp.pl/waluty.html:

Forex|EUR|4.22
Forex|CHF|3.52
Forex|USD|3.37
Forex|GBP|5.29
NBP  |EUR|4.23
NBP  |CHF|3.52
NBP  |USD|3.39
NBP  |GBP|5.32

125 PLN po przeliczeniu:

Forex|EUR|29.62
Forex|CHF|35.51
Forex|USD|37.09
Forex|GBP|23.63
NBP  |EUR|29.55
NBP  |CHF|35.51
NBP  |USD|36.87
NBP  |GBP|23.50

bart@wujeksamozuo:~$ kursywalut 10 gbp
$$$ KursyWalut 0.1 $$$

Pobieram dane...
Pobrałem dane!
Kursy z godz. 22:49, 14.11.2014 ze strony http://finanse.wp.pl/waluty.html:

Forex|EUR|4.22
Forex|CHF|3.52
Forex|USD|3.37
Forex|GBP|5.29
NBP  |EUR|4.23
NBP  |CHF|3.52
NBP  |USD|3.39
NBP  |GBP|5.32

10 GBP po przeliczeniu na PLN:

Forex|GBP|52.90
NBP  |GBP|53.20

bart@wujeksamozuo:~$ kursywalut 10 usd chf
$$$ KursyWalut 0.1 $$$

Pobieram dane...
Pobrałem dane!
Kursy z godz. 22:47, 28.11.2014 ze strony http://finanse.wp.pl/waluty.html:

Forex|EUR|4.18
Forex|CHF|3.47
Forex|USD|3.36
Forex|GBP|5.25
NBP  |EUR|4.18
NBP  |CHF|3.48
NBP  |USD|3.36
NBP  |GBP|5.28

10 USD po przeliczeniu na CHF:

Forex|CHF|9.68
NBP  |CHF|9.66
</code></pre>
