import pandas as pd

generatedPath = '../dataset/generated/'
datasetPath = '../dataset/dataset.csv'
origenDelContagioPath = '../dataset/IE-origen-del-contagio.csv'

infoDiaria = pd.read_csv(datasetPath, index_col='Fecha')
infoDiaria.index = pd.to_datetime(infoDiaria.index, format='%d/%m/%Y')
infoDiaria = infoDiaria.sort_values(by=['Fecha'], ascending=True)

# Casos diarios
fileName = 'DFcasosDiarios.csv'
infoDiaria[['Personas afectadas', 'Casos positivos desde el inicio', 'Aislamiento domiciliario', 'Ingresos totales', 'Ingresos en cuidados intensivos', 'Personas curadas', 'Fallecidos']] \
    .diff() \
    .fillna(infoDiaria) \
    .astype('int32') \
    .T \
    .to_csv(generatedPath + fileName, index_label='Fecha')

# Test realizados
fileName = 'DFtestRealizados.csv'
infoDiaria['Pruebas realizadas'] \
    .to_csv(generatedPath + fileName, index_label='Fecha')

# Casos según el origen del contagio (odc)
DFodc = pd.read_csv(origenDelContagioPath, index_col='Fecha')
DFodc = DFodc.sort_values(by=['Fecha'], ascending=True)

fileName = 'DFodcTipos.csv'
DFodc[['Importados','Autóctonos relacionado con un caso','Autóctonos sin vinculo epidemiológico', 'No consta']] \
    .T \
    .to_csv(generatedPath + fileName, index_label='Fecha')

fileName = 'DFodcRealizadasDetalladas.csv'
DFodc[['Pruebas realizadas', 'Casos detallados']] \
    .fillna(0) \
    .astype('int32') \
    .to_csv(generatedPath + fileName, index_label='Fecha')
