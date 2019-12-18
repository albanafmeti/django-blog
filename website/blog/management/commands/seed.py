from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from blog.models import Category, Post
from django.contrib.auth.models import User
from random import randint
from django.utils import timezone


class Command(BaseCommand):
    help = 'Seed data to database.'

    def handle(self, *args, **options):
        user_seeder = Seed.seeder()

        # Seed Users

        user_seeder.add_entity(User, 5, {
            'first_name': lambda x: user_seeder.faker.first_name(),
            'last_name': lambda x: user_seeder.faker.last_name(),
        })

        inserted_users = user_seeder.execute()
        random_user = inserted_users[User][randint(0, 4)]

        # Seed categories

        category_seeder = Seed.seeder()

        category_seeder.add_entity(Category, 5, {
            'name': lambda x: category_seeder.faker.word().capitalize(),
        })

        inserted_categories = category_seeder.execute()
        random_category = inserted_categories[Category][randint(0, 4)]

        # Seed posts

        post_seeder = Seed.seeder()

        post_seeder.add_entity(Post, 10, {
            'title': lambda x: category_seeder.faker.sentence(),
            'subtitle': lambda x: category_seeder.faker.sentence(),
            'content': lambda x: category_seeder.faker.text(max_nb_chars=1000),
            'author_id': lambda x: random_user,
            'category_id': lambda x: random_category,
            'published_at': lambda x: timezone.now(),
        })

        post_seeder.execute()

        self.stdout.write(self.style.SUCCESS('Successfully seeded.'))
