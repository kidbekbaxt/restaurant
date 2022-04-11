from django.conf import settings
from django.core.management.base import BaseCommand
from telegram.ext import Updater

from telegrambot.models import TelegramUser



class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater("5298795240:AAGDkRwngpBx8blcrNHwnPenKQiUNCswxlU")

        # for user in TelegramUser.objects.all():
        #     updater.bot.send_message(chat_id=user.telegram_user_id, text="You have successfully joined the database")

        photo_id=None
        for user in TelegramUser.objects.all():
            if photo_id is None:
                resp = updater.bot.send_photo(chat_id=user.telegram_user_id, photo=open(settings.BASE_DIR / "pic.jpeg", 'rb'))
                photo_id = resp.photo[-1].file_id
                print(photo_id)

            else:
                updater.bot.send_photo(chat_id=user.telegram_user_id, photo=photo_id)
