from django.db import models

# Create your models here.
class Registration(models.Model):
      username=models.CharField(max_length=200)
      email=models.EmailField()

      def __str__(self):
            return self.username