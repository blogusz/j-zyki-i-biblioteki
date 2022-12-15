import pickle
import pprint
from datetime import datetime
from datetime import timedelta

import bibliotekarze
import czytelnicy
import katalog


def menu_czytelnik(czytelnik):
    print('\n[1] Wypożycz')
    print('[2] Zarezerwuj')
    print('[3] Przedluż')
    print('[4] Przeglądaj katalog')
    print('[0] Wyloguj')

    try:
        wybor = int(input('Wybierz opcję: '))

        while wybor != 0:
            if wybor == 0:
                logowanie()
            elif wybor == 1:
                czytelnik.wypozycz()
            elif wybor == 2:
                czytelnik.zarezerwuj()
            elif wybor == 3:
                czytelnik.przedluz()
            elif wybor == 4:
                czytelnik.przegladaj()
            else:
                print('Nieprawidłowa komenda')

            print('\n[1] Wypożycz')
            print('[2] Zarezerwuj')
            print('[3] Przedluz')
            print('[4] Przeglądaj katalog')
            print('[0] Wyloguj')
            wybor = int(input('Wybierz opcję: '))

        if wybor == 0:
            logowanie()
    except ValueError:
        menu_czytelnik(czytelnik)


def menu_bibliotekarz(identyfikator):
    print('\n[1] Przyjmij zwrot')
    print('[2] Dodaj książkę do katalogu')
    print('[3] Usun książkę z katalogu')
    print('[4] Dodaj czytelnika')
    print('[5] Usuń czytelnika')
    print('[6] Przeglądaj katalog')
    print('[7] Wyświetl aktywne rezerwacje')
    print('[8] Anuluj rezerwację')
    print('[0] Wyloguj')
    try:
        wybor = int(input('Wybierz opcję: '))

        while wybor != 0:
            if wybor == 0:
                logowanie()
            elif wybor == 1:
                identyfikator.przyjmij_zwrot()
            elif wybor == 2:
                identyfikator.dodaj_ksiazke()
            elif wybor == 3:
                identyfikator.usun_ksiazke()
            elif wybor == 4:
                identyfikator.dodaj_czytelnika()
            elif wybor == 5:
                identyfikator.usun_czytelnika()
            elif wybor == 6:
                identyfikator.przegladaj()
            elif wybor == 7:
                identyfikator.wyswietl_aktywne_rezerwacje()
            elif wybor == 8:
                identyfikator.anuluj_rezerwacje()
            else:
                print('Nieprawidłowa komenda')

            print('\n[1] Przyjmij zwrot')
            print('[2] Dodaj książkę do katalogu')
            print('[3] Usuń książkę z katalogu')
            print('[4] Dodaj czytelnika')
            print('[5] Usuń czytelnika')
            print('[6] Przeglądaj katalog')
            print('[7] Wyświetl aktywne rezerwacje')
            print('[8] Anuluj rezerwację')
            print('[0] Wyloguj')
            wybor = int(input('Wybierz opcję: '))

        if wybor == 0:
            logowanie()

    except ValueError:
        menu_bibliotekarz(identyfikator)


