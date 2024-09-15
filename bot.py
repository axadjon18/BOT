from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# Bot tokenini kiriting
TOKEN = '7374096561:AAE30WHvVbuV9acxLshJ2DBDmKMWckpibn4'

# Tugmalar bilan menyu
def build_main_menu():
    keyboard = [
        ['Mening ismim Ahmad siznikichi?'],
        ['/start', '/help'],
        ['/salom', 'Meni xabar yuborish']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


    
# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = build_main_menu()
    await update.message.reply_text('Assalomu alekum!', reply_markup=reply_markup)

# /help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = build_main_menu()
    await update.message.reply_text(
        'Qo\'llanma:\n'
        '/start - Botni ishga tushuradi\n'
        '/help - Yordam bo\'yicha ma\'lumot\n'
        '/salom - Salom berish',
        reply_markup=reply_markup
    )

# /salom komandasi
async def salom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = build_main_menu()
    await update.message.reply_text('Assalomu alekum!', reply_markup=reply_markup)

# Matnli xabarlarni qayta ishlash
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    await update.message.reply_text(f" {user_message}: bu xabar hali bizga nomalum bu xabar ustida ishlamoqdamiz!") 

# Xatoliklarni qayta ishlash
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error(f'Xatolik: {context.error}')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Komandalarni qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("salom", salom))

    # Matnli xabarlarni qayta ishlash
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Xatoliklarni qayta ishlash
    application.add_handler(MessageHandler(filters.ALL, error_handler))

    # Hujjatlar va xatoliklarni ko‘rsatadigan logging qo‘shing 
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    application.run_polling()

if __name__ == '__main__':
    main()
