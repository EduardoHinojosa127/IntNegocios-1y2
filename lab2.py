import numpy as np
import pandas as pd

# Generar un arreglo de 6 números aleatorios
arreglo_original = np.random.randint(1, 100, 6)

print("First Exercise:")

# Imprimir el arreglo original
print("Arreglo original:")
print(arreglo_original)

# Renombrar los índices del arreglo
nuevos_indices = ['A', 'B', 'C', 'D', 'E', 'F']
arreglo_con_indices_nuevos = {indice: valor for indice, valor in zip(nuevos_indices, arreglo_original)}

# Imprimir el arreglo con los nuevos índices
print("\nArreglo con nuevos índices:")
print(arreglo_con_indices_nuevos)

print("----------------------------------------------------")

print("Second Exercise:")

# Crear un arreglo de 3 elementos de texto con valores numéricos
arreglo_texto = np.array(['42', '3.14', '7.5'])

# Convertir los datos de texto a números
arreglo_numerico = arreglo_texto.astype(float)

# Imprimir el arreglo numérico
print("Arreglo numérico:")
print(arreglo_numerico)
print("----------------------------------------------------")

print("Third exercise")

arreglo = np.random.randint(1, 51, 10)
arreglo_ordenado = np.sort(arreglo)
# Imprimir todos los números
print("Todos los números:")
print(arreglo_ordenado)

# Imprimir los primeros 5 números
print("\nLos primeros 5 números:")
print(arreglo_ordenado[:5])

# Imprimir los últimos 5 números
print("\nLos últimos 5 números:")
print(arreglo_ordenado[5:])

# Imprimir los 2 primeros números
print("\nLos 2 primeros números:")
print(arreglo_ordenado[:2])

# Imprimir los 2 últimos números
print("\nLos 2 últimos números:")
print(arreglo_ordenado[-2:])

print("----------------------------------------")

print("Fourth exercise")

data = {'Texto': ['A', 'B', 'C', 'D', 'E', 'F'],
        'Valor': [10, 20, 30, 40, 50, 60]}

df = pd.DataFrame(data)

# Imprimir el DataFrame
print("DataFrame original:")
print(df)

# Paso b - Cambiar el orden de las columnas
# Crear una lista con el orden deseado de las columnas
nuevo_orden_columnas = ['Valor', 'Texto']

# Reordenar las columnas del DataFrame
df = df[nuevo_orden_columnas]

# Imprimir el DataFrame con el nuevo orden de columnas
print("\nDataFrame con columnas reordenadas:")
print(df)

print("--------------------------------------------")

print("Fifth exercise")

nombre_archivo = "Ventas.csv"

# Leer el archivo CSV y cargarlo en un DataFrame
df = pd.read_csv(nombre_archivo)

print(df)

print("--------------------------------------------------")

print("Sixth exercise")

# Generar el primer DataFrame
data1 = {'Texto1': ['A', 'B', 'C', 'D', 'E', 'F'],
         'Valor1': [10, 20, 30, 40, 50, 60]}

df1 = pd.DataFrame(data1)

# Imprimir el primer DataFrame
print("Primer DataFrame:")
print(df1)

# Generar el segundo DataFrame
data2 = {'Texto2': ['G', 'H', 'I', 'J', 'K', 'L'],
         'Valor2': [70, 80, 90, 100, 110, 120]}

df2 = pd.DataFrame(data2)

# Imprimir el segundo DataFrame
print("\nSegundo DataFrame:")
print(df2)

# Agregar el segundo DataFrame al primero
df1 = pd.concat([df1, df2], axis=1)

# Imprimir el DataFrame resultante después de la agregación
print("\nDataFrame después de agregar el segundo DataFrame:")
print(df1)

print("-----------------------------------------------------")

print("Ventas del primer trimestre:")
print(df.head(3))
numero_de_registros = df.shape[0]
numero_de_campos = df.shape[1]

print("Número de registros y campos")
print(numero_de_registros)
print(numero_de_campos)

ventas_primer_trimestre = df.head(3)["Monto"].values

print(ventas_primer_trimestre)

media_ventas = np.mean(ventas_primer_trimestre)
print("Media de las ventas del primer trimestre:", media_ventas)

correlacion = df["Monto"].corr(df["Monto"])
print("Correlación entre Monto y Monto, ya que no hay más datos numéricos:", correlacion)

valor_minimo = np.min(ventas_primer_trimestre)
valor_maximo = np.max(ventas_primer_trimestre)
print("Valor más bajo:", valor_minimo)
print("Valor más alto:", valor_maximo)

# Imprimir la mediana
mediana_ventas = np.median(ventas_primer_trimestre)
print("Mediana de las ventas del primer trimestre:", mediana_ventas)

# Imprimir la desviación estándar
desviacion_estandar_ventas = np.std(ventas_primer_trimestre)
print("Desviación estándar de las ventas del primer trimestre:", desviacion_estandar_ventas)

# Imprimir solo la primera columna del dataset
primera_columna = df.iloc[:, 0]
print("Primera columna del dataset:")
print(primera_columna)

# Imprimir las 2 primeras columnas
dos_primeras_columnas = df.iloc[:, :2]
print("Dos primeras columnas del dataset:")
print(dos_primeras_columnas)

# Imprimir la primera fila y última columna
primera_fila_ultima_columna = df.iloc[0, -1]
print("Primera fila y última columna del dataset:")
print(primera_fila_ultima_columna)

# Imprimir los valores de la primera fila
valores_primera_fila = df.iloc[0, :].values
print("Valores de la primera fila:")
print(valores_primera_fila)

df_sin_columnas = pd.read_excel("Ventas02.xlsx", header=None)
print(df_sin_columnas)
