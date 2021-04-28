import telebot
import random
from telebot import types
import db
import pytils


bot = telebot.TeleBot("1722107740:AAEtj-GTFcHE1tNOelksf2vK4RD6-E35nao")

#Клавиатуры
keyb_start = types.ReplyKeyboardMarkup(resize_keyboard = True)
keyb_start.row("Начать")

keyb_gen = types.ReplyKeyboardMarkup(resize_keyboard = True)
keyb_gen.row("Сгенерировать")

#Бот
@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, "Привет!, я генерирую радномные данные для фб", reply_markup = keyb_gen)
	
@bot.message_handler(content_types = 'text')
def randomer(message):
	if message.text != 'Сгенерировать':
		bot.send_message(message.chat.id, "Ошибка, нажмите на кнопку 'Сгенерировать'")
		return random_start(message)
	else:
		#Имя, фамилия
		firstname = db.namelist[random.randint(0,len(db.namelist) - 1)]
		surname = db.surnamelist[random.randint(0, len(db.surnamelist) - 1)]
		name = firstname + ' ' + surname
		#Дата
		day = random.randint(1,28)
		month = random.randint(1,12)
		year = random.randint(1989,2000)
		date = '<code>' + str(day) + '.' + str(month) + '.' + str(year) + '</code>'
		#Логин
		nums = '1234567890'
		chars = 'abcdefghijklnopqrstuvwxyz'
		nametrans = pytils.translit.translify(firstname.lower())
		surnametrans = pytils.translit.translify(surname.lower())
		demologin = ''
		for i in range(2):
			demologin += nametrans[i]
		
		login = 'Логин: ' + '<code>' + demologin + '.' + surnametrans + str(random.randint(10,99)) + '</code>'
		
		#Пароль
		nums = '1234567890'
		chars = 'abcdefghijklnopqrstuvwxyz'
		charname = ''
		numname = ''
		for i in range(6):
			charkey= pytils.translit.translify(surname.lower())
			charname += charkey[i - 1]
		for i in range(2):
			charname += random.choice(nums)									
		password = 'Пароль: ' + '<code>' + charname + '</code>'
				
		#Компания ворк
		company = random.choice(db.company)
		
		#Должность
		position = random.choice(db.position)
      
	bot.send_message(message.chat.id, name + "\n" + date + "\n" + login + "\n" + password + '\n' + company + '\n' + position, parse_mode = 'HTML')
      	
    	
		





if __name__ == '__main__':
    bot.polling(none_stop=True)