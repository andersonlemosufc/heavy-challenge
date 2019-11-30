from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    message = models.TextField('Message')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_set')
    supervisors = models.ManyToManyField(User, blank=True, related_name='supervised_report_set')


class ReportResponse(models.Model):
    message = models.TextField('Message')
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='response_set')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_response_set')
