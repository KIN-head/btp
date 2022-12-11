from django.db import models
from django.db import models
from django.utils import timezone

class Request(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    VIN = models.CharField(max_length=20)
    Car = models.CharField(max_length=100)
    Model_year = models.IntegerField()
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.VIN
