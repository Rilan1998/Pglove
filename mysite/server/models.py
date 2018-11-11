from django.db import models

# Create your models here.


class GloveData(models.Model):
    #all = JSONField()
    username = models.CharField(max_length=60)
    datetime = models.DateTimeField(null=True)
    angledata = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)



