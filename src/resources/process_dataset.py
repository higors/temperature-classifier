import csv

import numpy as np


def execute(path):
    neutral_class = 0
    warm_class = 0
    cold_class = 0
    classes_name = ['Cold', 'Neutral', 'Warm']
    neutral_temperature = []
    warm_temperature = []
    cold_temperature = []
    temperatures = []
    labels = []
    with open(path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if float(row[4]) == -1:
                cold_class += 1
                cold_temperature.append(row[3])
                temperatures.append(row[3])

                labels.append(row[4])
            elif float(row[4]) == 1:
                warm_class += 1
                warm_temperature.append(row[3])
                temperatures.append(row[3])
                labels.append(row[4])
            else:
                neutral_class += 1
                neutral_temperature.append(row[3])
                temperatures.append(row[3])
                labels.append(row[4])

    temperatures = np.append([], temperatures)
    data_set_processed = {'temperatures': temperatures, 'labels': labels, 'classes_name': classes_name,
                          'neutral_class': neutral_class, 'warm_class': warm_class, 'cold_class': cold_class,
                          'neutral_temperature': neutral_temperature, 'warm_temperature': warm_temperature,
                          'cold_temperature': cold_temperature}
    return data_set_processed
