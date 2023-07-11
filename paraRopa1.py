import pandas as pd
import numpy as np

np.random.seed(42)  # Para reproducibilidad de resultados

fechas = pd.date_range(start='2017-01-01', end='2023-12-31', freq='D')
num_dias = len(fechas)

temperaturas = []
categorias = []

for _ in range(num_dias):
    while True:
        temp_dia_1 = np.random.randint(0, 41)  # Rango para "abrigada", "normal" y "verano": 0 a 40
        temp_dia_2 = np.random.randint(0, 41)  # Rango para "abrigada", "normal" y "verano": 0 a 40
        temp_dia_3 = np.random.randint(0, 41)  # Rango para "abrigada", "normal" y "verano": 0 a 40

        # Asignar categoría según los rangos de temperatura
        if 0 <= temp_dia_1 <= 15 or 0 <= temp_dia_2 <= 15 or 0 <= temp_dia_3 <= 15:
            categoria = 'abrigada'
        elif 16 <= temp_dia_1 <= 29 or 16 <= temp_dia_2 <= 29 or 16 <= temp_dia_3 <= 29:
            categoria = 'normal'
        else:
            categoria = 'verano'
        
        # Verificar si las temperaturas coinciden con la categoría asignada
        "queda si o si en categoria no hay de otra "
        if categoria == 'abrigada' and (0 <= temp_dia_1 <= 15) and (0 <= temp_dia_2 <= 15) and (0 <= temp_dia_3 <= 15):
            break
        elif categoria == 'normal' and (16 <= temp_dia_1 <= 29) and (16 <= temp_dia_2 <= 29) and (16 <= temp_dia_3 <= 29):
            break
        elif categoria == 'verano' and (30 <= temp_dia_1 <= 40) and (30 <= temp_dia_2 <= 40) and (30 <= temp_dia_3 <= 40):
            break
    
    temperaturas.append([temp_dia_1, temp_dia_2, temp_dia_3])
    categorias.append(categoria)

data = pd.DataFrame(temperaturas, columns=['temp_dia_1', 'temp_dia_2', 'temp_dia_3'])
data['ropa'] = categorias
data['fecha'] = fechas

data.to_csv('datos_temperatura_ropa4.csv', index=False)
