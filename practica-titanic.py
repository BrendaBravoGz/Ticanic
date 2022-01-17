import pandas
from seaborn import load_dataset

df = pandas.read_csv('titanic.csv',delimiter=",")
#Imprime el DataFrame
print(df)
print("\n")
#Imprime el número de filas
print("* Numero de filas:", len(df))
print("\n")
#Imprime el número de columas
print("* Numero de columnas:", len(df.columns))
print("\n")
#Imprime el total de elementos del DataFrame
print("* Numero de elementos:", df.size)
print("\n")
#Imprime el nombre de las columnas del DataFrame
print("* Nombre de columnas:",df.columns.values)
print("\n")
#Imprime el Nombre de las filas del DataFrame
print("* Nombre de filas:", df.index.values)
print("\n")
#Imprime los primeros 10 elementos del DataFrame
print("* Primeros 10: \n ", df.head(10))
print("\n")
#Imprime los últimos 10 elementos del DataFrame
print("* Últimos 10: \n", df.tail(10))
print("\n")
#Imprime los datos del pasajero 148
print("* pasajero con identificador 148: \n ", df.iloc[147])
#Imprime las filas en pares
x=0
while x < len(df):
    if x%2 != 0:
        pares=df.iloc[x]
        #print(pares)
    x=x+1

#Imprime la primera clase, ordenada alfabeticamente
df_pclass=df['Pclass'] == 1
df_filtrado_1 =df[df_pclass]

df_filtrado_1.sort_values('Name',inplace=True)
df_filtrado_1.head()

print(df_filtrado_1)
print("\n")
#Mostrar porcentaje de personas que sobrevivieron y murieron
print("Porcentaje de sobrevivientes y muertos")
print(df['Survived'].value_counts()/df['Survived'].count() * 100)
print("\n")
#Mostrar porcentaje de personas que sobrevivieron y murieron en cada clase
print("Sobrevivientes y muertos de clase 1")
print(df_filtrado_1['Survived'].value_counts()/df_filtrado_1['Survived'].count() * 100)
print("\n")
df_pclass=df['Pclass'] == 2
df_filtrado_2 =df[df_pclass]
print("Sobrevivientes y muertos de clase 2")
print(df_filtrado_2['Survived'].value_counts()/df_filtrado_2['Survived'].count() * 100)
print("\n")
df_pclass=df['Pclass'] == 3
df_filtrado_3 =df[df_pclass]
print("Sobrevivientes y muertos de clase 3")
print(df_filtrado_3['Survived'].value_counts()/df_filtrado_3['Survived'].count() * 100)
print("\n")
#Eliminar del DataFrame los pasajeros con edad desconocida
df_edad_desconocida=df[df['Age'].notna()]
print(df_edad_desconocida)
print("\n")
#Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase
df_edad_media = df.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female']
print(df_edad_media)
print("\n")

#Agregar nueva columna para ver si el pasajero era menor o mayor de edad
df['Mayor_edad'] = df['Age'] < 18

#Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase
print(df.groupby(['Pclass', 'Mayor_edad'])['Survived'].value_counts(normalize = True) * 100)