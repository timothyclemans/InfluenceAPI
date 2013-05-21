from django.db import models

class ChecklistTemplate(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
        
    def get_items(self):
        return ChecklistTemplateItem.objects.filter(checklist_template=self).order_by('order')
    
class ChecklistTemplateItem(models.Model):
    checklist_template = models.ForeignKey(ChecklistTemplate)
    order = models.PositiveIntegerField()
    summary = models.TextField()
    
    def __unicode__(self):
        return '%s: #%s: %s' % (self.checklist_template.name, self.order, self.summary)   
