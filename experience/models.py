
from django.db import models

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    image=models.ImageField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Allow null for ongoing experiences

    def __str__(self):
        return self.job_title  # Return job title as the string representation

class Responsibility(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    responsibility_text = models.CharField(max_length=200)

    def __str__(self):
        return self.responsibility_text  # Return responsibility text as the string representation
