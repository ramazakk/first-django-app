from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=100)

class Person(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete='CASCADE', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.f_name, self.l_name)






