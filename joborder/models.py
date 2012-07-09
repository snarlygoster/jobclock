# django library imports
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Product(models.Model):
    """Type of binding or object thing"""

    name = models.CharField(_('name'), max_length=50, blank=False, null=False)

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
    slug = models.SlugField()

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('')

class JobOrder(models.Model):
    """Job information for preparing estimate and shop work"""

    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    duedate = models.DateField(_('Due Date'), blank=True, null=True)
    covermaterial = models.CharField(_('Cover Material'), max_length=100, blank=True, null=True )

    class Meta:
        #ordering = ['id',]
        verbose_name, verbose_name_plural = "Job order", "Job orders"

    def __unicode__(self):
        return "%s" % (self.id)

    @models.permalink
    def get_absolute_url(self):
        return ('')


class ScheduledJob(models.Model):
    """ready to be put on the clock"""

    joborder = models.ForeignKey(JobOrder)
    customer = models.ForeignKey(Customer)

    creation_date = models.DateTimeField(_('creation date'), blank=True, null=True, auto_now_add=True)

    class Meta:
        ordering = ['creation_date',]

    def __unicode__(self):
        return "%s" % (self.ticket)

    @models.permalink
    def get_absolute_url(self):
        return ('')