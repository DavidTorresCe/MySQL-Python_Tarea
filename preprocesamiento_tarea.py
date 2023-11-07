"""
6 de noviembre de 2023
Torres Celedon David 951

Realizar una función que reciba como parámetro un DataFrame y
retorne el porcentaje de valores nulos de cada columna.


Realizar una función que reciba como parámetro un DataFrame y
retorne el número de renglones duplicados.


Realizar una función que reciba como parámetro un DataFrame y
un máximo porcentaje. Este debe eliminar todas las columnas que
superen o igualen el máximo porcentaje de valores nulos establecidos
en el DataFrame Original. Retornar la lista nombres de columnas eliminadas.
Validar que el porcentaje máximo esté entre 0 y 1.


Realizar una función que reciba como parámetro un DataFrame,
una lista con los nombres de las columnas a verificar y una cadena.
La cadena solo puede ser mean, bfill o ffill, en caso
contrario lanzar una excepción. Debe sustituir los valores nulos por
el método especificado y retornar el DataFrame modificado.


Realizar una función que reciba como parámetro un DataFrame y
elimine los renglones repetidos en el DataFrame Original.
Debe retornar la cantidad de renglones eliminados.

"""

import pandas as pd

datos = pd.read_csv("datasets/surveys.csv")

def porcentaje_nulos(value):
    nulos = value.isnull()
    porcentaje = nulos.sum()/len(value)
    print("el porcentaje de nulos de cada columna es: \n",porcentaje)

def duplicados(value):
    duplicados = value.drop_duplicates(subset=["sex", "weight"])
    print("La cantidad de valores duplicados es de: ",len(duplicados))

def nulos_eliminados(value, porcentaje):
    if porcentaje < 0 or porcentaje > 1:
        raise ValueError("El porcentaje debe estar entre 0 y 1")

    nulos_permitidos = porcentaje * len(value)

    eliminados = []
    for i in value.columns:
        if value[i].isna().sum() >= nulos_permitidos:
            eliminados.append(i)

    df = value.drop(eliminados, axis = 1)
    print("Las columnas eliminadas han sido: ", eliminados)
    print("Cantidad de columnas eliminadas: ",len(eliminados))
    print(df)


def sustitucion(dataframe, columnas, metodo):
    if metodo not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'")

    if metodo == 'mean':
        dataframe[columnas] = dataframe[columnas].fillna(dataframe[columnas].mean())
    elif metodo == 'bfill':
        dataframe[columnas] = dataframe[columnas].bfill()
    elif metodo == 'ffill':
        dataframe[columnas] = dataframe[columnas].ffill()

    return dataframe

def eliminar_duplicados(value):
    eliminar_duplicados = value.drop_duplicates(subset=["sex", "weight"])
    print("La cantidad de valores duplicados es de: ", len(eliminar_duplicados))




porcentaje_nulos(datos)
duplicados(datos)
nulos_eliminados(datos, 0.021)

lista = ["hindfoot_length", "weight"]
sustitucion(datos, lista, "mean")

eliminar_duplicados(datos)