class czytelnik:  # klasa zawierająca imię, nazwisko oraz definicje funkcji dostępnych dla czytelnika
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def wypozycz(self):  # jeżeli tytuł znajduje się w katalogu i jest dostępny, to możemy go wypożyczyć
        tytul = input('\nPodaj tytuł książki, którą chcesz wypożyczyć: ')

        if tytul in katalog.ksiazki.keys():
            if str(katalog.ksiazki[tytul]['dostepnosc']) == 'tak':
                try:
                    if int(katalog.rezerwacje[tytul]['czy_zarezerwowane']) == 0 \
                            or str(katalog.rezerwacje[tytul]['imie_rezerwujacego']) == self.imie \
                            and str(katalog.rezerwacje[tytul]['nazwisko_rezerwujacego']) == self.nazwisko:
                        print(f'Udało się wypożyczyć książkę: {tytul}')
                        katalog.rezerwacje.pop(tytul)
                except KeyError:
                    print(f'Udało się wypożyczyć książkę: {tytul}')
                    katalog.ksiazki[tytul]['dostepnosc'] = 'nie'
                else:
                    print('Niestety książka jest juz zarezerwowana.')
                    print(katalog.rezerwacje[tytul])
            else:
                print('Niestety książka nie jest aktualnie dostępna.')
        else:
            print(f'{tytul} nie znajduje się w katalogu.')

    def zarezerwuj(self):  # jeżeli książka jest w katalogu i nie jest wypozyczona,to ją rezerwujemy. Jeżeli jest
        # zarezerwowana przez kogoś innego, to sprawdzamy, czy data ich rezerwacji już nie minęła.
        temp = katalog.rezerwacje
        zawartosc = {}
        tytul = input('\nPodaj tytuł szukanej książki: ')
        if tytul in katalog.ksiazki:
            dzisiejsza_data = datetime.now()
            czas_rezerwacji = timedelta(days=31)
            if tytul not in katalog.rezerwacje:

                zawartosc['czy_zarezerwowane'] = '1'
                zawartosc['rezerwacja do'] = dzisiejsza_data + czas_rezerwacji
                zawartosc['imie_rezerwujacego'] = self.imie
                zawartosc['nazwisko_rezerwujacego'] = self.nazwisko
                katalog.ksiazki[tytul]['dostepnosc'] = 'nie'

                temp[tytul] = zawartosc
                katalog.rezerwacje = temp
                print(tytul, 'została zarezerwowana.')
                print(katalog.rezerwacje[tytul])

            else:
                if katalog.rezerwacje[tytul]['rezerwacja do'] < dzisiejsza_data:
                    temp[tytul] = zawartosc
                    katalog.rezerwacje = temp
                    zawartosc['czy_zarezerwowane'] = '1'
                    zawartosc['rezerwacja do'] = dzisiejsza_data + czas_rezerwacji
                    zawartosc['imie_rezerwujacego'] = self.imie
                    zawartosc['nazwisko_rezerwujacego'] = self.nazwisko
                    katalog.ksiazki[tytul]['dostepnosc'] = 'nie'

                    print(tytul, 'została zarezerwowana.')
                else:
                    print(f'Niestety książka jest już zarezerwowana')

        else:
            print(f'{tytul} nie znajduje się w katalogu')

    def przedluz(self):  # wyświetlamy nasze rezerwacje, wybieramy jedną i przedłużamy ją o 14 dni.
        czas_przedluzenia = timedelta(days=14)
        for rezerwacja in katalog.rezerwacje:
            if str(katalog.rezerwacje[rezerwacja]['imie_rezerwujacego']) == self.imie \
                    and str(katalog.rezerwacje[rezerwacja]['nazwisko_rezerwujacego']) == self.nazwisko:
                print(rezerwacja, end=':')
                print(katalog.rezerwacje[rezerwacja])

        wybor = input('Wybierz książkę, której rezerwację chcesz przedłużyć: ')
        for rezerwacja in katalog.rezerwacje:
            if str(katalog.rezerwacje[rezerwacja]['imie_rezerwujacego']) == self.imie \
                    and str(katalog.rezerwacje[rezerwacja]['nazwisko_rezerwujacego']) == self.nazwisko:
                if str(wybor) == str(rezerwacja):
                    termin = datetime.strptime(katalog.rezerwacje[rezerwacja]['rezerwacja do'], "%y/%m/%d %H:%M:%S.%f")
                    katalog.rezerwacje[rezerwacja]['rezerwacja do'] = termin + czas_przedluzenia
                    with open('baza_rezerwacji.pickle', 'wb') as rezerw:
                        pickle.dump(katalog.rezerwacje, rezerw)

    def przegladaj(self):
        print('\n[1] Wyszukaj po tytule')
        print('[2] Wyszukaj po autorze')
        print('[3] Wyszukaj po słowach kluczowych')
        print('[4] Wyświetl cały katalog')
        print('[0] Powrót')
        try:
            wybor = int(input('Wybierz opcję: '))

            while wybor != 0:
                if wybor == 0:
                    break
                elif wybor == 1:
                    tytul = input('Podaj szukany tytuł: ')
                    if tytul in katalog.ksiazki.keys():
                        print(katalog.ksiazki[tytul])
                elif wybor == 2:
                    autor = input('Podaj szukanego autora: ')
                    slowo = ''
                    for tytuly in katalog.ksiazki.keys():
                        for klucze in katalog.ksiazki[tytuly]['autor']:
                            slowo += klucze
                        if slowo == autor:
                            print(katalog.ksiazki[tytuly])
                            break
                        else:
                            slowo = ''
                elif wybor == 3:
                    slowo_klucz = input('Podaj słowo kluczowe: ')
                    slowa_kluczowe = ''
                    for tytuly in katalog.ksiazki.keys():
                        for klucze in katalog.ksiazki[tytuly]['slowa kluczowe']:
                            slowa_kluczowe += klucze
                        if slowo_klucz in katalog.ksiazki[tytuly]['slowa kluczowe']:
                            print(katalog.ksiazki[tytuly])
                        else:
                            slowa_kluczowe = ''
                elif wybor == 4:
                    pprint.pprint(katalog.ksiazki, sort_dicts=False)
                else:
                    print('Nieprawidłowa komenda')

                print('\n[1] Wyszukaj po tytule')
                print('[2] Wyszukaj po autorze')
                print('[3] Wyszukaj po słowach kluczowych')
                print('[4] Wyświetl cały katalog')
                print('[0] Powrót')
                wybor = int(input('Wybierz opcję: '))

            if wybor == 0:
                pass
        except ValueError:
            self.przegladaj()


