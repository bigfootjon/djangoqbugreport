from django.core.management.base import BaseCommand, CommandError
from testapp.models import Test, Tag
from django.db.models import Q


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Expect 2 results to match this query:")
        print(Test.objects.filter(Q(tags=1)))
        print()
        print("Expect 3 unique (4 total, one duplicate) results to match this query:")
        print(Test.objects.filter(Q(tags=1) | Q(tags=2)))
        print()
        print("Expect 1 result to match this query:")
        print(Test.objects.filter(Q(tags=1) & Q(tags=2)))
        print()
        print("Expect 1 result to match this query:")
        print(Test.objects.filter(Q(tags=1)).filter(Q(tags=2)))
        print()
        print("Expect 1 result to match this query:")
        print(Test.objects.filter(Q(tags=1), Q(tags=2)))
