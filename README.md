### Context

COVID-19 datasets based on data from Gobierno de la Región de Murcia, Spain. Data extracted from:

* Daily tweets of the [official twitter account](https://twitter.com/regiondemurcia) of Gobierno de la Región de Murcia.
* Epidemiological reports in pdf format from [MurciaSalud](http://www.murciasalud.es/pagina.php?id=458869), Consejería de Salud de la Región de Murcia.

The data comes from this [github repository](https://github.com/edumardo/covid19-carm), and you can explore it and build models in this [Kaggle page](https://www.kaggle.com/edumardo/covid19-dataset-from-regin-de-murcia-spain). I've done several charts created with the dataset on [edumardo.github.io/covid19-carm](https://edumardo.github.io/covid19-carm/).

### Content

#### dataset.csv

|Column| Description                                                       | Format             |
|------|-------------------------------------------------------------------|--------------------|
|Fecha | Date of the row, corresponding to the last information of the day | DD/MM/YYYY |
|Personas afectadas | Affected people | Number |
|Aislamiento domiciliario | Home insulation | Number |
|Ingresos totales | Hospitalized patients | Number |
|Ingresos en cuidados intensivos | Intensive care patients | Number |
|Personas curadas | Recovered persons | Number |
|Fallecidos | Deaths | Number |
|Pruebas realizadas | Tests performed | Number |
| Fuente | Data source (tweet from @regiondemurcia) | url |

#### IE-origen-del-contagio.csv

|Columna| Descripción | Formato |
|-------|-------------|---------|
| Pruebas realizadas | Pruebas diagnósticas realizadas para la detección de coronavirus | Número |
| Casos detallados |  Casos de los que se dispone información detallada | Número |
| Importados | Casos importados de otro país u otra CCAA | % |
| Autóctonos relacionado con un caso | Casos vinculados epidemiológicamente a un caso previo de fuera o dentro de la Región (casos secundarios) | % |
| Autóctonos sin vinculo epidemiológico | Casos autóctonos sin vínculo epidemiológico claro (indica transmisión comunitaria en la Región) | % |
| Municipios afectados | Número de municipios en los que se han registrado casos | Número |
| Fuente | Enlace al informe epidemiológico (documento pdf de MurciaSalud) | url |

### Acknowledgements

I compile the data checking by hand, hence, I try to be careful. 

### Inspiration

The Gobierno de la Región de Murcia provides the information about COVID-19 by an attached image in a tweet or in a pdf document, without historical context. Therefore, it's not easy to know how the virus is growing.
