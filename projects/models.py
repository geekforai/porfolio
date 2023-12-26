from django.db import models

class Projects(models.Model):
    project_title=models.CharField(max_length=50)
    project_image=models.ImageField(max_length=50)
    project_objective=models.TextField()
    project_desc=models.TextField()
    project_tech_used=models.TextField()
    project_link=models.CharField(max_length=50)
