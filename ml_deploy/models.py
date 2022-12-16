from django.db import models



class Iris(models.Model):

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/iris_home/'