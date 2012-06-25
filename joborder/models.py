from django.db import models

# Create your models here.


class JobOrder(models.Model):
    """Job information for preparing estimate and shop work"""
    
 
    class Meta:
        #ordering = ['id',]
        verbose_name, verbose_name_plural = "Job order", "Job orders"
 
    def __unicode__(self):
        return "%s" % (self.id)
 
    @models.permalink
    def get_absolute_url(self):
        return ('')