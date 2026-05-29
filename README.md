# Proyecto: Estadísticas Deportivas TUP ⚽

Este repositorio contiene el desarrollo del Trabajo Práctico Integrador para la materia **Organización Empresarial** de la Tecnicatura Universitaria en Programación (UTN). El proyecto aplica metodologías ágiles, control de versiones con Git y gestión de tareas mediante Jira [4, 5].

## 👥 Integrantes y Roles (Célula de Desarrollo)
Según el marco de trabajo definido por la cátedra [6]:
*   **Hugo (P1) - Líder y Organizador:** Responsable de la gobernanza del repositorio y estructura inicial.
*   **Paco (P2) - Desarrollador Técnico:** Responsable de la lógica algorítmica y procesamiento de datos.
*   **Luis (P3) - Revisor y QA:** Responsable de la calidad, Peer Review y documentación final.

## 📋 Escenario Elegido: Escenario D
El equipo ha seleccionado el **Escenario D: Estadísticas de Resultados Deportivos** [7]. 
**Objetivo:** Analizar datos de campeonatos para generar indicadores de rendimiento, tablas de posiciones y promedios de goles, facilitando la toma de decisiones basada en datos históricos [7].

## 📂 Estructura del Repositorio
Siguiendo los estándares de reproducibilidad técnica [8, 9]:
- `datos/`: Contiene los archivos CSV con las estadísticas de la Premier League.
- `scripts/`: Contiene el código fuente `analisis_datos.py` desarrollado en Python.
- `resultados/`: Almacena los reportes estadísticos y gráficos generados automáticamente.
- `.gitignore`: Archivo para excluir archivos temporales y sensibles [10].
## 🚀 Instrucciones de Ejecución
Para reproducir el análisis en un entorno de Google Colab, siga estos pasos [11-13]:
1. **Clonar el repositorio:**
   ```bash
   !git clone https://github.com/frano03/Estadisticas_Deportivas_TUP.git
Configurar el entorno: Asegúrese de que el archivo dataset - 2020-09-24.csv se encuentre en la carpeta /datos.
Ejecutar el script de análisis:
Ver resultados: Los archivos generados aparecerán en la carpeta /resultados.
🛠️ Gestión y Trazabilidad
Este proyecto utiliza un Mandato de Trazabilidad. Cada cambio en el código está vinculado a una tarea en Jira mediante el uso de IDs en los mensajes de commit (ej. SCRUM-2: Paco - Implementación de lógica...)
.

--------------------------------------------------------------------------------
Año Lectivo 2026 - UTN TUP a Distancia

### Por qué este archivo es profesional para tu TP:
*   **Cumple con la Rúbrica:** Incluye el título, integrantes, escenario y descripción del dataset, requisitos para obtener la calificación de "Excelente" [1, 2].
*   **Define Roles:** Clarifica quién es Hugo, Paco y Luis, lo que demuestra organización empresarial [6].
*   **Fomenta la Reproducibilidad:** Al detallar la estructura y los pasos de ejecución, permites que cualquier docente o compañero corra tu código sin errores [15].
*   **Menciona Jira:** Resalta la trazabilidad, que es un punto crítico evaluado por la cátedra [16].
