### Este projeto realiza a extração de cotações, moedas e dados macroeconômicos de API's do Banco do Brasil, Awesome API e SGS, compilando estes dados num dataframe.

### O script coleta dados das seguintes APIs:

**API do Banco Central do Brasil (BCB)**: O script faz uso da API do Banco Central do Brasil para coletar a cotação do dólar, euro e a taxa Selic. A API do BCB é acessada através do pacote bcb em Python. As funções cotacao_dolar(), cotacao_euro() e selic_meta() fazem solicitações a essa API para obter as informações necessárias.

**API AwesomeAPI**: O script faz uso da API AwesomeAPI para coletar a cotação do Bitcoin. A API AwesomeAPI é acessada através do endpoint https://economia.awesomeapi.com.br/last/BTC-BRL.

**API do BCB (SGS)**: O script faz uso da API do BCB para coletar a taxa Selic acumulada em 12 meses, o Índice Geral de Preços ao Consumidor (IGP-M) do mês e o Índice Nacional de Preços ao Consumidor (IPCA) do mês. As funções coleta_selic_12m(), coleta_igpm_mes() e ipca_mes() fazem solicitações a essa API para obter as informações necessárias 

Este repositório contém um script Python que coleta dados de várias APIs e os armazena em um DataFrame do pandas. O script é executado dentro de um contêiner Docker, que pode ser construído a partir da imagem eltonguilherme15186/repo:v1.0.

### Dependências
O script requer as seguintes bibliotecas Python:

`requests`: para fazer solicitações HTTP para as APIs.

`pandas`: para manipular e analisar os dados coletados.

`json`: para manipular os dados JSON retornados pelas APIs.

`datetime`: para trabalhar com datas e horários.

`bcb`: para acessar os dados do Banco Central do Brasil.

`lxml`: para manipular dados XML.

### Funções Principais
O script define várias funções para coletar dados de diferentes APIs:

`cotacao_dolar()`: coleta a cotação do dólar.

`cotacao_euro()`: coleta a cotação do euro.

`cotacao_btc()`: coleta a cotação do Bitcoin.

`selic_meta()`: coleta a meta da taxa Selic.

`coleta_selic_12m()`: coleta a taxa Selic acumulada em 12 meses.

`coleta_igpm_mes()`: coleta o Índice Geral de Preços ao Consumidor (IGP-M) do mês.

`ipca_mes()`: coleta o Índice Nacional de Preços ao Consumidor (IPCA) do mês.

### DataFrame de Cotacoes
O script define a função df_cotacoes() para criar um DataFrame do pandas com as cotacoes coletadas. O DataFrame resultante contém as seguintes colunas:

`dolar`: cotação do dólar.

`euro`: cotação do euro.

`btc`: cotação do Bitcoin.

`juros_selic`: meta da taxa Selic.

`ipca_mes`: IPCA do mês.

`selic_acum_12m`: taxa Selic acumulada em 12 meses.

`igpm_mes`: IGP-M do mês.

O script armazena os dados coletados em um DataFrame do pandas usando a função **pd.concat()**. A função **pd.concat()** é usada para concatenar várias séries ou dataframes ao longo de um eixo especificado 1.

No script, a função **df_cotacoes()** cria um DataFrame do pandas com as cotacoes coletadas. A função primeiro chama as funções **cotacao_dolar()**, **cotacao_euro()**, **cotacao_btc()**, **selic_meta()**, **coleta_selic_12m()**, **coleta_igpm_mes()** e **ipca_mes()** para coletar os dados. Cada uma dessas funções retorna um valor que é armazenado em uma série do pandas.

Em seguida, a função **pd.concat()** é usada para concatenar todas essas séries em um único DataFrame. O DataFrame resultante tem uma coluna para cada série e uma linha para cada data de coleta de dados. A função **pd.concat()** é chamada com o argumento axis=1, o que significa que as séries são concatenadas ao longo do eixo das colunas 2.

### Execução do Script
Para executar o script, você pode usar o seguinte comando:

```docker pull eltonguilherme15186/repo:v1.0```

Isso irá puxar a imagem Docker necessária para executar o script e, em seguida, você pode executar o script dentro de um contêiner Docker.
