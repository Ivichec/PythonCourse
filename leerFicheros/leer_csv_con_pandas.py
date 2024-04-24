import pandas as pd
import os
current_directory = os.getcwd()

# Construct the file path to usuario.csv
file_path = os.path.join(current_directory, "leerFicheros", "usuario.csv")
print(file_path)
# Read the CSV file
df = pd.read_csv(file_path)
df2 = pd.read_csv(file_path)

#Slaycing
cadena = "0123456789"
#print(cadena[5:9])
df_ordenadoAscendente = df.sort_values("codigo")
df_ordenadoDescendente = df.sort_values("codigo",ascending=False)

#Concatenando los 2 dataframes
de_concatenado = pd.concat([df_ordenadoAscendente,df_ordenadoDescendente])

#accediendo a la primeras fila con head()
primeraFila = df.head(3)
#accediendo a las ultimas filas con tail()
ultimasFilas = df.tail(3)
#accediendo a la cantidad de filas y columnas con shape
filasTotales,columnasTotales = df.shape
#obteniendo data estadistica del dataframe
df_info = df.describe()
#accediendo a un elemento especifico del df con loc
elementoEspecifico = df.loc[2,"codigo"]
#accediendo a un elemento especifico del df con iloc
elementoEspecifico = df.iloc[2,2]
#acceder a todos los elementos de una columna
codigos = df.iloc[:,2]
#acceder a todos los elementos de una fila
codigosFila = df.iloc[2,:]
#acceder a filas con mas de 2 en el codigo
mayorId = df.loc[df["codigo"]>2,:]

print(mayorId)