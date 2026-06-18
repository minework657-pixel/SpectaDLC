from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

BOT_TOKEN = "8720070468:AAGp-1U7ok6KoY2evSa1hURR31sCjILl464"

CFG_LINK = "https://workupload.com/file/ЕЩЕ НЕТУ"
RP_LINK = "https://workupload.com/file/djVywYfhgyw"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Выбрать товар", callback_data="shop")]
    ]

    await update.message.reply_photo(
        photo=open("logo.png", "rb"),
        caption="💎 Добро пожаловать в Мой РП/КФГ !\n\nВыберите рп/кфг:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "shop":
        keyboard = [
            [InlineKeyboardButton("⚙️ CFG", callback_data="cfg")],
            [InlineKeyboardButton("🎨 Resource Pack", callback_data="rp")]
        ]

        await query.message.reply_text(
            "🛒 Выберите товар:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "cfg":
        keyboard = [
            [InlineKeyboardButton("📥 Скачать КФГ", url=CFG_LINK)]
        ]

        await query.message.reply_text(
            "⚙️ Нажмите кнопку ниже для скачивания КФГ:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "rp":
        keyboard = [
            [InlineKeyboardButton("📥 Скачать РП", url=RP_LINK)]
        ]

        await query.message.reply_text(
            "🎨 Нажмите кнопку ниже для скачивания РП:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()