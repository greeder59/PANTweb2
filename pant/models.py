from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # **At some point we need to uncomment the next line and migrate it into the database.
    # sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Link(models.Model):
    category = models.ForeignKey(Category)
    # **At some point we need to uncomment the next line and migrate it into the database.
    # show_this = models.BooleanField(default=True)
    title = models.CharField(max_length=128)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    headline = models.CharField(max_length=128)
    ann_text = models.TextField('Announcement text', max_length=4096) #shorten to 1024
    show_this = models.BooleanField(default=True)
    # **At some point we need to uncomment the next line and migrate it into the database.
    # sequence = models.IntegerField(default=5)

    def __str__(self):
        return self.headline        