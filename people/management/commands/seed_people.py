from random import choice
from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person


class Command(BaseCommand):

    word = "people"

    help = f"This command seeds {word}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            help=f'How many {self.word} do you want to create?',
            default=1
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            Person, number, {
                "name": lambda x: seeder.faker.name(),
                "kind": lambda x: choice([Person.KIND_ACTOR, Person.KIND_DIRECTOR, Person.KIND_WRITER]),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {self.word} created!"))
