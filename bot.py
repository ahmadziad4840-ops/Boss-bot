import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
TOKEN=os.environ.get("BOT_TOKEN")
KB=[["⚡ شحن / سحب Boss"],["💰 أرباحي","📊 حسابي"]]
async def start(u,c):
 await u.message.reply_text("👑 Boss شغال 24/24", reply_markup=ReplyKeyboardMarkup(KB, resize_keyboard=True))
async def msg(u,c):
 await u.message.reply_text(f"وصل: {u.message.text}")
app=Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,msg))
app.run_polling()
