lista_pracownikow = []
hasla_pracownikow = {}

import pickle

with open('pracownicy.pickle', 'rb') as czyt:
    lista_pracownikow = pickle.load(czyt)
with open('hasla_pracownikow.pickle', 'rb') as hasl:
    hasla_pracownikow = pickle.load(hasl)
