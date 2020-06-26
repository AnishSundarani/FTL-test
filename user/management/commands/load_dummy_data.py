from django.core.management.base import BaseCommand, CommandError
from user.models import User, ActivityPeriod
from user.factories import UserFactory, ActivityPeriodFactory
import random

class Command(BaseCommand):
    help = 'Populates dummy data of users and their activities'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=20)

    def handle(self, *args, **options):
        count = 20
        if options['count']:
            count = options['count']
        for _ in range(count):
            member = UserFactory.create()
            random_count = random.randint(1,5)
            for _ in range(random_count):
                ActivityPeriodFactory.create(user=member)