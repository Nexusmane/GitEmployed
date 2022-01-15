from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class JobApp(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    submission_date = models.DateField('Submission Date')
    follow_up_date = models.DateField('Follow-Up Date')
    job_post_url = models.CharField(max_length=999)
    description = models.CharField(max_length=256)
    notes = models.CharField(max_length=256)
    excitement_level = models.IntegerField()
    resume_url = models.CharField(max_length=999)
    cover_letter_url = models.CharField(max_length=999)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"App for {self.company}"

    def get_absolute_url(self):
        return reverse('jobapps_index')
