# Proyecto: Estadísticas Deportivas TUP
Integrante: Francisco Nahuel Ortiz (Hugo, Paco y Luis)
Escenario: D
Estadísticas de Resultados Deportivos: Premier League ⚽
📋 Visión General
Este proyecto integra la gestión colaborativa, el control de versiones y la organización empresarial mediante el uso de metodologías ágiles (Scrum) y herramientas profesionales como Git, GitHub y Jira
. El objetivo es analizar el rendimiento de equipos de la Premier League a partir de datos históricos, garantizando un flujo de trabajo trazable y reproducible
.
👥 Célula de Desarrollo
El proyecto fue realizado por el siguiente equipo técnico:
P1 - Líder y Organizador: Hugo
P2 - Desarrollador Técnico: Paco
P3 - Revisor y QA (Quality Assurance): Luis
🛠️ Escenario Seleccionado
Se trabajó sobre el Escenario D: Estadísticas de Resultados Deportivos
. El análisis se centra en procesar resultados de partidos para generar métricas de rendimiento y tablas de posiciones, culminando en visualizaciones gráficas comparativas
.
📂 Estructura del Repositorio
Siguiendo el mandato técnico de la cátedra, el repositorio se organiza de la siguiente manera
:
Estadisticas_Deportivas_TUP/
│
├── datos/                # Dataset en formato CSV [13]
│   └── dataset - 2020-09-24.csv
│
├── scripts/              # Código fuente en Python (.py puro) [13, 14]
│   └── analisis_datos.py
│
├── resultados/           # Productos del análisis (gráficos/tablas) [2]
│   └── grafico_resultados.png
│
├── README.md             # Documentación general del proyecto [2]
└── .gitignore            # Exclusión de archivos innecesarios (.ipynb_checkpoints, etc.) [2, 15]
📊 Descripción del Dataset
El archivo utilizado es dataset - 2020-09-24.csv, el cual contiene registros detallados de los partidos de la Premier League
. Incluye variables clave como equipos intervinientes, goles marcados y fechas de los encuentros
.
🚀 Instrucciones de Ejecución
Para garantizar la reproducibilidad, el script utiliza rutas relativas
. Siga estos pasos para ejecutar el análisis en Google Colab o entorno local:
Clonar el repositorio:
Asegurarse de tener instalado Python 3.x y la librería Pandas.
Ejecutar el script principal:
Los resultados (gráficos) se guardarán automáticamente en la carpeta /resultados
.
📈 Gestión y Trazabilidad (Jira)
El desarrollo siguió un flujo de trabajo estrictamente vinculado al tablero de Jira para asegurar la trazabilidad
:
SCRUM-1: Inicialización de estructura técnica.
SCRUM-2: Implementación de lógica algorítmica y carga de datos
.
SCRUM-3: Revisión por pares (Peer Review) y QA final
.

--------------------------------------------------------------------------------
Institución: Universidad Tecnológica Nacional (UTN)
Materia: Organización Empresarial
Año: 2026
