import pickle
import numpy as np

import matplotlib.pyplot as plt
import process_dataset
from sklearn import svm
from sklearn.model_selection import train_test_split

import confusion_matrix

path = './csv/classified-temperatures.csv'

data_set_processed = process_dataset.execute(path)
# process_data_set.plot_statistics(data_set_processed['classes_name'], data_set_processed['cold_class'],
#                                 data_set_processed['neutral_class'], data_set_processed['warm_class'])


def train_svm_algorithm(temps, labels, classes_name):
    train_temperatures, test_temperatures, train_labels, test_labels = train_test_split(temps, labels,
                                                                                        test_size=0.25,
                                                                                        random_state=25)
    train_temperatures = train_temperatures.reshape(-1, 1)
    test_temperatures = test_temperatures.reshape(-1, 1)
    # create svm algorithm
    svm_classifier = svm.SVC(kernel='linear', C=1.0)

    # fit and serialize the algorithm svm
    trained_svm = svm_classifier.fit(np.array(train_temperatures), train_labels)
    pickle.dump(trained_svm, open("trained-svm-algorithm.p", "wb"))

    # validate the algorithm training
    classified_temperatures = trained_svm.predict(test_temperatures)

    np.set_printoptions(precision=2)
    plt.figure()
    confusion_matrix.execute(test_labels, classified_temperatures, classes=classes_name, title='Confusion Matrix')
    plt.show()
    print("Accuracy: %s" % svm_classifier.score(test_temperatures, test_labels))


train_svm_algorithm(data_set_processed['temperatures'], data_set_processed['labels'], data_set_processed['classes_name'])
