from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Feeling(models.Model):
    is_good = models.BooleanField()
    feeling = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('is_good', 'feeling')

    def __unicode__(self):
        return '%s: %s' % (self.is_good, self.feeling)

class Need(MPTTModel):
    need = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.need

