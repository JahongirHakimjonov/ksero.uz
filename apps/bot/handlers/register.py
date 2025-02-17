from django.utils.translation import activate, gettext as _
from telebot import TeleBot
from telebot.types import Message, CallbackQuery

from apps.bot.handlers.language import handle_language, handle_language_selection
from apps.bot.keyboard import get_main_buttons
from apps.bot.logger import logger
from apps.bot.utils import update_or_create_user
from apps.bot.utils.language import set_language_code


def handle_message(message: Message, bot: TeleBot):
    activate(set_language_code(message.from_user.id))
    if message.text == _("Language"):
        handle_language(message, bot)
    else:
        logger.info(f"User {message.from_user.id} sent a message.")
        bot.send_message(
            message.chat.id, _("Unknown command."), reply_markup=get_main_buttons()
        )
        update_or_create_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            is_active=True,
        )


def handle_callback_query(call: CallbackQuery, bot: TeleBot):
    activate(set_language_code(call.from_user.id))
    logger.info(f"User {call.data} ====================================")
    if call.data == "lang_ru" or call.data == "lang_uz" or call.data == "lang_en":
        handle_language_selection(call, bot)
        logger.info(f"User {call.from_user.id} selected a language.")
    else:
        bot.answer_callback_query(call.id, _("Unknown action."))
        logger.info(f"User {call.from_user.id} performed an unknown action.")
