import pandas as pd

datos = pd.read_csv("datasets/surveys.csv")


def porcentaje_nulos(value):
    nulos = value.isnull()
    porcentaje = nulos.sum()/len(value)
    print("el porcentaje de nulos de cada columna es: \n",porcentaje)

def duplicados(value):
    eliminar_duplicados = value.drop_duplicates(subset=["sex", "weight"])
    print("La cantidad de valores duplicados es de: ",len(eliminar_duplicados))

def nulos_eliminados(value, porcentaje):
    if porcentaje < 0 or porcentaje > 1:
        raise ValueError("El porcentaje debe estar entre 0 y 1")

    nulos_permitidos = porcentaje * len(value)

    eliminados = []
    for i in value.columns:
        if value[i].isna().sum() >= nulos_permitidos:
            eliminados.append(i)

    df = datos.drop(eliminados, axis = 1)
    print("Las columnas eliminadas han sido: ", eliminados)
    print("Cantidad de columnas eliminadas: ",len(eliminados))
    print(df)

def sustitucion(value, lista, cadena):
    pass


porcentaje_nulos(datos)
duplicados(datos)
nulos_eliminados(datos, 0.031)

