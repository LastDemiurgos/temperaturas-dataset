
import pandas as pd
import numpy as np

# Generar datos aleatorios
np.random.seed(42)  # Para reproducibilidad de resultados

fechas = pd.date_range(start='2017-01-01', end='2023-12-31', freq='D')
num_dias = len(fechas)

temperaturas = np.random.randint(0, 40, size=(num_dias, 3))
categorias = np.random.choice(['abrigada', 'normal', 'verano'], size=num_dias)

# Crear el DataFrame y guardar en el archivo CSV
data = pd.DataFrame(temperaturas, columns=['temp_dia_1', 'temp_dia_2', 'temp_dia_3'])
#, 'temp_dia_4', 'temp_dia_5'
data['ropa'] = categorias
data['fecha'] = fechas

data.to_csv('datos_temperatura_ropa3.csv', index=False)
