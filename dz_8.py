#Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
def zadacha_1():
    import telebot
    bot = telebot.TeleBot('5611683928:AAFaqVZP2bWGwfPetaOKbj60QnrQ_iUw3y0')
    @bot.message_handler(commands=['техподдержка'])
    def send_welcome(message):
        bot.send_message(message.from_user.id,
                     f'Здравствуйте {message.from_user.first_name}, это бот техподдержки. ')
    @bot.message_handler(content_types=['text'])
    def request(message):
        text = message.text
        if text != '':
            with open('text.txt', 'a', encoding='utf-8') as data:
                text = f'{message.from_user.id}: {message.text}\n'
                data.write(f'{text}')
    bot.polling()
# Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.
def zadacha_2():
    import telebot
    bot = telebot.TeleBot('5611683928:AAFaqVZP2bWGwfPetaOKbj60QnrQ_iUw3y0')
    @bot.message_handler(commands=['ответ'])
    def send_welcome(message):
        bot.send_message(message.from_user.id,
                     f'Здравствуйте {message.from_user.first_name} ')
    @bot.message_handler(content_types=['text'])
    def request(message):
        text = message.text
        if text != 'ok':
            with open('text.txt', 'r', encoding='utf-8') as file:
                request = file.read().replace('\n', ':').split(':')    
            answer = 'Все будет хорошо!'
            bot.send_message(request[0], f'Вы спрашивали: {request[1]}')
            bot.send_message(request[0], f'Ответ: {answer}')
    bot.polling()
 