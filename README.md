# Data_Streaming_Project

the link to the slide: https://www.overleaf.com/5531729263nsgvjjmztmwm

This project was made by Pierre LOVITON, Yao Pacome KOUAME and Angie Méndez-Llanos in the framework of the course Data Stream Processing from the M2 Data Science master's at the Institut Polytechnique.

The goal is to use online learning models to predict the future value of a given cryptocurrencies using Kafka to process the data. The models were compared to a similar batch version.

An analysis of the batch and online models along with some visualizations can be found in batch_models.ipynb and online_models.ipynb, respectively. 

## Application

The goal of the application is to create a data flow, using Kafka, to retrieve stock data in real time and then use an online learning model to predict the future value of a cryptocurrency. The sripts should be executed in the following order:

#### 1. Retrieving the data <*ingest-data-BTCUSDT.py*>

The script makes a request to the Binance API (https://binance-docs.github.io/apidocs/spot/en/#introduction) and a producer sends the data to a Kafka topic. 
In our example, the data is sent to  **BTCUSDT-1m-raw**.

#### 2. Clean raw data <*clean-data-BTCUSDT.py*>

A consumer reads the messages from  **BTCUSDT-1m-raw**, cleans the data and then a producer sends it to **BTCUSDT-1m-clean**.

#### 3. Model clean data (<*model-linear-BTCUSDT.py*>, <*model-HTreg-BTCUSDT.py*>, <*model-HATReg-BTCUSDT.py*>, <*model-SNARIMAX-BTCUSDT.py*>)

A consumer reads the data from BTCUSDT-1m-clean, the online models are trained and the output is saved to the respective model topic (**model-linear-BTCUSD**, **model-HTreg-BTCUSDT**, **model-HATReg-BTCUSDT**, **model-SNARIMAX-BTCUSDT**).
