===========
Kursy Walut
===========


.. image:: https://img.shields.io/pypi/v/kursywalut.svg
        :target: https://pypi.python.org/pypi/kursywalut

.. image:: https://img.shields.io/travis/bartgee/kursywalut.svg
        :target: https://travis-ci.org/bartgee/kursywalut

.. image:: https://readthedocs.org/projects/kursywalut/badge/?version=latest
        :target: https://kursywalut.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/bartgee/kursywalut/shield.svg
     :target: https://pyup.io/repos/github/bartgee/kursywalut/
     :alt: Updates



Program do wyświetlania i przeliczania aktualnych kursów walut.


* Free software: GNU General Public License v3
* Documentation: https://kursywalut.readthedocs.io.


Funkcje programu
----------------

* Pobiera aktualne kursy walut EUR, CHF, GBP i USD ze strony http://www.money.pl
* Pobiera datę i godzinę kursów

Przyszłość
----------

* Dodanie przeliczania podanej kwoty dowolnej waluty na PLN
* Dodanie przeliczania podanej kwoty z dowolnej waluty na inną dowolną

Dalsza przyszłość
-----------------

* Praca w trybie daemona i gromadzenie danych w bazie danych
* Generowanie strony wwww z aktualnymi i historycznymi kursami walut

UWAGA!
------

Wersja 0.1 została otagowana tylko ze wględów historycznych. Od dłuższego czasu nie działa,
ponieważ WP zmieniło stronę z kursami walut. Poprzednia wersja była w zasadzie prostym skryptem,
dlatego zdecydowałem się przepisać program na nowo.

Stabilny kod można pobrać z mastera, branch dev jest jako rozwojowy i może się zdarzyć że kod
z deva nie będzie działał. Pracuję nad wersją 0.2, która będzie bazować na tym co na dzień 17.12.2018
jest w masterze.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
