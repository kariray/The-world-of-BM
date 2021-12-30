from random import choice, choices, randint
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    word = "movies"

    help = f"This command seeds {word}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            help=f"How many {self.word} do you want to create?",
            default=1
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        categories = Category.objects.all()
        director = Person.objects.filter(kind=Person.KIND_DIRECTOR)
        cast = Person.objects.filter(kind=Person.KIND_ACTOR)
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie, number, {
                "title": lambda x: seeder.faker.sentence(),
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "category": lambda x: choice(categories),
                "director": lambda x: choice(director),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} {self.word} created!'))
