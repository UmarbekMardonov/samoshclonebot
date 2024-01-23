from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from tgbot.handlers.onboarding import static_text
from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text

UZBEK = "O'zbekcha 🇺🇿"
RUSSIA = "Russian 🇷🇺"


def language_keyboard() -> ReplyKeyboardMarkup:
    button = [[UZBEK, RUSSIA]]
    return ReplyKeyboardMarkup(button, resize_keyboard=True)


def main_keyboard() -> ReplyKeyboardMarkup:

    buttons = [[static_text.ORDER_BUTTON, static_text.SITTINGS_BUTTON], [static_text.OPINION_BUTTON, static_text.CONTACT_BUTTON]]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
