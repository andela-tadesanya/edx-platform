from django.db import models
from student.models import UserProfile


class UserCompany(models.Model):
    '''Holds the company field for each student user profile'''
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
    company = models.CharField(blank=True, null=True, max_length=50, db_index=True)

    class Meta(object):
        db_table = "auth_usercompany"
