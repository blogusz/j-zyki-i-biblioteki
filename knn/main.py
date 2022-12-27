import numpy as np
import math as m


def euclidean(train, test):
    distance = 0.0

    for x in range(len(train) - 1):
        distance += (train[x] - test[x]) ** 2
    distance = m.sqrt(distance)

    return distance


def taxicab(train, test):
    distance = 0.0

    for x in range(len(train) - 1):
        distance += abs(train[x] - test[x])
    return distance


def maximum(train, test):
    distance = 0.0
    for x in range(len(train) - 1):
        distance = max(abs(train[x] - test[x]), distance)
    return distance


def cosine(train, test):
    distance = np.dot(train[:-1], test) / (np.linalg.norm(train[:-1])) + np.linalg.norm(test)
    return distance


class knn:

    def __init__(self, k, data_set):
        self.k = k
        self.data_set = data_set
        # self.metric=metric

    def train(self, train):
        for row in train:
            self.data_set.append(row)

    def predict(self, data_set, distance):
        if distance == 'euclidean':
            distance = euclidean
        elif distance == 'taxicab':
            distance = taxicab
        elif distance == 'maximum':
            distance = maximum
        elif distance == 'cosine':
            distance = cosine
        else:
            exit(1)

        neighbors = []

        # brak pomysłu na zadanie :(

        return neighbors


if __name__ == "__main__":
    train_set = [[1.235664, 0.954321, 0],
                 [7.12121, 5.432345, 1],
                 [5.0086, 5.432345, 0.5],
                 [2.312312, 0.321312, 0]]

    dataset = [[2.7810836, 2.550537003, 0],
               [1.465489372, 2.362125076, 0],
               [3.396561688, 4.400293529, 0],
               [1.38807019, 1.850220317, 0],
               [3.06407232, 3.005305973, 0],
               [7.627531214, 2.759262235, 1],
               [5.332441248, 2.088626775, 1],
               [6.922596716, 1.77106367, 1],
               [8.675418651, -0.242068655, 1],
               [7.673756466, 3.508563011, 1]]

    test = knn(1, list(dataset))
    test.train(train_set)

    print(test.predict([[3.56, 1.0], [2.2, 0.5], [1.11, 0.0]], 'euclidean'))
    print(test.predict([[3.56, 1.0], [2.2, 0.5], [1.11, 0.0]], 'taxicab'))
    print(test.predict([[3.56, 1.0], [2.2, 0.5], [1.11, 0.0]], 'maximum'))
    print(test.predict([[3.56, 1.0], [2.2, 0.5], [1.11, 0.0]], 'cosine'))
    print('ZADANIE NIE JEST SKOŃCZONE')
