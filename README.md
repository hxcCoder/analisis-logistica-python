# 📊 Análisis de Datos de Logística

## 📋 Resumen del Proyecto

Este proyecto es un análisis de datos completo para una empresa de logística. Utilicé Python y la biblioteca pandas para procesar y limpiar datos de entregas, clientes y transportistas. El objetivo fue identificar las métricas clave de rendimiento y visualizar los resultados para ayudar a tomar decisiones informadas.

## 🚀 Habilidades Tecnicas

* **Python:** Utilización de scripts para automatizar el análisis de datos.
* **Pandas:** Carga de datos, limpieza, manipulación (`.str.strip()`, `.str.lower()`) y unión de múltiples DataFrames (`pd.merge`).
* **Análisis de Datos:** Cálculo de métricas como el tiempo de entrega promedio por región, el porcentaje de entregas por estado y el conteo de vehículos.
* **Visualización de Datos:** Creación de gráficos claros y concisos utilizando `Matplotlib`.
* **Gestión de Proyectos:** Organización del proyecto con una estructura de carpetas lógica (`data`, `outputs`) y manejo de errores de archivos.
* **Habilidad de Depuración:** Superación de errores comunes como `KeyError`, lo que demuestra una sólida capacidad para resolver problemas de forma independiente.
  
## 📈 Resultados del Análisis

El script `analisis.py` procesa los datos y genera los siguientes resultados:

1.  **Distribución de Entregas por Estado:**
    ![Distribución de Entregas por Estado](outputs/porcentaje_entregas.png)

2.  **Tiempo de Entrega Promedio por Región:**
    ![Tiempo de Entrega Promedio por Región](outputs/tiempo_por_region.png)

Además, el script exporta un archivo de Excel llamado `reporte_entregas_retrasadas.xlsx` que contiene una lista de todas las entregas con estado 'Retrasado' para un análisis más detallado.

## ▶️ Cómo ejecutar el proyecto

Para ejecutar el análisis en tu entorno local, sigue estos pasos:

1.  Asegúrate de tener Python instalado.
2.  Instala las bibliotecas necesarias:
    ```bash
    pip install pandas matplotlib openpyxl
    ```
3.  Coloca tus archivos `clientes.xlsx`, `entregas.xlsx` y `transportistas.xlsx` en la carpeta `data`.
4.  Ejecuta el script desde tu terminal:
    ```bash
    python analisis.py
    ```

El script generará automáticamente los gráficos y el reporte de Excel en la carpeta `outputs`.
