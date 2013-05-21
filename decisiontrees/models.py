from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Decision(MPTTModel):
    name = models.CharField(max_length=50) # don't make unique=true
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    summary = models.TextField(blank=True)
    explanation = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name

    def get_url(self):
        return '/decisions/%s/' % (self.id)
