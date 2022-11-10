import pprint


# Funkcja build () na podstawie wprowadzonych wzorców konstruuje drzewo trie.
# Pobiera kolejne wzorce z tablicy wzorców i zaczynając od stanu 0 dodajemy odpowiednie krawędzie do trie
def build(patterns):
    # Każdy wpis w trie będzie zawierał 1.obecny stan, 2. znak, po którym prowadzi krawędź badanego vertexa,
    # 3. listę potomków/dzieci, 4. stan, do którego prowadzi failure link oraz 5. wzorzec na danej gałęzi drzewa trie
    trie.append({'state': 0, 'char': '', 'next': [], 'fail': 0, 'pattern': []})

    for pat in patterns:
        n = len(pat)
        state = 0  # domyślny stan
        character = 0
        child = next_state(state, pat[character])

        while child is not None:
            state = child
            character += 1

            # iterujemy po kolejnych znakach naszego wzorca
            if n > character:
                child = next_state(state, pat[character])
            else:
                break

        for c in range(character, n):
            trie[state]['next'].append(len(trie))
            vertex = {'state': len(trie), 'char': pat[c], 'next': [], 'fail': 0, 'pattern': []}  # tworzymy vertex
            trie.append(vertex)  # i dodajemy go do trie
            state = len(trie) - 1

        trie[state]['pattern'].append(pat)  # cały wzorzec dodajemy do trie
    # END for

    # dalszy fragment funkcji build () odpowiada za dodanie failure linków do gotowego drzewa trie
    # poprzez wykorzystanie przeszukiwania wszerz tworzone są kolejne failure linki w drzewie trie

    bfs1 = []

    for vertex in trie[0]['next']:  # vertexy bezpośrednio połączone z rootem otrzymują failure link na root
        trie[vertex]['fail'] = 0
        bfs1.append(vertex)  # dodajemy vertex do listy pomocniczej

    while bfs1:  # dopóki nie opróżnimy listy przeszukiwanych vertexów, będziemy kolejno:
        # 1.usuwać skrajny lewy element, 2.szukać jego dziecka, które następnie 3.dodamy do listy bfs2.
        # 4. zapamiętujemy aktualny stan (= zapamiętujemy drogę)
        # 5. jeżeli nie da się zajść dalej po failure linku dziecka, to zmieniamy stan na ten z fail

        bfs2 = bfs1.pop(0)  # 1.

        for kid in trie[bfs2]['next']:  # 2.
            bfs1.append(kid)  # 3.
            state = trie[bfs2]['fail']  # 4.

            while state != 0 and next_state(state, trie[kid]['char']) is None:  # 5.
                state = trie[state]['fail']

            trie[kid]['fail'] = next_state(state, trie[kid]['char'])

            if trie[kid]['fail'] is None:  # jeśli nie istnieje pasujący failure link od dziecka, to
                trie[kid]['fail'] = 0  # ustawiamy failure link na korzeń

    # END while

    print('')
    pprint.pprint(trie, sort_dicts=False)  # Wyświetla gotowe drzewo trie "ładniej" tzn. w osobnych linijkach

    # build END


########################################################################################################################

# sprawdzamy kolejne stany od naszego stanu i szukamy, czy jesteśmy w stanie przejść którymś z nich do przodu po
# konkretnym znaku
def next_state(state, char):
    for vertex in trie[state]['next']:
        if trie[vertex]['char'] == char:
            return vertex  # zwracamy pasujący nam vertex lub None, jeżeli żaden nie spełnia kryteriów
    return None
    # END next


########################################################################################################################

# Przeglądamy wprowadzony łańcuch znaków.
# Przechodzimy po odpowiednich stanach (next lub failure) i zapisujemy znalezione wzorce.
def search(text):
    state = 0
    found_patterns = []
    n = len(text)

    for x in range(n):  # iterujemy po kolejnych symbolach przeszukiwanego łańcucha znaków
        while state != 0 and next_state(state, text[x]) is None:
            # Sprawdzamy, czy nasz stan nie jest zerowy i czy
            # jednocześnie nie istnieje kolejny stan.
            state = trie[state]['fail']  # W takiej sytuacji przechodzimy przez failure link

        state = next_state(state, text[x])

        if state is not None:
            for y in trie[state]['pattern']:
                if x - len(y) + 1 > -1:  # zabezpieczenie przed ujemnymi indeksami
                    found_patterns.append({'ind': x - len(y) + 1, 'pattern': y})  # nasz końcowy wynik
                    # wyświetlamy początkowy indeks wystąpienia wzorca oraz znaleziony wzorzec
        else:
            state=0

    return found_patterns
    # END search
#

###################################################### MAIN ############################################################


trie = []

text_to_be_searched = input('\nWprowadź przeszukiwany ciąg znaków ')
pattern_array = []
print('')

while True:  # mechanizm dodawania kolejnych wzorców
    pattern = input('Podaj kolejny wzorzec ')

    if pattern == 'X':  # wprowadzenie 'X' jako wzorzec powoduje wyjście z pętli
        break
    pattern_array.append(pattern)
    # END while

print('\nWzorce: ', end='')
print(pattern_array)

build(pattern_array)  # wywołujemy metodę zbudowania drzewa trie na podstawie podanych wzorców

print('\nZnalezione wzorce: ')
pprint.pprint(search(text_to_be_searched))  # Wyświetla końcowy rezultat. Pprint, żeby wyświetliło w osobnych wierszach
