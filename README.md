

---

# 📈 Análise de Ações com Python e APIs Financeiras

Eu desenvolvi este projeto para coletar, armazenar e analisar dados históricos de ações de empresas utilizando uma API financeira. Com ele, automatizei a análise de dados para facilitar a interpretação de tendências do mercado de ações, aplicando cálculos estatísticos e técnicas de média móvel. Este projeto oferece insights práticos sobre o comportamento das ações de diferentes empresas ao longo do último ano.

## 🗂️ Resumo do Projeto

Neste projeto, integrei Python a APIs financeiras, como o Yahoo Finance (yfinance) ou Alpha Vantage, para coletar dados diários de ações. Após a coleta, fiz uma análise exploratória com cálculos de métricas financeiras básicas e identifiquei padrões de tendência usando cruzamentos de médias móveis. Para facilitar o acesso e reutilização dos dados, armazenei-os em um banco de dados SQLite e também em arquivos CSV.

## 🔍 Objetivos e Funcionalidades

- **Coleta de Dados Financeiros**: Busquei dados históricos de ações de cinco empresas distintas, incluindo informações como preço de fechamento e volume de negociação, cobrindo o último ano com atualização diária.
- **Armazenamento de Dados**: Organizei e salvei os dados em um banco de dados SQLite e arquivos CSV, separados por empresa.
- **Análise de Dados**:
  - **Média Móvel Simples (SMA)**: Calculei SMAs para analisar flutuações médias de preços em diferentes períodos, como 50 dias e 200 dias.
  - **Desvio Padrão e Volatilidade**: Mensurei a volatilidade de cada ação, destacando o risco e estabilidade do ativo.
  - **Identificação de Tendências**: Analisei cruzamentos de médias móveis para detectar sinais de alta ou baixa, identificando tendências de mercado.

## 🚀 Ferramentas e Tecnologias Utilizadas

- **Python**: Linguagem escolhida para a coleta, análise e visualização de dados.
- **APIs Financeiras**: Utilize `yfinance` ou `Alpha Vantage` para acesso rápido aos dados históricos das ações.
- **SQLite**: Banco de dados leve e eficiente para armazenamento e consulta dos dados.
- **Pandas e NumPy**: Manipulação e cálculo de dados de forma otimizada.
- **Matplotlib e Seaborn**: Visualizações e gráficos de tendências de maneira clara e acessível.

## 📊 Metodologia

1. **Coleta de Dados**: Conectei o projeto à API financeira para coletar dados históricos diários de cada empresa selecionada.
2. **Processamento de Dados**: Limpei e organizei os dados para garantir sua consistência antes da análise.
3. **Cálculo de Métricas Financeiras**:
   - **Média Móvel Simples (SMA)**: Calculei para períodos variados, o que me permitiu observar tendências de curto e longo prazo.
   - **Desvio Padrão**: Avaliei a variação diária dos preços para mensurar a volatilidade.
4. **Identificação de Tendências**:
   - **Cruzamento de Médias Móveis**: Identifiquei pontos de alta ou baixa com base no cruzamento das médias móveis de 50 e 200 dias.
5. **Armazenamento dos Resultados**: Salvei todos os dados e métricas em um banco de dados SQLite e também em arquivos CSV, organizados por empresa para facilitar o acesso.

## 📈 Exemplo de Análise

Para cada ação, gerei gráficos que mostram as médias móveis de 50 e 200 dias junto aos preços diários. Sinalizei cruzamentos de médias móveis para indicar tendências de alta e baixa, fornecendo uma ferramenta útil para observar o comportamento das ações ao longo do ano e identificar pontos de entrada e saída de investimentos.



## 🤝 Contribuição

Feedbacks são bem-vindos! Este projeto é pessoal, mas estou aberto a sugestões e melhorias.

---
