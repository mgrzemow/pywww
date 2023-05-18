from django.core.management import BaseCommand
from posts.models import Post


class Command(BaseCommand):
    help = '''Generuję fakowe posty.'''

    def handle(self, *args, no=5, **kwargs):
        print('jestem wywołana', no)
        for _ in range(no):
            p = Post()
            p.fill_fake()
            p.save()

    def add_arguments(self, parser):
        parser.add_argument('no', default=5, type=int)
