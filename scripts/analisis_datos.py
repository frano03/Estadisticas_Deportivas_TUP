import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos (Uso de rutas relativas para reproducibilidad) [3, 18]
df = pd.read_csv('datos/dataset.csv')

# 2. Lógica del Escenario D: Estadísticas Deportivas [17]
# Supongamos que el CSV tiene columnas: 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante'

# Ejemplo: Calcular promedio de goles por partido
promedio_goles = (df['goles_local'].sum() + df['goles_visitante'].sum()) / len(df)

# 3. Guardar resultados en la carpeta /resultados [2, 19-21]
with open('resultados/resumen_estadistico.txt', 'w') as f:
    f.write(f"Promedio de goles por partido: {promedio_goles:.2f}")

# 4. Generar y guardar un gráfico [17, 21]
df.groupby('equipo_local')['goles_local'].sum().plot(kind='bar')
plt.title('Goles Totales por Equipo (Local)')
plt.savefig('resultados/grafico_rendimiento.png')

print("Análisis completado. Archivos generados en /resultados")
