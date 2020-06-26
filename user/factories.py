import factory
import user
from django.utils import timezone
import pytz
import random
import factory.fuzzy
from . import models
from datetime import datetime


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    real_name = factory.Faker('name')
    tz =  factory.fuzzy.FuzzyChoice([tz for tz in pytz.all_timezones])

class UserWithActivityPeriodFactory(UserFactory):
    
    @factory.post_generation
    def activities(obj, create, extracted, **kwargs):
        """
        If called like: UserFactory(activities=4) it generates a User with 4
        Activities.  If called without `activities` argument, it generates a
        random amount of activities for this user
        """
        
        if not create:
            return

        if extracted:
            for n in range(extracted):
                user.factories.ActivityPeriodFactory(user=obj)
        else:
            import random
            number_of_units = random.randint(1, 10)
            for n in range(number_of_units):
                user.factories.ActivityPeriodFactory(user=obj)


class ActivityPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ActivityPeriod

    start_time = factory.fuzzy.FuzzyDateTime(datetime(2020, 4, 1, tzinfo=pytz.UTC), datetime(2020, 5, 1, tzinfo=pytz.UTC))
    end_time = factory.fuzzy.FuzzyDateTime(datetime(2020, 5, 1, tzinfo=pytz.UTC))
    user = factory.SubFactory(UserFactory)