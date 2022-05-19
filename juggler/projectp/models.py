from django.db import models


# Create your models here.
class Project(models.Model):
    """Simple project class."""
    project_name = models.TextField(max_length=30, verbose_name='Name of project')
    persons = models.IntegerField(verbose_name='Number of persons in project.')

    def __str__(self):
        return self.project_name


class Task(models.Model):
    """Simple task class"""
    task_name = models.TextField(max_length=30, verbose_name='Name of task')
    days = models.IntegerField(verbose_name='Quantity of days')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
