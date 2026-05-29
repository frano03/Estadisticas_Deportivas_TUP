import pandas as pd
import matplotlib.pyplot as plt
import os

# ID-Jira: SCRUM-2 (Paco) - Implementación de lógica con dataset correcto
# Uso de rutas relativas según el estándar de reproducibilidad [5]
ruta_datos = 'datos/dataset - 2020-09-24.csv' 
ruta_resultados = 'resultados/'

try:
    # Carga de datos
    df = pd.read_csv(ruta_datos)
    print(f"Archivo {ruta_datos} cargado con éxito.")

    # IMPORTANTE: Como confirmamos antes que este dataset es de JUGADORES 
    # y no de PARTIDOS, aquí debes ajustar la lógica. 
    # Por ejemplo, calcular el promedio de goles de los jugadores:
    promedio_goles = df['Goals'].mean()
    
    # Ranking de goleadores por club
    top_goleadores = df.sort_values(by='Goals', ascending=False).head(10)

    # Crear carpeta de resultados si no existe
    os.makedirs(ruta_resultados, exist_ok=True)
    
    # Guardar reporte de texto
    with open(f'{ruta_resultados}resumen_estadistico.txt', 'w') as f:
        f.write("=== ANÁLISIS DE ESTADÍSTICAS DE JUGADORES ===\n")
        f.write(f"Promedio de goles por jugador: {promedio_goles:.2f}\n\n")
        f.write("Top 10 Goleadores:\n")
        f.write(top_goleadores[['Name', 'Club', 'Goals']].to_string())

    # Generar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(top_goleadores['Name'], top_goleadores['Goals'], color='orange')
    plt.title('Top 10 Goleadores - Premier League')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{ruta_resultados}grafico_resultados.png')
    
    print(f"Análisis finalizado. Resultados guardados en {ruta_resultados}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {ruta_datos}. Verifique la carpeta /datos.")
except Exception as e:
    print(f"Error inesperado: {e}")
