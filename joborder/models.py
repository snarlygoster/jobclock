# django library imports
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Product(models.Model):
    """Type of binding or object thing"""

    name = models.CharField(_('name'), max_length=50, blank=False, null=False)
    details = models.CharField(_('details'), max_length=1000, blank=True, null=True, help_text="questions to answer for this type of product")
    
    class Meta:
        ordering = ['name',]
        verbose_name, verbose_name_plural = "product", "products"

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('')


class Customer(models.Model):
    """Customer Contact Info for a JobOrder"""
    name = models.CharField(_('name'), max_length=100, blank=True, null=True)
    email = models.EmailField()

    class Meta:
        ordering = ['name', 'email']

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('')


class Job(models.Model):
    """Job connects customer to jobitems and scheduled activities"""
    
    customer = models.ForeignKey(Customer) 
    creation_time = models.DateTimeField(_('created'), auto_now_add=True)
    

    class Meta:
        ordering = ['customer',]
        verbose_name, verbose_name_plural = "job", "jobs"
 
    def __unicode__(self):
        return "%s" % (self.customer.name)
 
    @models.permalink
    def get_absolute_url(self):
        return ('')

class JobItem(models.Model):
    """Job information for preparing estimate and shop work"""
    
    job = models.ForeignKey(Job)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    detail_answers = models.CharField(_('details'), max_length=1000, blank=True, null=True, help_text="")
    
    class Meta:
        #ordering = ['id',]
        verbose_name, verbose_name_plural = "Job item", "Job Items"

    def __unicode__(self):
        return "%s" % (self.id)

    @models.permalink
    def get_absolute_url(self):
        return ('')
