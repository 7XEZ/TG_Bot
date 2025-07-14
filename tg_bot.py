# -*- coding: utf-8 -*-
import telebot
from telebot import types
from groq import Groq
# Замените 'YOUR_API_KEY' на ключ вашего бота, полученный от BotFather
bot = telebot.TeleBot('7857799746:AAEdk-QpscOKMmiZRt2F2k7DoGjQSP1NUdU')

client = Groq(api_key="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")#замените api_key на свой

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Привет! Можешь спрашивать меня! Что тебя интересует?')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  messages = [{"role": 'user', "content": message.text}]
  response = client.chat.completions.create(model='llama3-70b-8192', messages=messages, temperature=0)
  bot.send_message(message.from_user.id, response.choices[0].message.content)

# Запуск бота

bot.polling()
memory_usage()
