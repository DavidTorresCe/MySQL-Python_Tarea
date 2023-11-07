"""
Torres Celedon David Antonio 951
6 de Noviembre de 2023

Realizar una función que normalice los datos usando min-max
que reciba como parámetro un DataFrame y otro parámetro
que sea una lista de columnas a normalizar.
Retornar el DataFrame con los datos normalizados.

Realizar una función que normalice los datos usando Z-Score
que reciba como parámetro un DataFrame y otro parámetro
que sea una lista de columnas a normalizar.
Retornar el DataFrame con los datos normalizados.

Realizar una función que normalice los datos usando escalado simple
que reciba como parámetro un DataFrame y otro parámetro que
sea una lista de columnas a normalizar.
Retornar el DataFrame con los datos normalizados
"""
import pandas as pd

def min_max(value, lista):
    for i in lista:
        min_i = value[i].min()
        max_i = value[i].max()

        value[f"minmax_{i}"] = (value[i] - min_i)/(max_i - min_i)

    return value

def z_score(value, lista):
    for i in lista:
        prom = value[i].mean()
        std = value[i].std()

        value[f"z_score_{i}"] = (value[i] - prom) / std

    return value

def escalado_simple(value, lista):
    for i in lista:
        max_i = value[i].max()

        value[f"es_{i}"] = value[i]/max_i

    return value

df = pd.DataFrame({'A': [1, 2, 3, 4, 4],
                   'B': [5, 6, 7, 8, 8],
                   'C': [9, 10, 11, 12, 14]})

lista = ["A", "B", "C"]
df_normalizado = min_max(df, lista)
print(df_normalizado)

df_normalizado2 = z_score(df, lista)
print(df_normalizado2)

df_escalado = escalado_simple(df, lista)
print(df_escalado)