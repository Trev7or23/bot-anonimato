import telebot
import csv

# Crea una instancia del bot con tu token de acceso
TOKEN = 'AGREGA TU TOKEN AQUI'
bot = telebot.TeleBot(TOKEN)

# usamos /start para loguear el usuario
@bot.message_handler(commands=['start'])
def start (message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Bienvenido, escribe con tus amigos")

    with open('users.csv', 'r+', newline='') as users:
        users_read = csv.reader(users) 
        exist = False

        for user in users_read:
            if chat_id == int(user[0]):
                exist = True
                break
        if not exist:
            users_add = csv.writer(users)
            users_add.writerow([chat_id])

# cuando un usuario escriba le mandamos el sms a todo excepto a el mismo usuario        
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id

    with open('users.csv', 'r') as users:
        users_file = csv.reader(users)
        for user in users_file:
            if int(user[0]) != chat_id:
                bot.send_message(int(user[0]), message.text)


if __name__ == "__main__":
    # Inicia el bot
    bot.polling()
