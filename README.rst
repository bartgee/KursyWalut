===========
Kursy Walut
===========


.. image:: https://img.shields.io/pypi/v/kursywalut.svg
        :target: https://pypi.python.org/pypi/kursywalut

.. image:: https://img.shields.io/travis/bartgee/KursyWalut.svg
        :target: https://travis-ci.org/bartgee/KursyWalut

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

Używanie
--------

Jako osobna aplikacja::

    (venv) $ kursywalut
    ##################
    $ KursyWalut 0.2 $
    ##################

    Pobieram dane... FOREX
    OK
    Pobieram dane... NBP
    OK

    FOREX	kupno	sprzedaż

    DATA	Dziś, 20.12.2018 09:43
    EUR	4,2800	4,2825
    CHF	3,7769	3,7799
    GBP	4,7404	4,2825
    USD	3,7447	3,7472

    NBP	kurs średni

    DATA	nr 246/A/NBP/2018 z dnia 19-12-2018
    EUR	4,2846
    CHF	3,7875
    GBP	4,7607
    USD	3,7619


W swoim programie::

    (venv) $ ipython
    Python 3.6.7 (default, Oct 22 2018, 11:32:17)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: import kursywalut

    In [2]: moneypl = kursywalut.handlers.MoneyPlHandler()

    In [3]: data = moneypl.get_moneypl()
    Pobieram dane... FOREX
    OK
    Pobieram dane... NBP
    OK

    In [4]: print(data)
    OrderedDict([('FOREX', OrderedDict([('DATA', 'Dziś, 20.12.2018 09:59'), ('EUR', ['4,2808', '4,2833']), ('CHF', ['3,7784', '3,7813']), ('GBP', ['4,7429', '4,2833']), ('USD', ['3,7453', '3,7478'])])), ('NBP', OrderedDict([('DATA', 'nr 246/A/NBP/2018 z dnia 19-12-2018'), ('EUR', '4,2846'), ('CHF', '3,7875'), ('GBP', '4,7607'), ('USD', '3,7619')]))])


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
