from django.db import models
from .enums import *
from company.models import Company
from token_auth.models import UserProfile


class Skill(models.Model):
    text = models.CharField(max_length=256, null=False, unique=True)

    class Meta:
        db_table = 'skill'


class Vacancy(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    short_description = models.CharField(max_length=256, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    salary = models.IntegerField(null=False, blank=True)

    experience_type = models.IntegerField(null=False, blank=True)
    schedule_type = models.IntegerField(null=False, blank=True)
    employment_type = models.IntegerField(null=False, blank=True)

    approved = models.BooleanField(null=False, blank=False, default=False)

    skills = models.ManyToManyField(Skill, through='VacancySkills')
    min_points = models.IntegerField(null=False, blank=True)
    company = models.ForeignKey(Company, null=False, db_constraint=True, on_delete=models.CASCADE,
                                related_name='vacancies')

    class Meta:
        db_table = 'vacancy'


class VacancySkills(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'vacancy_skills'
        unique_together = ['vacancy', 'skill']


class Request(models.Model):
    comment = models.TextField(null=True, blank=True)
    decision = models.CharField(max_length=16, choices=Decision.choices(), default=Decision.NO_ANSWER.value)
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserProfile, null=False, db_constraint=True, on_delete=models.CASCADE,
                             related_name='requests')
    vacancy = models.ForeignKey(Vacancy, null=False, db_constraint=True, on_delete=models.CASCADE,
                                related_name='requests')

    class Meta:
        db_table = 'request'