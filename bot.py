from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "BU_YERGA_BOT_TOKENINGIZNI_QO'YASIZ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚗 Inoyat Motors Bot ga xush kelibsiz!\n\n"
        "Tez orada bu yerda avtomobillarni qidirish, sotish va sotib olish imkoniyati bo'ladi."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
