from django.utils.translation import activate

from apps.users.models.bot import BotUser


def set_language_code(telegram_id):
    if BotUser.objects.filter(telegram_id=telegram_id).exists():
        user = BotUser.objects.get(telegram_id=telegram_id)
        activate(user.language_code)
        return user.language_code
    else:
        activate("uz")
        return "uz"
