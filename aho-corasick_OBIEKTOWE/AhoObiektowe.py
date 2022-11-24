import pprint


class AhoCorasick:

    def __init__(self):
        self.patterns = None
        self.trie = [{'state': 0, 'char': '', 'next': [], 'fail': 0, 'pattern': []}]
        # self.trie = []
        # self.trie.append({'state': 0, 'char': '', 'next': [], 'fail': 0, 'pattern': []})

    def build(self, patterns_array):  # funkcja budującą drzewo wykorzystuje tablicę wzorców
        self.patterns = patterns_array

        for pat in self.patterns:
            n = len(pat)
            state = 0
            character = 0
            child = self.next_state(state, pat[character])

            while child is not None:
                state = child
                character += 1

                if n > character:
                    child = self.next_state(state, pat[character])
                else:
                    break

            for c in range(character, n):
                self.trie[state]['next'].append(len(self.trie))
                vertex = {'state': len(self.trie), 'char': pat[c], 'next': [], 'fail': 0, 'pattern': []}
                self.trie.append(vertex)
                state = len(self.trie) - 1

            self.trie[state]['pattern'].append(pat)

        # poniższy fragment odpowiedzialny jest za stworzenie failurelinków
        bfs1 = []

        for vertex in self.trie[0]['next']:
            self.trie[vertex]['fail'] = 0
            bfs1.append(vertex)

        while bfs1:

            bfs2 = bfs1.pop(0)

            for kid in self.trie[bfs2]['next']:
                bfs1.append(kid)
                state = self.trie[bfs2]['fail']

                while state != 0 and self.next_state(state, self.trie[kid]['char']) is None:
                    state = self.trie[state]['fail']

                self.trie[kid]['fail'] = self.next_state(state, self.trie[kid]['char'])

                if self.trie[kid]['fail'] is None:
                    self.trie[kid]['fail'] = 0

    def next_state(self, state, char):  # funkcja szukającą następników węzłów
        for vertex in self.trie[state]['next']:
            if self.trie[vertex]['char'] == char:
                return vertex
        return None

    def __repr__(self):
        #pprint.pprint(self.trie, sort_dicts=False)
        #print('')
        rep = self.trie
        return rep

    @staticmethod
    def text_to_work_on():
        tekst = input('\nWprowadź przeszukiwany ciąg znaków ')
        return tekst

    def search(self, tekst):  # funkcja przeszukującą wprowadzony tekst
        state = 0
        found_patterns = []
        n = len(tekst)

        for x in range(n):
            while state != 0 and self.next_state(state, tekst[x]) is None:
                state = self.trie[state]['fail']

            state = self.next_state(state, tekst[x])

            if state is not None:
                for y in self.trie[state]['pattern']:
                    if x - len(y) + 1 > -1:
                        found_patterns.append({'ind': x - len(y) + 1, 'pattern': y})
            else:
                state = 0

        return pprint.pprint(found_patterns)

    @staticmethod
    def create_patterns():  # funkcja tworząca tablicę wykorzystywanych wzorców
        pattern_array = []
        while True:
            pattern = input('Podaj kolejny wzorzec ')

            if pattern == 'END':
                break
            pattern_array.append(pattern)
        return pattern_array


######################### MAIN #########################

ahocorasick = AhoCorasick()  # tworzymy obiekt ahocorasick z klasy AhoCorasick

patterns = ahocorasick.create_patterns()  # tworzymy tablicę wzorców
ahocorasick.build(patterns)  # budujemy drzewo wykorzystując naszą tablicę wzorców

print('')
print(ahocorasick.__repr__())

text = ahocorasick.text_to_work_on()  # wprowadzamy tekst do przeszukania
ahocorasick.search(text)  # przeszukujemy wprowadzony tekst
