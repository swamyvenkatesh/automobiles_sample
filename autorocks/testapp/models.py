# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Insertdata(models.Model):
    name=models.CharField(max_length=200,blank=True)
    values=models.CharField(max_length=200,blank=True)