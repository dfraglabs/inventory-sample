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
        return 'Item: {0} - {1}'.format(self.name, self.species)


class Logs(Item):
    pass

    class Meta:
        verbose_name_plural = "logs"


class Plywood(Item):
    pass

    class Meta:
        verbose_name_plural = "plywood"
