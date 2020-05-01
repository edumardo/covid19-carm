import pandas as pd
import datetime as dt

generatedPath = '../dataset/generated/'
datasetPath = '../dataset/dataset.csv'
origenDelContagioPath = '../dataset/IE-origen-del-contagio.csv'

infoDiaria = pd.read_csv(datasetPath, index_col='Fecha')
infoDiaria.index = pd.to_datetime(infoDiaria.index, format='%d/%m/%Y')
infoDiaria = infoDiaria.sort_values(by=['Fecha'], ascending=True)

fechaCambioDetalle = dt.datetime.strptime('18/04/2020', '%d/%m/%Y')

# Variación diaria
fileName = 'DFcasosDiarios.csv'
infoDiaria[['Personas afectadas', 'Casos positivos desde el inicio', 'Aislamiento domiciliario', 'Ingresos totales', 'Ingresos en cuidados intensivos', 'Personas curadas', 'Fallecidos']] \
    .diff() \
    .fillna(infoDiaria) \
    .astype('int32') \
    .T \
    .to_csv(generatedPath + fileName, index_label='Fecha')

# Detalle de casos positivos
fileName = 'DFdetalleCasosPositivos.csv'
infoDiaria[['Casos positivos desde el inicio (PCR)', 'Casos positivos desde el inicio (Anticuerpos)']] \
    .diff() \
    .dropna() \
    .astype('int32') \
    .rename(columns={'Casos positivos desde el inicio (PCR)': 'PCR', 'Casos positivos desde el inicio (Anticuerpos)': 'Anticuerpos'}) \
    .to_csv(generatedPath + fileName, index_label='Fecha')

# Test diarios realizados
fileName = 'DFtestRealizados.csv'
totalTestRealizados = infoDiaria['Pruebas realizadas'].diff().fillna(infoDiaria['Pruebas realizadas']).astype('int32')
totalTestRealizados.where(totalTestRealizados.index < fechaCambioDetalle, 0, True)
detallePRCRealizados = infoDiaria['Pruebas realizadas (PCR)'].diff().fillna(0).astype('int32')
detalleAntiRealizados = infoDiaria['Pruebas realizadas (Anticuerpos)'].diff().fillna(0).astype('int32')
testRealizados = pd.DataFrame( \
    {   'Pruebas realizadas': totalTestRealizados, \
        'Pruebas realizadas (PCR)': detallePRCRealizados, \
        'Pruebas realizadas (Anticuerpos)' : detalleAntiRealizados
    }) \
    .T \
    .to_csv(generatedPath + fileName, index_label='Fecha')

# Casos positivos
fileName = 'DFcasosPositivos.csv'
infoDiaria[['Personas afectadas', 'Personas curadas', 'Fallecidos']] \
    .to_csv(generatedPath + fileName, index_label='Fecha')

# Desenlace de casos cerrados (% curados vs % fallecidos)
fileName = 'DFcasosCerrados.csv'
casosCerrados = infoDiaria['Personas curadas'] + infoDiaria['Fallecidos']
ratioCuradas = round(infoDiaria['Personas curadas'] * 100 / casosCerrados, 2).fillna(0)
ratioFallecidos = round(infoDiaria['Fallecidos'] * 100 / casosCerrados, 2).fillna(0)
pd.DataFrame({'% Personas curadas': ratioCuradas, '% Fallecidos': ratioFallecidos}) \
    .to_csv(generatedPath + fileName, index_label='Fecha')

# Casos según el origen del contagio (odc)
DFodc = pd.read_csv(origenDelContagioPath, index_col='Fecha')
DFodc.index = pd.to_datetime(DFodc.index, format='%d/%m/%Y')
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
