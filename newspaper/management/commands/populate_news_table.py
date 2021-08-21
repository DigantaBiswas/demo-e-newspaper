from django.core.management.base import BaseCommand, CommandError

from newspaper.tasks.tasks import schedule_populate_news_data


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        schedule_populate_news_data()