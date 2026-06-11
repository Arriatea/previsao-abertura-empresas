# Previsão de Abertura de Empresas

Projeto desenvolvido a partir de um case tecnico real anonimizado, com foco em analisar o mercado de abertura de empresas e construir uma projecao mensal para 2026.

O resultado final e um painel em Streamlit para apresentar, de forma simples, a estimativa de mercado e a meta de vendas necessaria para atingir 20% de market share.

Os dados e a identidade da organizacao analisada foram anonimizados para fins de portfolio.

## Acesse o painel

O app publicado no Streamlit esta disponivel em:

https://previsao-abertura-empresas.streamlit.app/

## Sobre este projeto

Este projeto teve origem em um case técnico desenvolvido para uma empresa real durante um processo de avaliação profissional. Para torná-lo adequado para publicação pública e apresentação em portfólio, todas as referências à organização, ao processo seletivo e a quaisquer informações potencialmente sensíveis foram removidas ou anonimizadas.

A versão disponibilizada neste repositório preserva integralmente a lógica analítica, as técnicas de tratamento de dados, a engenharia de atributos, os modelos de Machine Learning, as métricas de avaliação e os insights gerados durante o desenvolvimento original.

O objetivo desta adaptação é demonstrar competências em análise de dados, modelagem preditiva, visualização de informações e construção de soluções orientadas a dados, respeitando a confidencialidade da empresa envolvida.

Todo o código, estrutura analítica, documentação e implementação apresentados refletem o trabalho realizado pelo autor, com adaptações apenas para garantir a anonimização do contexto original.

## Objetivo do projeto

O projeto tem tres objetivos principais:

- analisar o historico de abertura de empresas;
- testar modelos preditivos e escolher uma abordagem para a projecao de 2026;
- apresentar os resultados.

## Descricao do problema

A organizacao analisada precisava estimar o volume de abertura de empresas em 2026 e transformar essa previsao em uma referencia mensal de vendas para buscar 20% de market share.

Com isso, o desafio analitico foi entender o historico, observar padroes de sazonalidade e testar uma abordagem preditiva que fosse simples de explicar e util para planejamento.

## Estrutura do projeto

```text
forecast_analytics/
|
|-- app.py
|-- README.md
|-- requirements.txt
|
|-- data/
|   `-- dados_anonimizados_2026.xlsx
|
|-- notebooks/
|   |-- analise_exploratoria.ipynb
|   |-- graficos_analise.ipynb
|   |-- modelagem.ipynb
|   `-- modelo_final.ipynb
|
`-- outputs/
    |-- historico_mensal.csv
    |-- previsao_2026_mensal.csv
    |-- tabela_market_share.csv
    |-- resumo_incerteza.csv
    `-- resumo_market_share.csv
```

## Principais arquivos

Esta secao resume o papel de cada arquivo importante do projeto. A ideia e facilitar a leitura, mostrando onde esta cada parte do raciocinio.

### Arquivos da raiz

#### `README.md`

Arquivo de apresentacao do projeto. Contem o objetivo do projeto, a estrutura das pastas, instrucoes de instalacao e o passo a passo para rodar o painel.

#### `requirements.txt`

Lista as bibliotecas necessarias para executar os notebooks e o app em Streamlit.

#### `app.py`

Aplicacao em Streamlit usada para apresentar os resultados finais. O app nao treina o modelo; ele apenas le os arquivos CSV ja gerados na pasta `outputs/`.

No painel aparecem:

- mercado projetado para 2026;
- meta anual para 20% de market share;
- media mensal de vendas necessaria;
- grafico de historico vs projecao;
- grafico de meta mensal de vendas;
- tabela mensal de 2026.

### Pasta `data/`

#### `data/dados_anonimizados_2026.xlsx`

Base anonimizada do desafio analitico. Ela contem o historico de abertura de empresas por ano, mes, cidade agrupada e segmento.

### Pasta `notebooks/`

#### `notebooks/analise_exploratoria.ipynb`

Notebook usado para entender a base, analisar sazonalidade, comparar periodos, cidades agrupadas e segmentos.

Ele funciona como a primeira etapa do projeto, antes da modelagem. O objetivo foi entender o comportamento do mercado e levantar pontos importantes para a apresentacao.

#### `notebooks/graficos_analise.ipynb`

Notebook com graficos exploratorios usados como apoio para a apresentacao.

Neste arquivo ficam visualizacoes mais diretas sobre serie historica, sazonalidade, participacao por cidade, participacao por segmento e volatilidade.

