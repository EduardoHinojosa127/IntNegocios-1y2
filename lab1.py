import pandas as pd

# Nombre del archivo CSV generado
nombre_archivo = "Panamericanos_Lima.csv"

# Leer el archivo CSV y cargarlo en un DataFrame
df = pd.read_csv(nombre_archivo)

#Estas listas contienen los numeros de la primera fila y columna
primera_columna = df.iloc[:, 2].tolist()
columnas_desde_tercera_hasta_sexta = df.iloc[:, 2:4]
# Imprimir los datos
print(df)
print("-------------------------------------")
print("Sumatoria de tercera columna: ",sum(primera_columna))
print("-------------------------------------")
print("Cantidad de elementos del dataframe: ",df.size)
print("-------------------------------------")
print("Media del dataframe: ", columnas_desde_tercera_hasta_sexta.mean().mean())
print("-------------------------------------")
print("Media del dataframe redondeada: ", round(columnas_desde_tercera_hasta_sexta.mean().mean(),2))
print("-------------------------------------")
print("Mediana del dataframe: ", columnas_desde_tercera_hasta_sexta.median().median())
print("-------------------------------------")
print("Moda del dataframe: ", columnas_desde_tercera_hasta_sexta.mode().iloc[0, 0])
print("-------------------------------------")

percentil_25 = columnas_desde_tercera_hasta_sexta.quantile(0.25)
percentil_50 = columnas_desde_tercera_hasta_sexta.quantile(0.50)  # Esto es equivalente a la mediana
percentil_75 = columnas_desde_tercera_hasta_sexta.quantile(0.75)

# Imprimir los percentiles
print("Percentil 25:")
print(percentil_25)
print("\nPercentil 50 (Mediana):")
print(percentil_50)
print("\nPercentil 75:")
print(percentil_75)
print("-------------------------------------")
print("Varianza de todos los números: ", columnas_desde_tercera_hasta_sexta.values.var())