class bibliotekarz:  # klasa zawierająca identyfikator pracownika (ja przyjąłem, że jest to dowolny ciąg cyfr, np. 1337)
    def __init__(self, identyfikator):
        self.identyfikator = identyfikator

    def przyjmij_zwrot(
            self):  # przyjmujemy zwort i jeżeli jest na niego rezerwacja, to 'dostępnośc' dalej jest równa 'nie'
        tytul = input('Podaj tytuł zwracanej książki: ')
        print(katalog.ksiazki[tytul])
        try:
            if str(katalog.ksiazki[tytul]['dostepnosc']) == 'nie':
                try:
                    if str(katalog.rezerwacje[tytul]['czy_zarezerwowane']) == '0':
                        katalog.ksiazki[tytul]['dostepnosc'] = 'tak'
                        print(f'Zwrócono {tytul}')
                    else:
                        print(katalog.rezerwacje[tytul])
                        print(f'Zwrócono {tytul}. Jest na niego rezerwacja.')
                except KeyError:
                    katalog.ksiazki[tytul]['dostepnosc'] = 'tak'
                    print(f'Zwrócono {tytul}')
            else:
                print('Książka została już zwrócona.')
        except ValueError:
            self.przyjmij_zwrot()

    def dodaj_ksiazke(self):
        temp = katalog.ksiazki
        wnetrze_temp = {}
        tytul = input('Wprowadź tytuł książki: ')
        if tytul not in katalog.ksiazki:
            autor = input('Wprowadź autora książki: ')
            slowa_kluczowe = []
            while True:
                slowo_klucz = input('Wprowadź słowo kluczowe książki: ')
                if slowo_klucz != '' and slowo_klucz != ' ' and slowo_klucz is not None:
                    slowa_kluczowe.append(slowo_klucz)
                else:
                    break
            wnetrze_temp['tytul'] = tytul
            wnetrze_temp['autor'] = autor
            wnetrze_temp['slowa kluczowe'] = slowa_kluczowe
            wnetrze_temp['dostepnosc'] = 'tak'

            temp[tytul] = wnetrze_temp
            katalog.ksiazki = temp
            print(temp[tytul])
        else:
            print(f'{tytul} znajduje się już w katalogu.')

    def usun_ksiazke(self):
        print(katalog.ksiazki.keys())
        tytul = input('Wprowadź tytuł książki do usunięcia: ')
        if tytul in katalog.ksiazki:
            wybor = input(f'Czy na pewno chcesz usunąć {tytul} z katalogu? [tak/nie]: ')
            if str(wybor) == 'tak':
                katalog.ksiazki.pop(tytul)
        else:
            print(f'{tytul} nie znajduje się w katalogu.')

    def dodaj_czytelnika(self):  # dodajemy czytelnika po imienu, nawisku i ustalamy jego hasło
        imie = input('Podaj imię dodawanej osoby: ')
        nazwisko = input('Podaj nazwisko dodawanej osoby: ')
        osoba = imie + ' ' + nazwisko

        if osoba not in czytelnicy.lista_czytelnikow:
            haslo = input('Wprowadź hasło, które zostanie przypisane do tego konta: ')
            czytelnicy.hasla_czytelnikow[osoba] = haslo
            czytelnicy.lista_czytelnikow.append(osoba)
        else:
            print(f'{osoba} znajduje się już w systemie.')

    def usun_czytelnika(self):  # usuwamy czytelnika oraz zmieniamy odpowiednio wartości powiązanych z nim wypozyczeń
        # i rezerwacji
        print(czytelnicy.lista_czytelnikow)
        imie = input('Podaj imię usuwanej osoby: ')
        nazwisko = input('Podaj nazwisko usuwanej osoby: ')
        osoba = imie + ' ' + nazwisko

        if osoba in czytelnicy.lista_czytelnikow:
            wybor = input('Czy na pewno chcesz usunąć użytkownika? [tak/nie]')
            do_usuniecia = []
            if str(wybor) == 'tak':
                for rezerwacja in katalog.rezerwacje:
                    if str(katalog.rezerwacje[rezerwacja]['imie_rezerwujacego']) == imie \
                            and str(katalog.rezerwacje[rezerwacja]['nazwisko_rezerwujacego']) == nazwisko:
                        do_usuniecia.append(rezerwacja)
                print(katalog.rezerwacje.keys())
                for element in do_usuniecia:
                    if element in katalog.rezerwacje.keys():
                        katalog.rezerwacje.pop(element)
                        katalog.ksiazki[element]['dostepnosc'] = 'tak'
                czytelnicy.lista_czytelnikow.remove(osoba)
                czytelnicy.hasla_czytelnikow.pop(osoba)

                print(f'{osoba} został usunięty z systemu.')

            elif str(wybor) == 'nie':
                pass
            else:
                print('Błędna komenda. ')
        else:
            print(f'{osoba} nie znajduje się w systemie.')

    def przegladaj(self):
        try:
            print('\n[1] Wyszukaj po tytule')
            print('[2] Wyszukaj po autorze')
            print('[3] Wyszukaj po słowach kluczowych')
            print('[4] Wyświetl cały katalog')
            print('[0] Powrót')
            opcja = int(input('Wybierz opcję: '))

            while opcja != 0:
                if opcja == 0:
                    break
                elif opcja == 1:
                    tytul = input('Podaj szukany tytuł: ')
                    if tytul in katalog.ksiazki.keys():
                        print(katalog.ksiazki[tytul])
                elif opcja == 2:
                    autor = input('Podaj szukanego autora: ')
                    slowo = ''
                    for tytuly in katalog.ksiazki.keys():
                        for klucze in katalog.ksiazki[tytuly]['autor']:
                            slowo += klucze
                        if slowo == autor:
                            print(katalog.ksiazki[tytuly])
                            break
                        else:
                            slowo = ''
                elif opcja == 3:
                    slowo_klucz = input('Podaj słowo kluczowe: ')
                    slowa_kluczowe = ''
                    for tytuly in katalog.ksiazki.keys():
                        for klucze in katalog.ksiazki[tytuly]['slowa kluczowe']:
                            slowa_kluczowe += klucze
                        if slowo_klucz in katalog.ksiazki[tytuly]['slowa kluczowe']:
                            print(katalog.ksiazki[tytuly])
                        else:
                            slowa_kluczowe = ''
                elif opcja == 4:
                    pprint.pprint(katalog.ksiazki, sort_dicts=False)
                else:
                    print('Nieprawidłowa komenda')

                print('\n[1] Wyszukaj po tytule')
                print('[2] Wyszukaj po autorze')
                print('[3] Wyszukaj po słowach kluczowych')
                print('[4] Wyświetl cały katalog')
                print('[0] Powrót')
                opcja = int(input('Wybierz opcję: '))

            if opcja == 0:
                pass

        except ValueError:
            self.przegladaj()

    def wyswietl_aktywne_rezerwacje(self):
        pprint.pprint(katalog.rezerwacje, sort_dicts=False)

    def anuluj_rezerwacje(self):
        print(katalog.rezerwacje)
        imie = input('Podaj imię osoby połączonej z anulowaną rezerwacją: ')
        nazwisko = input('Podaj nazwisko osoby połączonej z anulowaną rezerwacją: ')
        osoba = imie + ' ' + nazwisko

        if osoba in czytelnicy.lista_czytelnikow:
            for rezerwacja in katalog.rezerwacje:
                if str(katalog.rezerwacje[rezerwacja]['imie_rezerwujacego']) == imie \
                        and str(katalog.rezerwacje[rezerwacja]['nazwisko_rezerwujacego']) == nazwisko:
                    print(rezerwacja, end=':')
                    print(katalog.rezerwacje[rezerwacja])
            wybor = input('Podaj tytuł, którego rezerwację chcesz anulować: ')
            katalog.rezerwacje.pop(wybor)


