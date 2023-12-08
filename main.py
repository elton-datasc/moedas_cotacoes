# Databricks notebook source
# MAGIC %md ### Consumo de dados de API (cotações e indicadores)

# COMMAND ----------

# MAGIC %md #### Instalação e atualização de bibliotecas específicas

# COMMAND ----------

#atualização do pacote adm de biblio
#pip install --upgrade pip

# COMMAND ----------

# instalando a biblioteca datetime
#pip install datetime

# COMMAND ----------

# biblioteca do bcb e do componente lxml
#pip install python-bcb
#pip install lxml

# COMMAND ----------

# MAGIC %md #### Importação de bibliotecas

# COMMAND ----------

# importando as bibliotecas

from bcb import sgs
import requests
import pandas as pd
import json
import datetime as dt
from datetime import timedelta

# COMMAND ----------

# MAGIC %md #### Construção das funções para coleta das API's e elaboração do Dataframe Spark

# COMMAND ----------

#Coletar a cotação do dólar,euro e btc (último fechamento)
#_____________________________________________________________
def cotacao_dolar(url=0):
    presentday = dt.date.today() 
    yesterday = presentday - timedelta(1)
    d=dt.date.strftime(yesterday,'%m-%d-%Y')
    url=f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{d}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"
    api_cotacoes= requests.get(url)
    json_cotacoes = api_cotacoes.json()
    pd.json_normalize(json_cotacoes)
    df = pd.read_json(url)
    cotacao_dolar= round(df["value"][0]['cotacaoCompra'],2)
    return cotacao_dolar

def cotacao_euro(url=0):
    presentday = dt.date.today() 
    yesterday = presentday - timedelta(1)
    d=dt.date.strftime(yesterday,'%m-%d-%Y')
    url=f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='EUR'&@dataCotacao='{d}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim"
    api_cotacoes= requests.get(url)
    json_cotacoes = api_cotacoes.json()
    pd.json_normalize(json_cotacoes)
    df = pd.read_json(url)
    cotacao_euro= round(df["value"][0]['cotacaoVenda'],2)
    return cotacao_euro

def cotacao_btc(url=0):
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
    cotacoes = cotacoes.json()
    cotacao_btc = cotacoes['BTCBRL']["bid"]
    return cotacao_btc
#_________________________________________________________________

#Traz a SELIC meta (mais recente)
def selic_meta(s=0):
    selic = sgs.get({'selic' : 432}, start = '2021-01-01')
    selic = selic['selic'].iloc[-1]
    return selic

#Traz a SELIC (acumulada em 12 meses)
def coleta_selic_12m(url=0):
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.13522/dados?formato=json'
    api_selic_12m= requests.get(url)
    json_selic_12m = api_selic_12m.json()
    pd.json_normalize(json_selic_12m)
    df = pd.read_json(url)
    selic_12m = df.iloc[-1]['valor']
    return selic_12m

#Traz o IGP-M do mês (mais recente)
def coleta_igpm_mes(url=0):
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados?formato=json'
    api_igpm_mes= requests.get(url)
    json_igpm_mes = api_igpm_mes.json()
    pd.json_normalize(json_igpm_mes)
    df = pd.read_json(url)
    igpm_mes = df.iloc[-1]['valor']
    return igpm_mes

#Coleta o IPCA do mês (mais recente)
def ipca_mes(i=0):
    ipca_mes = sgs.get({'ipca' : 433},start = '2021-01-01')
    ipca_mes = ipca_mes.reset_index()
    ipca_mes = ipca_mes['ipca'].iloc[-1]
    return ipca_mes

#Cria o df com os indices coletados
def df_cotacoes(d=0):
    df_dolar = pd.Series(cotacao_dolar(), name='dolar')
    df_euro = pd.Series(cotacao_euro(),name='euro')
    df_btc = pd.Series(cotacao_btc(),name='btc')
    selic = pd.Series(selic_meta(),name='juros_selic')
    ipca=pd.Series(ipca_mes(),name='ipca_mes')
    selic_acum_12m=pd.Series(coleta_selic_12m(),name='selic_acum_12m')
    igpm_mes=pd.Series(coleta_igpm_mes(),name='igpm_mes')
    df_cotacoes = pd.concat([df_dolar, df_euro, df_btc, selic, ipca,selic_acum_12m, igpm_mes], axis=1)
    return df_cotacoes

# COMMAND ----------

# MAGIC %md #### Conexão com SQL Server e carga do Dataframe na tabela

# COMMAND ----------

# criação do df spark com uso da função

df = df_cotacoes()
print(df)


# COMMAND ----------

# encapsulamento de dados sensíveis - usuário e senha


# COMMAND ----------

# carga na tabela SQL


# COMMAND ----------

