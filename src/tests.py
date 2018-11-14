import pickle
import re


def __format_result(result):
    if int(result) == 1:
        result_name = "Hot"
    elif int(result_svm) == 0:
        result_name = "Neutral"
    else:
        result_name = "Cold"
    return result_name


trained_svm = pickle.load(open("trained-svm-algorithm.p", "rb"))
temp = [[10]]
result_svm = re.sub('[^0-9-]', '', str(trained_svm.predict(temp)))
result_svm_name = __format_result(result_svm)
print("For temperature: " + str(temp[0][0]) + " the SVM algorithm classified it as a " + result_svm_name + " temperature")

trained_knn = pickle.load(open("trained-knn-algorithm.p", "rb"))
temp = [[10]]
result_knn = re.sub('[^0-9-]', '', str(trained_knn.predict(temp)))
result_knn_name = __format_result(result_knn)
print("For temperature: " + str(temp[0][0]) + " the KNN algorithm classified it as a " + result_knn_name + " temperature")