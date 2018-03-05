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
    id = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    balance = models.FloatField()

    def __str__(self):
        return str(self.id) + " - " + self.customer


class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    trans_amount = models.FloatField()
    trans_date = models.DateField()
    trans_type = models.CharField(max_length=1)
    trans_remarks = models.CharField(null=True, max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.trans_type + ' - ' + str(self.trans_amount)
