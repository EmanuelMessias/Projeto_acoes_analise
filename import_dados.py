import yfinance as yf
import sqlite3 as sql
import schedule 
import time

ticker_NVDA = "NVDA"
ticker_INTC = "INTC",
ticker_AMD = "AMD", 
ticker_Gigabyte = "2376.TW"

#data = yf.download(tickers, group_by='ticker', auto_adjust=True )


def update_data(ticker, db_name):
    # Baixar os dados do Yahoo Finance
    data_export = yf.download(ticker, start='2020-01-01', end='2024-09-18')
    data_export.reset_index(inplace=True)
    
    # Conectar ao banco de dados SQLite e salvar os dados
    conn = sql.connect(db_name)
    data_export.to_sql('stock_data', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"Dados da {ticker} exportados com sucesso", flush=True)

#Essa comando agenda uma tarefa, chamando de volta minha função (update_date), sempre as 9am
# schedule.every().day.at("09:00").do(update_data_nvda, update_data_intc, update_data_amd, update_data_gigabyte)
schedule.every().day.at("09:00").do(update_data, ticker="NVDA", db_name="acoes_data_nvidia.db")
schedule.every().day.at("09:00").do(update_data, ticker="INTC", db_name="acoes_data_intel.db")
schedule.every().day.at("09:00").do(update_data, ticker="AMD", db_name="acoes_data_amd.db")
schedule.every().day.at("09:00").do(update_data, ticker="2376.TW", db_name="acoes_data_gigabyte.db")

# Loop infinito para manter o agendador ativo
while True:
    schedule.run_pending()
    print('Aguardando Tarefa')
    time.sleep(60) #Espera um minuto até verificar se há uma tarefa pendente
