from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text("Salom")


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
