import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from bashterminal import BashTerminal

#Introduce here the token given by bot father
TOK = 'A'
#Introduce here your user id (you can get it from the bot)
usr_id = 0

terminal = BashTerminal();
def main():
    #Initiate the bot
    bot = telegram.Bot(token=TOK);
    #Stablish handlers
    updater = Updater(token=TOK);
    dispatcher = updater.dispatcher;
    dispatcher.add_handler(CommandHandler('start',start))
    dispatcher.add_handler(CommandHandler('userid',userid))
    dispatcher.add_handler(MessageHandler(Filters.text, command_reception));
    #Bot starts working
    updater.start_polling();

    print "Bot initiated"
    updater.idle();
    return;

def start(bot, update):
    msg="Terminal bot :)"
    bot.send_message(chat_id=update.message.chat_id, text=msg);
    return;

def userid(bot, update):
    msg="Your telegram user id is "+ str(update.message.from_user.id);
    bot.send_message(chat_id=update.message.chat_id, text=msg);
    return;

def command_reception(bot, update):
    # My usr id :) so just I can execute commands on my pc
    if(update.message.from_user.id != usr_id):
        bot.send_message(chat_id=update.message.chat_id, text="You cant use this bot.\n");
        return;

    response = terminal.ex_command(update.message.text);
    # Messages cannot be longer than 4096 chars
    while len(response) > 0:
        bot.send_message(chat_id=update.message.chat_id, text=response[0:4000]);
        response=response[4000:]
    return;


if __name__ == "__main__":
    main();
