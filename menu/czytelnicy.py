lista_czytelnikow = []
hasla_czytelnikow = {}

import pickle

with open('dane_czytelnikow.pickle', 'rb') as czyt:
    lista_czytelnikow = pickle.load(czyt)
with open('hasla_czytelnikow.pickle', 'rb') as hasl:
    hasla_czytelnikow = pickle.load(hasl)
