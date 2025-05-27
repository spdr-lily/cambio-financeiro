# **Projeto de Câmbio Financeiro**

## **1\. Introdução**

O objetivo do projeto é demonstrar a manipulação de dados de preços de produtos em diferentes moedas e a capacidade de adicionar novas conversões monetárias a um conjunto de dados existente.

**2\. Bibliotecas Utilizadas**

O projeto faz uso da seguinte biblioteca Pandas, uma biblioteca flexível para análise e manipulação de dados em Python.

A biblioteca foi importada no início do projeto com o comando "import pandas as pd".

## **3\. Conjunto de Dados Inicial**

O ponto de partida do projeto é um conjunto de dados fictício, criado como um dicionário. Este dicionário contém informações sobre três produtos (Produto A, Produto B, Produto C) e seus respectivos preços em três moedas: Dólar Americano (USD), Euro (EUR) e Iene Japonês (JPY).

dados\_cambio \= {'Produto':\['Produto A','Produto B','Produto C'\],  
                'Preco USD': \[100,150,200\],  
                'Preco EUR':\[85,125,170\],  
                'Preco JPY':\[10000,15000,20000\]  
               }

Para facilitar a manipulação e análise, este dicionário foi convertido em um DataFrame do Pandas com o comando: df\_cambio \= pd.DataFrame(dados\_cambio)

A estrutura inicial do DataFrame df\_cambio é a seguinte:

| Produto | Preco USD | Preco EUR | Preco JPY |
| :---- | :---- | :---- | :---- |
| Produto A | 100 | 85 | 10000 |
| Produto B | 150 | 125 | 15000 |
| Produto C | 200 | 170 | 20000 |

## **4\. Função de Conversão de Câmbio**

Uma função auxiliar, conversao\_para\_usd, foi definida para realizar a conversão de um preço de uma moeda para Dólar Americano (USD), dado um preço e uma taxa de câmbio.

def conversao\_para\_usd(preco, taxa):  
    return preco / taxa

**O que a Função Faz:**

* A função conversao\_para\_usd converte um valor monetário de uma moeda para Dólar Americano (USD).  
* Ela recebe dois argumentos:  
  * preco: O valor na moeda original que você deseja converter.  
  * taxa: A taxa de câmbio entre a moeda original e o USD.  
* Ela realiza uma divisão simples: preco / taxa. O resultado dessa divisão é o valor equivalente em USD.  
* Ela retorna o valor em USD.

Esta função é genérica e pode ser aplicada a qualquer preço e taxa, embora no contexto do projeto ela não seja diretamente utilizada para adicionar novas colunas de moeda ao DataFrame, que é feito com uma abordagem diferente (funções lambda).

**5\. Taxas de Câmbio Definidas**

As taxas de câmbio para as moedas USD, EUR e JPY são armazenadas em um dicionário. A taxa para USD é 1, indicando que é a moeda base para as conversões implícitas no projeto.

taxa \= {'USD':1, 'EUR':1.2,'JPY':0.009}

Isso significa:

* 'USD': 1: 1 USD \= 1 USD (o USD é a moeda base)  
* 'EUR': 1.2: 1 EUR \= 1.2 USD  
* 'JPY': 0.009: 1 JPY \= 0.009 USD

A função conversao\_para\_usd espera que a taxa seja o valor de 1 unidade da moeda original em relação ao USD.

## **6\. Adicionando Preços em Libras Esterlinas (GBP)**

Uma das funcionalidades do projeto é a adição de uma nova coluna ao DataFrame, Preco GBP, que representa o preço dos produtos em Libras Esterlinas. Esta conversão é realizada a partir do Preco USD utilizando uma função lambda e o método .apply() do Pandas. A taxa de conversão utilizada é de 1.4 (ou seja, 1 USD \= 1.4 GBP).

df\_cambio\['Preco GBP'\] \= df\_cambio\['Preco USD'\].apply(lambda x: x \* 1.4)

## **7\. Resultado Final do DataFrame**

Após a adição da coluna Preco GBP, o DataFrame df\_cambio apresenta a seguinte estrutura e dados:

| Produto | Preco USD | Preco EUR | Preco JPY | Preco GBP |
| :---- | :---- | :---- | :---- | :---- |
| Produto A | 100 | 85 | 10000 | 140.0 |
| Produto B | 150 | 125 | 15000 | 210.0 |
| Produto C | 200 | 170 | 20000 | 280.0 |
