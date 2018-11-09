import matplotlib.pyplot as plt
import numpy as np


def plot_statistics(classes_names, class_one, class_two, class_three):
    y_pos = np.arange(len(classes_names))
    performance = [class_one, class_two, class_three]
    plt.bar(classes_names, performance, align='center', alpha=0.9)
    plt.xticks(y_pos, classes_names)
    plt.ylabel('Amount')
    plt.title('Amount per class ')
    plt.show()
