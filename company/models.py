from django.db import models

from core.models import City
from token_auth.models import UserProfile


class Role(models.Model):
    full_name = models.CharField(max_length=256, null=False, blank=False)
    position = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.TextField(null=False, blank=True, default='')

    class Meta:
        db_table = 'role'


class Company(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    logo = models.TextField(null=False, blank=True)

    city = models.ForeignKey(City, null=False, blank=False, db_constraint=True, on_delete=models.CASCADE,
                             related_name='companies')

    subject = models.TextField(null=False, blank=False)
    state = models.TextField(null=False, blank=False)
    link = models.CharField(max_length=256, null=False, blank=True)
    roles = models.ManyToManyField(Role, through='CompanyRoles')

    profile = models.ForeignKey(UserProfile, null=False, db_constraint=True, on_delete=models.CASCADE,
                                related_name='companies')

    class Meta:
        db_table = 'company'


class CompanyRoles(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'company_roles'
