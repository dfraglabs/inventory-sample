from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=50, blank=False)
    species = models.CharField(max_length=50)
    dimensions = models.FloatField()
    price = models.FloatField()

    choices = (
        ('PENDING', 'Transaction pending'),
        ('PAID', 'Invoice paid'),
        ('COMPLETE', 'Transaction complete')
    )

    status = models.CharField(max_length=10, choices=choices, default='PENDING')
    notes = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)


class Logs(Item):
    pass


class Plywood(Item):
    pass
