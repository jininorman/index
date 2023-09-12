from django.db import models

# Create your models here.


class orders(models.Model):
    image = models.ImageField(upload_to='image',null=True)
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)


    def __str__(self):
        return self.name

    class Meta:
      verbose_name_plural = 'Drinks'