#### `notebooks/modelagem.ipynb`

Notebook de testes dos primeiros modelos. Nele foram comparadas abordagens mais simples, como Regressao Linear, com Random Forest, usando 2025 como periodo de validacao.

Esse notebook mostra o caminho ate a escolha do modelo final. Ele nao e o notebook principal do projeto, mas registra os testes e as limitacoes encontradas.

#### `notebooks/modelo_final.ipynb`

Notebook principal do projeto. Nele e treinado o modelo final, feita a projecao de 2026 e gerados os arquivos CSV usados pelo painel.

Ao final dele sao exportados os resultados para a pasta `outputs/`, que depois e usada pelo Streamlit.

### Pasta `outputs/`

#### `outputs/historico_mensal.csv`

Tabela com o historico mensal agregado de abertura de empresas.

#### `outputs/previsao_2026_mensal.csv`

Tabela com a previsao mensal de abertura de empresas para 2026.

#### `outputs/tabela_market_share.csv`

Tabela usada para calcular e apresentar a meta mensal de vendas para 20% de market share.

#### `outputs/resumo_incerteza.csv`

Tabela com a visao anual da faixa de incerteza operacional da projecao, incluindo limite inferior, previsao central e limite superior.

#### `outputs/resumo_market_share.csv`

Tabela resumida com os principais indicadores usados nos cards do painel.

## Dados utilizados

A base principal esta em:

```text
data/dados_anonimizados_2026.xlsx
```

As principais colunas utilizadas no projeto sao:

- `ano`
- `mes`
- `cidade_agrupada`
- `class_segmentos`
- `abertura_empresas`

## Instalacao

Recomendacao: usar um ambiente virtual para instalar as dependencias.

### 1. Criar ambiente virtual

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
```

### 2. Ativar ambiente virtual

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Quando ativado, o terminal deve mostrar algo como:

```text
(.venv) PS C:\...\forecast_analytics>
```

### 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

As principais bibliotecas usadas sao:

- Streamlit
- pandas
- numpy
- scikit-learn
- matplotlib
- plotly
- openpyxl

## Principais analises

As analises foram separadas em etapas para facilitar o raciocinio:

- leitura e entendimento da base historica;
- analise de sazonalidade por ano e mes;
- comparacao de periodos antes, durante e depois da pandemia;
- leitura por cidade agrupada e segmento;
- testes de modelagem usando 2025 como periodo de validacao;
- projecao mensal de 2026 e traducao da previsao em meta para 20% de market share.

## Modelo preditivo

O modelo final escolhido foi um Random Forest com variaveis historicas.

Antes de treinar com toda a base, usei 2025 como teste para ter uma nocao do erro mensal. Depois disso, o modelo foi treinado com o historico completo disponivel para gerar a projecao de 2026.

## Metricas

Usei MAE para ver o erro medio em quantidade de empresas e WMAPE para ter uma leitura percentual que da mais peso aos grupos com maior volume.

Na validacao mensal de 2025, o Random Forest com variaveis historicas teve WMAPE de aproximadamente 8,83%. Essa taxa tambem foi usada como uma margem simples para montar a faixa de incerteza operacional da projecao.

## Como gerar os arquivos do painel

Antes de abrir o app, rode o notebook final:

```text
notebooks/modelo_final.ipynb
```

Esse notebook gera os arquivos:

```text
outputs/historico_mensal.csv
outputs/previsao_2026_mensal.csv
outputs/tabela_market_share.csv
outputs/resumo_incerteza.csv
outputs/resumo_market_share.csv
```

Esses arquivos sao a base do painel em Streamlit.

## Como rodar o painel

Com o ambiente virtual ativado, rode:

```powershell
streamlit run app.py
```

Ou, se preferir chamar diretamente pela `.venv`:

```powershell
.\.venv\Scripts\streamlit.exe run app.py
```

Depois abra no navegador:

```text
http://localhost:8501
```

## O que aparece no painel

O painel apresenta:

- mercado projetado para 2026;
- meta anual para 20% de market share;
- media mensal de vendas necessaria;
- grafico de historico mensal vs projecao de 2026;
- grafico da projecao de 2026 com faixa de incerteza;
- grafico da meta mensal de vendas;
- tabela mensal com mercado projetado e meta de vendas.

## Comando rapido

Depois que as dependencias estiverem instaladas e os CSVs ja tiverem sido gerados:

```powershell
.\.venv\Scripts\streamlit.exe run app.py
```
