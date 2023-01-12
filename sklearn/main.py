import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB


languages = []
texts = []

for filename in os.listdir('dane'):  # wczytanie danych
    with open(os.path.join('dane', filename), 'r') as f:
        languages.append(filename.split('.')[0])
        texts.append(open(os.path.join('dane',filename)).read())


ngrams = CountVectorizer(ngram_range=(3, 3), analyzer='char') # stworzenie ngramow (3gramow)
processed_text = ngrams.fit_transform(texts)


perceptron = Perceptron()
perceptron.fit(processed_text, languages)

knn = KNeighborsClassifier()
knn.fit(processed_text, languages)

bayes = MultinomialNB() # naiwny klasyfikator bayesa
bayes.fit(processed_text, languages)


text_pol = "Ten tekst napisany jest po polsku. Zobaczmy, jak sobie z tym poradzi!"
text_eng = "This is a test text in English. Let us see how it goes!"
text_it = "Questo testo è in italiano. Vediamo cosa succede!"
text_de = "Dies ist ein Testtext in deutscher Sprache. Mal sehen was passiert!"
text_fi = "Tämä on suomenkielinen testiteksti. Katsotaan, mitä tapahtuu!"
text_spa = "Este es un texto de prueba en español. ¡Veamos qué pasa!"
text_fr = "Ce texte est rédigé en français. Voyons comment il gère ça!" # dodatkowy jezyk spoza puli


test_pol = ngrams.transform([text_pol])
test_eng = ngrams.transform([text_eng])
test_it = ngrams.transform([text_it])
test_de = ngrams.transform([text_de])
test_fi = ngrams.transform([text_fi])
test_spa = ngrams.transform([text_spa])
test_fr = ngrams.transform([text_fr])

print("NaiveBayes (pol):", bayes.predict(test_pol))
print("NaiveBayes (eng):", bayes.predict(test_eng))
print("NaiveBayes (it):", bayes.predict(test_it))
print("NaiveBayes (de):", bayes.predict(test_de))
print("NaiveBayes (fi):", bayes.predict(test_fi))
print("NaiveBayes (spa):", bayes.predict(test_spa))

print("NaiveBayes (fr):", bayes.predict(test_fr))


print("knn (pol):", knn.predict(test_pol))
print("knn (eng):", knn.predict(test_eng))
print("knn (it):", knn.predict(test_it))
print("knn (de):", knn.predict(test_de))
print("knn (fi):", knn.predict(test_fi))
print("knn (pol):", knn.predict(test_spa))
print("knn (fr):", knn.predict(test_fr))

print("knn:", knn.predict(test_fr))


print("Perceptron (pol):", perceptron.predict(test_pol))
print("Perceptron (eng):", perceptron.predict(test_eng))
print("Perceptron (it):", perceptron.predict(test_it))
print("Perceptron (de):", perceptron.predict(test_de))
print("Perceptron (fi):", perceptron.predict(test_fi))
print("Perceptron (pol):", perceptron.predict(test_spa))
print("Perceptron (spa):", perceptron.predict(test_fr))

print("Perceptron (fr):", perceptron.predict(test_fr))



