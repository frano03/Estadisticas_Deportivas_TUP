import pandas as pd
import matplotlib.pyplot as plt
import os

# ID-Jira: SCRUM-2 (Paco) - Desarrollo de lógica de análisis para la Premier League

# 1. CONFIGURACIÓN DE RUTAS Y CARGA
# Usamos rutas relativas para garantizar la reproducibilidad en Google Colab [5]
# NOTA: Cambia 'dataset_premier_league.csv' por el nombre real de tu archivo si es distinto
ruta_datos = 'datos/dataset - 2020-09-24.csv' 

try:
    df = pd.read_csv(ruta_datos)
    print(f"Dataset cargado exitosamente: {ruta_datos}")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {ruta_datos}. Verifique la carpeta /datos.")
    exit()

# 2. PROCESAMIENTO DE ESTADÍSTICAS (Escenario D: Estadísticas Deportivas) [8]
# Calculamos el promedio de goles sumando ambos extremos (local/visitante). 
# Se asume que no hay valores nulos para no sesgar el promedio por partido.
total_goles = df['home_goals'].sum() + df['away_goals'].sum()
promedio_goles = total_goles / len(df)

# Determinamos el ganador mediante una función lambda/apply para crear una 
# columna de resultados. Esto facilita el conteo posterior de victorias por equipo.
def calcular_ganador(row):
    if row['home_goals'] > row['away_goals']:
        return row['home_team']
    elif row['away_goals'] > row['home_goals']:
        return row['away_team']
    else:
        return 'Empate'

df['ganador'] = df.apply(calcular_ganador, axis=1)
# Filtramos los empates para obtener solo el ranking de equipos victoriosos
partidos_ganados = df[df['ganador'] != 'Empate']['ganador'].value_counts()

# 3. PERSISTENCIA DE RESULTADOS EN /resultados [7, 12]
os.makedirs('resultados', exist_ok=True)

with open('resultados/resumen_estadistico.txt', 'w') as f:
    f.write("=== RESUMEN DE ESTADÍSTICAS DEPORTIVAS ===\n")
    f.write(f"Promedio de goles por partido: {promedio_goles:.2f}\n\n")
    f.write("Ranking de Partidos Ganados por Equipo:\n")
    f.write(partidos_ganados.to_string())

# 4. VISUALIZACIÓN DE RENDIMIENTO [8]
plt.figure(figsize=(10, 6))
# Mostramos solo el Top 10 para mantener la legibilidad del gráfico
partidos_ganados.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Equipos con más Partidos Ganados - Premier League')
plt.xlabel('Equipos')
plt.ylabel('Victorias Totales')
plt.xticks(rotation=45)
plt.tight_layout()

# Guardado del producto visual en la carpeta técnica correspondiente [13]
plt.savefig('resultados/grafico_rendimiento.png')
print("Análisis finalizado. Resultados exportados a la carpeta /resultados")
