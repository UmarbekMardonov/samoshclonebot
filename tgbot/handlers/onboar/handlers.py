import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from telegram import ReplyKeyboardMarkup

from product.models import Category
from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from users.models import User, PhoneModel
from tgbot.handlers.onboarding import keyboards
from tgbot import states


def category(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)
    categories = Category.objects.filter(parent=None)
    if not len(categories):
        update.message.reply_text("No categories")

    keyboard = []
    for index in range(0, len(categories), 2):
        if len(categories) - 1 == index:
            keyboard.append([categories[index].title])
        else:
            keyboard.append([categories[index].title, categories[index + 1].title])

    update.message.reply_text("Keyboard", reply_markup=ReplyKeyboardMarkup(keyboard))


def contact_def(update: Update, context: CallbackContext) -> None:
    nr = PhoneModel.objects.all()
    if update.message.text == "☎️ Biz bilan aloqa":
        text = "Biz bilan bog'lanish uchun quyidagi" \
               f"raqamga telefon qiling!\n {nr[0].number}"
        update.message.reply_text(text=text)


def choose_correct_languages(update: Update, context: CallbackContext) -> None:
    text = "Quyidagilardan birini tanlang"
    update.message.reply_text(text, reply_markup=keyboards.language_keyboard())


def choose_languages(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if update.message.text == "UZBEK":
        u.language = "uz"
    elif update.message.text == "RUSSIAN":
        u.language = "ru"
    u.save()
    text = static_text.start_not_created.format(first_name=u.first_name)
    update.message.reply_text(text=text, reply_markup=keyboards.main_keyboard())
    return states.MAIN

# def secret_level(update: Update, context: CallbackContext) -> None:
#     # callback_data: SECRET_LEVEL_BUTTON variable from manage_data.py
#     """ Pressed 'secret_level_button_text' after /start command"""
#     user_id = extract_user_data_from_update(update)['user_id']
#     text = static_text.unlock_secret_room.format(
#         user_count=User.objects.count(),
#         active_24=User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()
#     )
#
#     context.bot.edit_message_text(
#         text=text,
#         chat_id=user_id,
#         message_id=update.callback_query.message.message_id,
#         parse_mode=ParseMode.HTML
#     )
