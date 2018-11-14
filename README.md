# Temperature-classifier
Foi utilizado um data-set com 157 temperaturas coletadas da cidade de Campinas (SP) do período de 01/06/2018 até 04/11/2018.
As temperaturas maiores ou iguais a 22ºC e maior foram classificadas como temperaturas quentes, já as temperaturas entre 16ºC e 22ºC foram classificadas como neutras, e por último temperaturas abaixo de 16ºC foram classificadas como frias.

## Dados utilizados para treinar o algoritmo
![Dados utilizados para treinar o algoritmo](./src/resources/images/data-set.PNG)

## Confusion Matrix Knn algorithm
* Acurácia: 89%
* Base de validação do agente: ~30% do data-set
* Neighbors: 9
![Confusion Matrix KNN algorithm](./src/resources/images/confusion-matrix-knn.PNG)

## Confusion Matrix svm algorithm
* Acurácia: 92,5%
* Base de validação do agente: ~25% do data-set

![Confusion Matrix SVM algorithm](./src/resources/images/confusion-matrix-svm.PNG)

## Instalação de ambiente
### Update pip
.\venv\Scripts\python.exe -m pip install --upgrade pip --force-reinstall

### Update requirements
.\venv\Scripts\pip.exe freeze > requirements.txt

### Install requirements
.\venv\Scripts\pip3.6.exe install -r  requirements.txt