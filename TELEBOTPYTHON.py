from typing import Final
from telegram.ext import Update
from telegram.ext import Application , CommandHandler, MessageHandler, filters, ContextTypes


TOKEN : Final = "7158425331:AAEj9XZh6MtikPXaUTW9BIUrI8RaGcTvU3s"
BOT_USERNAME = "@yoniChatBot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text("Hello, thanks for chatting with me")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text("help command")
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text("custom command")
    
    
def handle_response(text : str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'hello there'
    
    if 'how are you' in processed:
        return 'good'
    


async def handle_message(update : Update , context: ContextTypes.DEFAULT_TYPES):
    message_type: str = update.message.chat.type
    text : str = update.message.text
    
    print(f"user {update.message.chat.id} in {message_type}: {text}")
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            text : str = text.replace(BOT_USERNAME, '')
            response : str = handle_response(text)
            await update.message.reply_text(response)
        else:
            print('not for me')
    else:
        response : str = handle_response(text)
        await update.message.reply_text(response)
        
    print('response sent' ,  response)
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPES):
    print(f"Update {update} caused error {context.error}")
    
if __name__ == "__main__":
    print("starting ...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    
    
    app.add_handler(MessageHandler(filters.TEXT , handle_message))
    
    
    app.add_error_handler(error)
    
    
    print("polling ...")
    app.run_polling(poll_interval=1.0)

    
    
    
    
    
    
    
    
    
    