from django.db import models

# Create your models here.
class Hospidb(models.Model):

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)



    def __str__(self):
        return f'{self.fname} {self.lname},'

    