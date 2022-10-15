# Solicitação de Cotação de moeda criando um bot no Telegram e fazendo um deploy da solução no heroku.

import telebot

import requests

# solicitando a cotação do euro pela API

request_euro = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
request_dictionary1 = request_euro.json()
eur = float(request_dictionary1['EURBRL']['bid'])

request_dolar = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
request_dictionary2 = request_dolar.json()
usd = float(request_dictionary2['USDBRL']['bid'])

request_bitcoin = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
request_dictionary3 = request_bitcoin.json()
btc = float(request_dictionary3['BTCBRL']['bid'])


token = "5615586690:AAH8WipKH2MXTPs708AN7dIC4E2nWl_o5PE"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["dolar"])
def dolar(msg):
    bot.send_message(msg.chat.id, f"Cotação do Dólar hoje: R$ {usd}")

@bot.message_handler(commands=["euro"])
def euro(msg):
    bot.send_message(msg.chat.id, f"Cotação do Euro hoje: R$ {eur}")

@bot.message_handler(commands=["bitcoin"])
def bitcoin(msg):
    bot.send_message(msg.chat.id, f"Cotação do Bitcoin hoje: R$ {btc}")

@bot.message_handler(commands=["cotacao"
                               ""])
def opcao1(msg):
    texto = """
    Qual cotação você precisa?
    /dolar Dólar
    /euro Euro
    /bitcoin Bitcoin"""
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=["cotacao"])
def opcao2(msg):
    bot.send_message(msg.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@balbalba.com")

@bot.message_handler(commands=["cotacao"])
def opcao3(msg):
    bot.send_message(msg.chat.id, "Valeu! Lira mandou um abraço de volta")

def verify(msg):
    return True

@bot.message_handler(func=verify)
def responder(msg):
    texto = """
    Aperte opção para continuar:
     /cotacao
"""
    bot.reply_to(msg, texto)

bot.polling()
