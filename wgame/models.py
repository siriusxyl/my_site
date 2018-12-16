# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class WGameVersion(models.Model):
    game = models.CharField(max_length=50, default='')
    version = models.CharField(max_length=20, default='')
    switch = models.IntegerField(default=0)

    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

