KursyWalut
==========

Aplikacja do wyświetlania i przeliczania aktualnych kursów walut do polskich złotych czyli:

Web scraping http://finanse.wp.pl/waluty.html

Under development... might be not stable!

Co aktualnie może program?

- pobiera dane o aktualnych kursach dla walut EUR, CHF, USD i GBP ze strony http://finanse.wp.pl/waluty.html
- pobiera godzinę i datę kursów i dodaje je do listy dictów
- dodaje dane do listy dictów i wyświetla kursy w czytelnej formie
- w przypadku uruchomienia programu z podaną wartością w PLN jako parametr, przelicza dodatkowo podaną kwotę na wyżej wymienione waluty

Funkcje, które zostaną dodane w najbliższej przyszłości:

- przeliczanie dowolnej waluty na PLN
- przeliczanie dowolnej waluty na inną dowolną
- praca w trybie daemona i gromadzenie danych w bazie SQLite3

Dalsza przyszłość?

- web scraping stron banków w celu pobierania i gromadzenia danych o kursach spłaty (kredyty hipoteczne)
- pewnie pojawią się też inne pomysły - jestem otwarty na propozycje (mój email znajdziecie w moim profilu na GitHubie)
