from django.db import models
from django.contrib.auth.models import User


class UserCompany(models.Model):
    '''Holds the company field for each student user profile'''
    user = models.OneToOneField(User, unique=True, db_index=True, related_name='company')
    company = models.CharField(blank=True, max_length=50, db_index=True)

    class Meta(object):
        db_table = "auth_usercompany"
