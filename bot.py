import config
import telebot
from telebot import types
import wikipedia
from collections import defaultdict, deque

def deque_10():
	return deque([], 10)


bot = telebot.TeleBot(config.token)

users_history = defaultdict(deque_10)

user = bot.get_me()

history_template = 'Your last 10 request:\n{}'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Input word or phrase and get link to wiki page!")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Input '/start' or '/history'")


@bot.message_handler(commands=['history'])
def send_history(message):
	bot.send_message(message.chat.id, history_template.format(
		'\n'.join(list(users_history[user.id]))
		)
	)


@bot.message_handler(content_types=["text"])
def return_wiki_pages(message):
	wiki_links = wikipedia.search(message.text, results=4)
	print(wiki_links, len(wiki_links))
	try:
		wiki_page = wikipedia.page(wiki_links[0]).url
		users_history[user.id].append(wiki_page)
		markup = types.ReplyKeyboardMarkup()
		itembtna = types.KeyboardButton(wikipedia.page(wiki_links[1]).title)
		itembtnb = types.KeyboardButton(wikipedia.page(wiki_links[2]).title)
		itembtnc = types.KeyboardButton(wikipedia.page(wiki_links[3]).title)
		markup.row(itembtna, itembtnb, itembtnc)
	except wikipedia.exceptions.DisambiguationError:
		wiki_page = 'Please input more clear phrase!'
		markup = types.ReplyKeyboardRemove(selective=False)
	bot.send_message(message.chat.id, wiki_page, reply_markup=markup)

if __name__ == '__main__':
     bot.polling(none_stop=True)
     a=1
	test='qweqwesdasdaddsdsasklflqweqwesdasdaddsdsasklfldakskslslsslsllslslslslslslslsslssllsslalls;sas;lss;as'
