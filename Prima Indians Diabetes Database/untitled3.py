# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:54:10 2022

@author: rodri
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression #libreria del modelo
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from warnings import simplefilter
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


simplefilter(action='ignore', category=FutureWarning)

url = 'diabetes.csv'
data = pd.read_csv(url)

#Tratamiento de los datos

data.Age.replace(np.nan, 33, inplace=True)
rangos = [0,18, 30, 48, 60, 88, 100]
nombres = ['1', '2', '3', '4', '5', '6']
data.Age = pd.cut(data.Age, rangos, labels=nombres)
data.drop(['DiabetesPedigreeFunction', 'BMI', 'Insulin', 'BloodPressure'], axis=1, inplace=True)

# Partir la data por la mitad (Media pa training y media pa testing)

data_train = data[:410]
data_test = data[410:]

x = np.array(data_train.drop(['Outcome'], 1))
y = np.array(data_train.Outcome) 


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

x_test_out = np.array(data_test.drop(['Outcome'], 1))
y_test_out = np.array(data_test.Outcome) 

# Regresión Logística

# Seleccionar un modelo
logreg = LogisticRegression(solver='lbfgs', max_iter = 7600)

# Entreno el modelo
logreg.fit(x_train, y_train)

# MÉTRICAS

print('*'*50)
print('Regresión Logística')

# Accuracy de Entrenamiento de Entrenamiento
print(f'accuracy de Entrenamiento de Entrenamiento: {logreg.score(x_train, y_train)}')

# Accuracy de Test de Entrenamiento
print(f'accuracy de Test de Entrenamiento: {logreg.score(x_test, y_test)}')

# Accuracy de Validación
print(f'accuracy de Validación: {logreg.score(x_test_out, y_test_out)}')

# MAQUINA DE SOPORTE VECTORIAL

# Seleccionar un modelo
svc = SVC(gamma='auto')

# Entreno el modelo
svc.fit(x_train, y_train)

# MÉTRICAS

print('*'*50)
print('Maquina de soporte vectorial')

# Accuracy de Entrenamiento de Entrenamiento
print(f'accuracy de Entrenamiento de Entrenamiento: {svc.score(x_train, y_train)}')

# Accuracy de Test de Entrenamiento
print(f'accuracy de Test de Entrenamiento: {svc.score(x_test, y_test)}')

# Accuracy de Validación
print(f'accuracy de Validación: {svc.score(x_test_out, y_test_out)}')

# ARBOL DE DECISIÓN

# Seleccionar un modelo
arbol = DecisionTreeClassifier()

# Entreno el modelo
arbol.fit(x_train, y_train)

# MÉTRICAS

print('*'*50)
print('Decisión Tree')

# Accuracy de Entrenamiento de Entrenamiento
print(f'accuracy de Entrenamiento de Entrenamiento: {arbol.score(x_train, y_train)}')

# Accuracy de Test de Entrenamiento
print(f'accuracy de Test de Entrenamiento: {arbol.score(x_test, y_test)}')

# Accuracy de Validación
print(f'accuracy de Validación: {arbol.score(x_test_out, y_test_out)}')

# RANDOM FOREST

ranforest = RandomForestClassifier()

# Entrenar el modelo
ranforest.fit(x_train, y_train)

# Metricas

print('*'*50)
print('Random Forest')


# Accuracy de Entrenamiento de Entrenamiento
print(f'accuracy de Entrenamiento de Entrenamiento: {ranforest.score(x_train, y_train)}')

# Accuracy de Test de Entrenamiento
print(f'accuracy de Test de Entrenamiento: {ranforest.score(x_test, y_test)}')

# Accuracy de Validación
print(f'accuracy de Validación: {ranforest.score(x_test_out, y_test_out)}')