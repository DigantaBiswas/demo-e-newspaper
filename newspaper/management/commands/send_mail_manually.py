from django.core.management.base import BaseCommand

from newspaper.tasks.tasks import schedule_email_notification


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        schedule_email_notification()
