### Context

COVID-19 dataset based on data from Gobierno de la Región de Murcia, Spain. Data extracted from the daily tweets of the [official twitter account](https://twitter.com/regiondemurcia) of Gobierno de la Región de Murcia.

The data comes from this [github repository](https://github.com/edumardo/covid19-carm), and you can explore it and build models in this [Kaggle page](https://www.kaggle.com/edumardo/covid19-dataset-from-regin-de-murcia-spain). I've done several charts created with the dataset on [github.com/edumardo/covid19-carm](https://github.com/edumardo/covid19-carm).

### Content

The dataset has one row per day, from the official twitter account of Gobierno de la Región de Murcia, Spain. They publish the daily account via tweet, in an attached image.
They are reporting the information since March 10th, with the following columns:

|Column| Description                                                       | Format             |
|------|-------------------------------------------------------------------|--------------------|
|Fecha | Date of the row, corresponding to the last information of the day | DD/MM/YYYY HH24:MM |
|Personas afectadas | Affected people | Number |
|Aislamiento domiciliario | Home insulation | Number |
|Ingresos totales | Hospitalized patients | Number |
|Ingresos en cuidados intensivos | Intensive care patients | Number |
|Personas curadas | Recovered persons | Number |
|Fallecidos | Deaths | Number |
|Pruebas realizadas | Tests performed | Number |
| Fuente | Data source (tweet from @regiondemurcia) | text |

### Acknowledgements

I compile the data checking the tweets by hand, hence, I try to be careful. 

### Inspiration

The Gobierno de la Región de Murcia provides the information about COVID-19 by an attached image in a tweet without historical context. Therefore, it's not easy to know how the virus is growing.