def logowanie():  # logujemy się albo jako użytkownik albo pracownik biblioteki
    print('\n[1] Zaloguj sie jako czytelnik')
    print('[2] Zaloguj sie jako pracownik')
    print('[0] Wyjście')

    try:
        log = int(input('>>'))

        if log == 1:
            # print(czytelnicy.lista_czytelnikow)
            # print(czytelnicy.hasla_czytelnikow)

            imie = input('Podaj swoje imie: ')
            nazwisko = input('Podaj swoje nazwisko: ')
            czyt = czytelnik(imie, nazwisko)
            osob = imie + ' ' + nazwisko

            if osob not in czytelnicy.lista_czytelnikow:
                czy_nowe_konto = input(
                    'Nie znaleziono konta powiązanego z wprowadzonymi danymi. Czy chcesz założyć nowe konto? [tak/nie]: ')
                if str(czy_nowe_konto) == 'tak':
                    zakladanie_konta_czytelnika(osob)
                else:
                    logowanie()
            else:
                haslo = input('Wprowadz haslo do swojego konta: ')
                if haslo == czytelnicy.hasla_czytelnikow.get(osob):
                    menu_czytelnik(czyt)
                else:
                    print('Nieprawidlowe haslo')
                    logowanie()
        if log == 2:
            # print(bibliotekarze.lista_pracownikow)
            # print(bibliotekarze.hasla_pracownikow)
            identyfikator = input('Podaj identyfikator: ')
            bib = bibliotekarz(identyfikator)
            bibl = identyfikator
            if bibl not in bibliotekarze.lista_pracownikow:
                czy_nowe_konto = input(
                    'Nie znaleziono konta powiązanego z wprowadzonym identyfikatorem. Czy chcesz założyć nowe konto? [tak/nie]: ')
                if str(czy_nowe_konto) == 'tak':
                    zakladanie_konta_bibliotekarza(bibl)
                else:
                    logowanie()
            else:
                haslo = input('Wprowadź haslo do swojego konta: ')
                if haslo == bibliotekarze.hasla_pracownikow.get(bibl):
                    menu_bibliotekarz(bib)
                else:
                    print('Nieprawidlowe haslo')
                    logowanie()
        if log == 0:  # zapisanie danych na dysk
            with open('baza_rezerwacji.pickle', 'wb') as rezerw:
                pickle.dump(katalog.rezerwacje, rezerw)
            with open('baza_ksiazek.pickle', 'wb') as ksiaz:
                pickle.dump(katalog.ksiazki, ksiaz)
            with open('dane_czytelnikow.pickle', 'wb') as czytel:
                pickle.dump(czytelnicy.lista_czytelnikow, czytel)
            with open('hasla_czytelnikow.pickle', 'wb') as hasl:
                pickle.dump(czytelnicy.hasla_czytelnikow, hasl)
            with open('pracownicy.pickle', 'wb') as prac:
                pickle.dump(bibliotekarze.lista_pracownikow, prac)
            with open('hasla_pracownikow.pickle', 'wb') as hasl_prac:
                pickle.dump(bibliotekarze.hasla_pracownikow, hasl_prac)
            exit(0)
    except ValueError:
        logowanie()


