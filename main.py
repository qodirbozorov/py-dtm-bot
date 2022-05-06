import json

from telegram.ext import Updater, CommandHandler


user = {
    "name": "Qodir",
    'origin': 'Najot talim',
    "phone": '+998990545606',
    "yunalishlar": [{'nomi': "XTA", 'otm': 'inyaz', 'mvdir': "55685425"}, {'nomi': "XTA", 'otm': 'inyaz', 'mvdir': "55685425"}, {'nomi': "XTA", 'otm': 'inyaz', 'mvdir': "55685425"}, {'nomi': "XTA", 'otm': 'inyaz', 'mvdir': "55685425"}, {'nomi': "XTA", 'otm': 'inyaz', 'mvdir': "55685425"}],
    'id': '0008'
}

samdtu = {}


def start(update, context):
    update.message.reply_text(F"{samdtu['yunalishlar']}")


with open('vuz-data.json') as json_file:
    data = json.load(json_file)

    samdtu = data[0]
    # for reading nested data [0] represents
    # the index value of the list

    # for printing the key-value pair of
    # nested dictionary for loop can be used


def main():
    # Uodater
    updater = Updater(
        "5358446083:AAF0FxxdxJivuBQ5qOdzSwkJwr8vZxgiE-8", use_context=True)

    # dispatcher event
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


main()
