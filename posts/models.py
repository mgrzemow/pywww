from django.db import models
import faker as fk
import random

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Post(title: {self.title})'

    def fill_fake(self):
        f = fk.Faker('PL_pl')
        self.title = f.bs().title()
        self.content = '\n\n'.join(f.paragraphs(random.randint(3, 7)))
        self.published = random.choice([True, False])
        