def zakladanie_konta_czytelnika(osoba):
    haslo = input('Wprowadz hasło, które zostanie przypisane do twojego konta: ')
    czytelnicy.hasla_czytelnikow[osoba] = haslo
    # print(czytelnicy.hasla_czytelnikow)
    czytelnicy.lista_czytelnikow.append(osoba)
    logowanie()


def zakladanie_konta_bibliotekarza(identyfikator):
    haslo = input('Wprowadź hasło, które zostanie przypisane do twojego konta: ')
    bibliotekarze.hasla_pracownikow[identyfikator] = haslo
    # print(bibliotekarze.hasla_pracownikow)

    bibliotekarze.lista_pracownikow.append(identyfikator)
    logowanie()


if __name__ == "__main__":
    # with open ('baza_rezerwacji.pickle', 'wb') as rezerw1:
    #     pickle.dump(katalog.rezerwacje, rezerw1)
    # with open('baza_ksiazek.pickle', 'wb') as rezerw1:
    #     pickle.dump(katalog.ksiazki, rezerw1)
    # with open('dane_czytelnikow.pickle', 'wb') as czytel1:
    #     pickle.dump(czytelnicy.lista_czytelnikow, czytel1)
    # with open('hasla_czytelnikow.pickle', 'wb') as hasl1:
    #     pickle.dump(czytelnicy.hasla_czytelnikow, hasl1)
    # with open('pracownicy.pickle', 'wb') as p1:
    #     pickle.dump(bibliotekarze.lista_pracownikow, p1)
    # with open('hasla_pracownikow.pickle', 'wb') as p2:
    #     pickle.dump(bibliotekarze.hasla_pracownikow, p2)

    with open('baza_rezerwacji.pickle', 'rb') as rezerw2:  # wczytywanie danych z dysku
        katalog.rezerwacje = pickle.load(rezerw2)
    with open('baza_ksiazek.pickle', 'rb') as rezerw2:
        katalog.ksiazki = pickle.load(rezerw2)
    with open('dane_czytelnikow.pickle', 'rb') as czytel2:
        czytelnicy.lista_czytelnikow = pickle.load(czytel2)
    with open('hasla_czytelnikow.pickle', 'rb') as hasl2:
        czytelnicy.hasla_czytelnikow = pickle.load(hasl2)
    with open('pracownicy.pickle', 'rb') as czyt:
        bibliotekarze.lista_pracownikow = pickle.load(czyt)
    with open('hasla_pracownikow.pickle', 'rb') as czyt:
        bibliotekarze.hasla_pracownikow = pickle.load(czyt)

    print('\n\nPROSZĘ SIĘ NAJPIERW ZAPOZNAĆ Z readme.txt!\n')
    logowanie()
