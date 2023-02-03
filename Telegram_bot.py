from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application, MessageHandler, filters, ConversationHandler
import Main
import moon
import how_many_days_for_holiday as HMD
global flag_caclc
global my_calc
COOSING, TYPING_REPLY, TYPING_CHOISW = range(3)
reply_keyboard = [["Фаза луны", "Калькулятор самописный"], [
    "Дней до НГ", "Калькулятор интернет"], []]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def fact_to_str(user_data: dict[str, str]) -> str:
    facts = [f"{key}-{value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Привет! Выберите одну из команд в меню", reply_markup=markup)
    return COOSING


async def regular_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global flag_caclc
    global my_calc
    text = update.message.text
    context.user_data["choice"] = text
    answer = 'None'
    if (text == 'Фаза луны'):
        answer = str('фаза луны сегодня: ' + moon.get_phase_on_day())
    elif (text == 'Дней до НГ'):
        answer = str('дней до НГ осталось: ' + HMD.how_many())
    elif (text == 'Калькулятор самописный'):
        flag_caclc = True
        my_calc = True                 # калькулятор тыкать сюда
        answer = 'Введите выражение(без комплексных чисел'
    await update.message.reply_text(answer)
    return TYPING_REPLY


async def custom_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ## Пользовательские категории#
    await update.message.reply_text('Пожалуйста отправь мне категорию')
    return TYPING_CHOISW


async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global flag_caclc
    global my_calc
    text = update.message.text
    category = context.user_data["choice"]
    context.user_data[category] = text.lower()
    del context.user_data["choice"]
    if (text == 'Фаза луны'):
        answer = str('фаза луны сегодня: ' + moon.get_phase_on_day())
        flag_caclc = False
        my_calc = False
    elif (text == 'Дней до НГ'):
        answer = str('дней до НГ осталось: ' + HMD.how_many())
        flag_caclc = False
        my_calc = False
    else:
        answer = "Повторите выбор"
        if (flag_caclc and my_calc):
            try:
                answer = Main.calc(text)
                flag_caclc = False
                my_calc = False
            except:
                answer = "Ошибка при вычислении"
                flag_caclc = False
                my_calc = False
        elif (flag_caclc):
            answer = "интернет попалось"
            flag_caclc = False
            my_calc = False
    await update.message.reply_text(  # калькулятор это походу сюда
        answer,
        reply_markup=markup,
    )

    return COOSING


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    return ConversationHandler.END


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i+n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


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
conv_handler = ConversationHandler(entry_points=[CommandHandler("start", start)], states={COOSING: [MessageHandler(filters.Regex("^(Фаза луны|Калькулятор самописный|Дней до НГ|Калькулятор интернет)$"), regular_choice), MessageHandler(filters.Regex("^Something else...$"), custom_choice)], TYPING_CHOISW: [
                                   MessageHandler(filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), regular_choice)], TYPING_REPLY: [MessageHandler(filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), received_information,)], }, fallbacks=[MessageHandler(filters.Regex("^Done$"), done)],)

app.add_handler(CommandHandler("calc", calc))
app.add_handler(conv_handler)
app.run_polling()
