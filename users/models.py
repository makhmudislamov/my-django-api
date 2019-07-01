from django.db import models
from django.contrib.auth.models import AbstractUser


# is your user a teacher or a student?
class User(AbstractUser):
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username

class Student(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username