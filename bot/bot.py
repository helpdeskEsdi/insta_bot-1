from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from instagram.profiles import get_num_followers
from bot.telegram_utils import send_followers
from instagram.track_followers import create_report
from instagram.login import load_cookies, open_login
from telegram_utils import send_followers_report

token = '7614189700:AAGZV6cnbtRGmOChSF4txBajQ61KfWjVUfY'
bot_chatID = '8024601173'

driver = open_login()

def track (update): 
    
    load_cookies(driver)

    num_followers = get_num_followers()
    
    new_followers, unfollows = create_report(num_followers)
    send_followers(token, bot_chatID , num_followers, new_followers, unfollows)
     
    # Responder al usuario de Telegram
    update.message.reply_text(f"📊 **Seguidores Report**\n\n"
                              f"**Seguidores actuales:** {num_followers}\n"
                              f"**Seguidores nuevos:** {new_followers}\n"
                              f"**Seguidores perdidos:** {unfollows}")
    


#COMANDO PARA ENVIAR EXCEL DE SEGUIDORES
def report (update):

    send_followers_report(token, bot_chatID)



def main():


    application = Application.builder().token(token).build()
    

    # Manejar el comando /track
    track_handler = CommandHandler('track', track)
    application.add_handler(track_handler)

    report_handler = CommandHandler('report', report)
    application.add_handler(report_handler)

    # Empezar el bot
    application.start_polling()
    application.idle()


if __name__ == '__main__':
    main()