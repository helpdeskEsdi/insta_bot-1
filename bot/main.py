from telegram import Update
from instagram.login import load_cookies, open_login
from telegram.ext import Updater, CommandHandler, CallbackContext
from instagram.profiles import get_num_followers
from bot.telegram_utils import send_followers
from instagram.track_followers import create_report

token = '7614189700:AAGZV6cnbtRGmOChSF4txBajQ61KfWjVUfY'
bot_chatID = '8024601173'
driver = open_login()

def track (update: Update, context: CallbackContext): 
    
    load_cookies(driver)
    num_followers = get_num_followers()

    new_followers, unfollows = create_report(num_followers)

    send_followers(token, bot_chatID , num_followers, new_followers, unfollows)
     
    # Responder al usuario de Telegram
    update.message.reply_text(f"📊 **Seguidores Report**\n\n"
                              f"**Seguidores actuales:** {num_followers}\n"
                              f"**Seguidores nuevos:** {new_followers}\n"
                              f"**Seguidores perdidos:** {unfollows}")
    
    
def main():


    updater = Updater(token, use_context=True)
    
    dispatcher = updater.dispatcher

    # Manejar el comando /track
    track_handler = CommandHandler('track', track)
    dispatcher.add_handler(track_handler)

    # Empezar el bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()