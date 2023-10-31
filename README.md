# Objetivos do Projeto

O projeto terá:

- WebScrapper: Preencherá um banco com dados em intevalos predefenidos;

- API: Executará no banco queries para extrair e interprepar os dados presentes no banco;

- Uma interface em Next.JS: para visualização de dados tabulares e gráficos

- (Opcional) Aplicação Python para uso local

# Estruturas - Ações

## Dados Empresa

- nome - **NOT NULL**

- cnpj - **NOT NULL**

- ano de fundação - **NOT NULL**

- setor

- segmento

## Cotacao

- timestamp - **NOT NULL**

- valor - **NOT NULL**

## Estatisticas

- trimestre - **NOT NULL**

- ano - **NOT NULL**

- receita liquida

- ebita

- ebit

- imposto

- divida bruta

- divida liquida

- lucro liquido

- lucro bruto

- custo

- margem bruta

- margem ebita

- margem liquida

- roe

- roa 

- roic

- pl

- growth5y

- p/vp

- dy

- free float

- tag alone

- lpa

- vpa

# Estruturas - FIIS

## Dados FIIs

- nome - **NOT NULL**

- segmento - **NOT NULL**

- publico alvo - **NOT NULL**

- tipo de fundo - **NOT NULL**

- gestão - **NOT NULL**

## Cotação

- timestamp - **NOT NULL**

- valor - **NOT NULL**

## Estatisticas

- mes - **NOT NULL**

- ano - **NOT NULL**

- p/vp - **NOT NULL**

- mandato - **NOT NULL**

- duração - **NOT NULL**

- dy12m

- liquides diaria

- valorização

- taxa administrativa

- dy5anos

- vacancia

- valor patrimonial

- ultimo rendimento

- qntd imoveis
