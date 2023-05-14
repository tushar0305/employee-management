from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=255)
    selected_role = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.title
