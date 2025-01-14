from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from instagram.login import open_login, load_cookies
from instagram.profiles import get_num_followers
from bot.telegram_utils import send_followers_report  # Importa estas funciones desde el módulo correspondiente

# Comando para responder a /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(f"¡Hola, {user.first_name}! Soy tu bot. ¿En qué puedo ayudarte?")

# Comando para responder a /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/start - Iniciar el bot\n"
        "/help - Ver esta ayuda\n"
        "/track - Realizar seguimiento de seguidores\n"
        "/report - Enviar un reporte de seguidores"
    )

# Comando para /track
async def track(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        driver = open_login()
        load_cookies(driver, cookies_file="cookies.json", use_json=True)
        followers = get_num_followers(driver)
        await update.message.reply_text(f"Seguimiento completado. Número de seguidores: {followers}")
    except Exception as e:
        await update.message.reply_text(f"Error en el seguimiento: {e}")

# Comando para /report
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        token = "YOUR_TOKEN_HERE"  # Reemplaza con tu token
        chat_id = "YOUR_CHAT_ID_HERE"  # Reemplaza con tu chat ID
        send_followers_report(token, chat_id)
        await update.message.reply_text("Reporte de seguidores enviado exitosamente.")
    except Exception as e:
        await update.message.reply_text(f"Error al enviar el reporte: {e}")


def main():

    TOKEN = "7614189700:AAGZV6cnbtRGmOChSF4txBajQ61KfWjVUfY"
    
    # Crear la aplicación del bot
    application = Application.builder().token(TOKEN).build()
    
    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("track", track))
    application.add_handler(CommandHandler("report", report))
    
    # Iniciar el bot
    print("Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling()

if __name__ == "__main__":
    main()
