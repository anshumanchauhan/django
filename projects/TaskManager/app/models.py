from django.db import models

 

class TaskManage(models.Model):
    task_name = models.CharField(max_length=50)
    assign_by = models.CharField(max_length=50)
    assign_to = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Notes(models.Model):
    title =models.CharField(max_length=50)
    content=models.CharField(max_length=500)
    todo=models.CharField(max_length=50)
