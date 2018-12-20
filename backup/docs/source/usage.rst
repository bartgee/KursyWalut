=====
Usage
=====

Podstawowe użycie::

    (venv) bart@gdn-n-bart:~/Dokumenty/python/github/KursyWalut/docs$ kursywalut
    ##################
    $ KursyWalut 0.2 $
    ##################

    Pobieram dane... FOREX
    OK
    Pobieram dane... NBP
    OK

    FOREX	kupno	sprzedaż

    DATA	Dziś, 20.12.2018 00:56
    EUR	4,2826	4,2926
    CHF	3,7837	3,7937
    GBP	4,7471	4,2926
    USD	3,7604	3,7704

    NBP	kurs średni

    DATA	nr 246/A/NBP/2018 z dnia 19-12-2018
    EUR	4,2846
    CHF	3,7875
    GBP	4,7607
    USD	3,7619

Aby użyć moduł Kursy Walut w swoim projekcie, wystarczy go zaimportować::

    import kursywalut

