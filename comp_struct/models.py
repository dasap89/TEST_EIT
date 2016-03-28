from __future__ import unicode_literals
from django.db import models
from treebeard.mp_tree import MP_Node


class Company(MP_Node):
    name = models.CharField(unique=True, max_length=30)
    earnings = models.IntegerField()

    def __unicode__(self):
        return self.name
