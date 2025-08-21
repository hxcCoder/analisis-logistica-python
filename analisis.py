import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- 1. CONFIGURACIÓN DEL PROYECTO Y CARGA DE DATOS ---
# Define la estructura de carpetas
BASE = Path('.')
DATA_FOLDER = BASE / 'data'
OUT_FOLDER = BASE / 'outputs'
OUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Lee cada archivo de Excel en un DataFrame de pandas
try:
    df_entregas = pd.read_excel(DATA_FOLDER / 'entregas.xlsx', engine='openpyxl')
    df_clientes = pd.read_excel(DATA_FOLDER / 'clientes.xlsx', engine='openpyxl')
    df_transportistas = pd.read_excel(DATA_FOLDER / 'transportistas.xlsx', engine='openpyxl')
    print("✅ Archivos cargados exitosamente.")
except FileNotFoundError as e:
    print(f"❌ Error: Uno de los archivos no se encontró. Revisa la carpeta 'data'. Detalles: {e}")
    exit()

# --- 2. LIMPIEZA Y UNIFICACIÓN DE DATOS ---
# Estandariza los nombres de las columnas para evitar errores de formato
df_entregas.columns = df_entregas.columns.str.lower().str.strip()
df_clientes.columns = df_clientes.columns.str.lower().str.strip()
df_transportistas.columns = df_transportistas.columns.str.lower().str.strip()

# Unifica las tablas de forma lógica y secuencial
df_completo = pd.merge(df_entregas, df_clientes, on='id_cliente', how='left')
df_completo = pd.merge(df_completo, df_transportistas, on='id_transportista', how='left')

# Limpieza adicional de datos
df_completo['fecha'] = pd.to_datetime(df_completo['fecha'], errors='coerce')
df_completo.dropna(subset=['fecha'], inplace=True)
df_completo['estado'] = df_completo['estado'].str.capitalize()
print("\n✅ Datos unificados y limpios.")

# --- 3. ANÁLISIS DE DATOS CLAVE ---
print("\n--- INICIANDO ANÁLISIS DE DATOS ---")

conteo_estados = df_completo['estado'].value_counts(normalize=True) * 100
print("\n🔍 Porcentaje de entregas por estado:")
print(conteo_estados)

tiempo_por_region = df_completo.groupby('region')['tiempo_entrega_horas'].mean().sort_values()
print("\n🔍 Tiempo de entrega promedio por región (horas):")
print(tiempo_por_region)

conteo_vehiculos = df_completo['tipo_vehiculo'].value_counts()
print("\n🔍 Conteo de entregas por tipo de vehículo:")
print(conteo_vehiculos)

# --- 4. VISUALIZACIÓN Y REPORTE ---
print("\n--- GENERANDO REPORTES Y GRÁFICOS ---")

# Gráfico 1: Distribución de Entregas por Estado
plt.figure(figsize=(8, 6))
conteo_estados.plot(kind='bar', color=['green', 'red', 'orange'])
plt.title('Distribución de Entregas por Estado', fontsize=15)
plt.ylabel('Porcentaje (%)', fontsize=12)
plt.xlabel('Estado', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT_FOLDER / 'porcentaje_entregas.png')
print(f"✅ Gráfico de distribución guardado en {OUT_FOLDER / 'porcentaje_entregas.png'}")
plt.show()

# Gráfico 2: Tiempo de Entrega Promedio por Región
plt.figure(figsize=(10, 7))
tiempo_por_region.plot(kind='barh', color='skyblue')
plt.title('Tiempo de Entrega Promedio por Región', fontsize=15)
plt.xlabel('Tiempo de entrega promedio (horas)', fontsize=12)
plt.ylabel('Región', fontsize=12)
plt.tight_layout()
plt.savefig(OUT_FOLDER / 'tiempo_por_region.png')
print(f"✅ Gráfico de tiempo de entrega por región guardado en {OUT_FOLDER / 'tiempo_por_region.png'}")
plt.show()

# Guarda las entregas retrasadas en un nuevo archivo
df_retrasadas = df_completo[df_completo['estado'] == 'Retrasado']
df_retrasadas.to_excel(OUT_FOLDER / 'reporte_entregas_retrasadas.xlsx', index=False)
print(f"✅ Reporte de entregas retrasadas guardado en {OUT_FOLDER / 'reporte_entregas_retrasadas.xlsx'}")

print("\n--- PROYECTO COMPLETADO EXITOSAMENTE ---")