import secrets

from django.core.management.base import BaseCommand, CommandError

from bot.models import TgUser
from bot.tg.bot_logic import get_user_goals, show_categories
from bot.tg.client import TgClient
from bot.tg.schemas import Message
from goals_planner.settings import BOT_TOKEN


class Command(BaseCommand):
    help = 'Command run bot'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TgClient(BOT_TOKEN)
        self.users_data = {}

    def add_arguments(self, parser):
        parser.add_argument('runbot', nargs='?', default='runbot')

    def handle(self, *args, **options):
        if options['runbot']:
            offset = 0
            try:
                while True:
                    res = self.client.get_updates(offset=offset)

                    for item in res.result:
                        offset = item.update_id + 1
                        self.handle_message(item.message)
            except Exception as e:
                raise CommandError(f'Error: {e}')

    def handle_message(self, message: Message) -> None:
        chat_id = message.chat.id
        tg_user, _ = TgUser.objects.get_or_create(tg_id=chat_id, defaults={'username': message.chat.username})

        if not tg_user.is_verified:
            token = secrets.token_urlsafe()[:16]
            tg_user.verification_code = token
            tg_user.save()
            message = f"Link your account.\nVerification code: {token}"
            self.client.send_message(chat_id=chat_id, text=message)
        else:
            self.handle_auth_user(tg_user=tg_user, message=message)

    def handle_auth_user(self, tg_user: TgUser, message: Message) -> None:
        if message.text.startswith('/'):
            match message.text:
                case '/goals':
                    text = get_user_goals(tg_user.user.id)
                case '/create':
                    text = show_categories(user_id=tg_user.user.id, chat_id=message.chat.id, users_data=self.users_data)
                case '/cancel':
                    if self.users_data[message.chat.id]:
                        del self.users_data[message.chat.id]
                    text = 'New goal creation canceled'
                case _:
                    text = 'This command does not exist'
        elif message.chat.id in self.users_data:
            next_handler = self.users_data[message.chat.id].get('next_handler')
            text = next_handler(
                user_id=tg_user.user.id, chat_id=message.chat.id, message=message.text, users_data=self.users_data
            )
        else:
            text = 'Commands:\n/goals - Show my goals\n' '/create - Create a new goal\n/cancel - Cancel to create'
        self.client.send_message(chat_id=message.chat.id, text=text)
