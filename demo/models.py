from django.db import models

# Create your models here.

class Course:
    def __init__(self, name, duration, price, topics=None):
        self.name = name
        self.duration = duration
        self.price = price
        self.topics = topics

    def __str__(self):
        return "%s %d %d" % (self.name, self.duration, self.price)


class Account(models.Model):
    customer = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    balance = models.FloatField()

    def __str__(self):
        return self.customer


