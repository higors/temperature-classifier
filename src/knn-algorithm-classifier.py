import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from src.resources import confusion_matrix, statistics, process_dataset

path = './resources/classified-temperatures.csv'
data_set_processed = process_dataset.execute(path)
statistics.plot_statistics(data_set_processed['classes_name'], data_set_processed['cold_class'],
                           data_set_processed['neutral_class'], data_set_processed['warm_class'])


def train_knn_algorithm(temps, all_labels, classes):
    train_temperatures, test_temperatures, train_labels, test_labels = train_test_split(temps, all_labels,
                                                                                        test_size=0.25,
                                                                                        random_state=25)
    train_temperatures = train_temperatures.reshape(-1, 1)
    test_temperatures = test_temperatures.reshape(-1, 1)
    # create knn algorithm
    knn_algorithm_classifier = KNeighborsClassifier(n_neighbors=3)

    # fit and serialize the algorithm knn
    trained_svm = knn_algorithm_classifier.fit(np.array(train_temperatures), train_labels)
    pickle.dump(trained_svm, open("trained-knn-algorithm.p", "wb"))

    # validate the algorithm training
    classified_temperatures = trained_svm.predict(test_temperatures)

    np.set_printoptions(precision=2)
    plt.figure()
    confusion_matrix.execute(test_labels, classified_temperatures, classes=classes, title='Confusion Matrix')
    plt.show()
    print("Accuracy: %s" % knn_algorithm_classifier.score(test_temperatures, test_labels))


train_knn_algorithm(data_set_processed['temperatures'], data_set_processed['labels'],
                    data_set_processed['classes_name'])
