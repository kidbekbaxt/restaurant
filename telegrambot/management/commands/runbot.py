from django.core.management.base import BaseCommand

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegrambot.models import TelegramUser


class Command(BaseCommand):
    def start_handler(self, update: Update, context: CallbackContext):
        update.effective_message.reply_text(f"Xush kelibsiz, {update.effective_user.last_name}!!!")

        user, created = TelegramUser.objects.get_or_create(
            telegram_user_id=update.effective_user.id,
            first_name=update.effective_user.first_name,
            last_name=update.effective_user.last_name,
            username=update.effective_user.username,
        )


    def help_hanlder(self, update: Update, context: CallbackContext):
        update.effective_message.reply_text(f"Nima yordam kerak, { update.effective_user.first_name }??")

    def handle(self, *args, **options):
        updater = Updater("5298795240:AAGDkRwngpBx8blcrNHwnPenKQiUNCswxlU")

        dispatcher = updater.dispatcher

        # on different commands - answer in Telegram
        dispatcher.add_handler(CommandHandler("start", self.start_handler))
        dispatcher.add_handler(CommandHandler("help", self.help_hanlder))

        # on non command i.e message - echo the message on Telegram
        #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


        updater.start_polling()


        updater.idle()
