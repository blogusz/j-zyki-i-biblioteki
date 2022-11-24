import pprint


def sort_dict_by_value(d, reverse=False):  # funkcja sortująca słownik względem liczby wystąpień słów
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def unique_words(dictio, number):  # funkcja pracującą na uporządkowanym słowniku wyświetla 'number' pierwszych słów (wartości, bo dla remisów wyświetla więcej)
    # print(dictio)
    counter = 0
    licznik = 1
    i = 0
    j = 1
    xyz = list(dictio.values())
    abc = list(dictio.keys())

    length = len(xyz)

    # print(xyz)
    print(abc)
    # print(length)

    while licznik <= number and j < length:  # licznik pilnuje, żeby nie przekroczyć wartości 'number' pierwszych slow
        if xyz[i] == xyz[j]:  # liczba wystąpień kolejnych dwóch słów jest równa
            counter += 1  # counter zapamiętuje o ile więcej słów trzeba wydrukować
            i += 1
            j += 1
        else:
            # i += 1
            # j += 1
            i = j
            j = i + 1
            licznik += 1

    # print(counter)

    first_n_pairs = {element: dictio[element] for element in list(dictio.keys())[:number + counter]}  # ustalamy pierwsze 'number' + counter najczęstszych slow
    pprint.pprint(first_n_pairs, sort_dicts=False)


################# MAIN #################

my_file = open('Potop.txt', 'r', encoding='utf8')  # odczytujemy plik z odpowiednim kodowaniem

zbanowane_znaki = [',', '.', '?', ':', ';', '(', ')', '!', '*', '-', '\"', '\'']  # lista symboli, których raczej nie chcemy mieć w naszym słowie

tekst = my_file.read()
tekst_list = tekst.split()

liczba_wystapien = {}


for word in tekst_list:  # 'obieramy' po kolei każde słowu w pliku
    if word[-1] in zbanowane_znaki:  # ostatnia litera w słowie jest zbanowanym znakiem
        try:
            while word[-1] in zbanowane_znaki:  # usuwamy wszystkie zbanowane znaki z końca słowa
                word = word[:-1]
        except IndexError:
            continue
    if word[0] in zbanowane_znaki:  # pierwsza litera w słowie jest zbanowanym znakiem
        try:
            while word[0] in zbanowane_znaki:  # usuwamy wszystkie zbanowane znaki z początku
                word = word[1:]
        except IndexError:
            continue

    word = word.lower()  # ustawiamy małe litery
    liczba_wystapien.setdefault(word, 0)  # domyślnie każde słowo startuje z zerową liczbą wystąpień
    liczba_wystapien[word] += 1

dictionary = sort_dict_by_value(liczba_wystapien, True)  # sortujemy nasz otrzymany słownik

unique_words(dictionary, 15)  # wywołujemy funkcję na gotowym słowniku
