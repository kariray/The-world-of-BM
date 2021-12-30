from random import choice, randint
from django.core.management.base import BaseCommand
from django_seed import Seed
from books.models import Book
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    word = "books"

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
        writers = Person.objects.filter(kind=Person.KIND_WRITER)
        seeder = Seed.seeder()
        seeder.add_entity(
            Book, number, {
                "title": lambda x: seeder.faker.text(max_nb_chars=randint(7, 25)),
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "category": lambda x: choice(categories),
                "writer": lambda x: choice(writers),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {self.word} created!"))
