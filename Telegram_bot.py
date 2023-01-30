from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import Main
import moon
import how_many_days_for_holiday as HMD


async def Hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет  {update.effective_user.full_name}')


async def How_many(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(f'дней до НГ осталось: '+HMD.how_many())


async def Moon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(f'фаза луны сегодня: '+moon.get_phase_on_day())


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    correct_mes = mess[4::]
    try:
        result = Main.calc(correct_mes)
    except:
        # просто ошибка чтобы бот не лег. Вытянуть какя именно ошибка не получилось
        result = "Error"
    await update.message.reply_text(result)

app = ApplicationBuilder().token(
    "6159471403:AAEjBd3tXe7GVw_986YoPkzk1Y2gayTuPkw").build()

app.add_handler(CommandHandler("hello", Hi))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("HMD", How_many))
app.add_handler(CommandHandler("moon", Moon))

app.run_polling()
