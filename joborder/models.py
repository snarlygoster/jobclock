# django library imports
from django.db import models
from django.utils.translation import ugettext as _
# third party imports

from picklefield.fields import PickledObjectField

# Create your models here.

specs = [{'q': 'Cover Material', 'a': ''}]

class Product(models.Model):
    """Type of binding or object thing"""

    name = models.CharField(_('name'), max_length=50, blank=False, null=False)
    detail_spec = PickledObjectField(default=specs)
#     detail_spec = models.CharField(_('detail specifications'), max_length=1000, default="Cover Material", help_text="questions to answer for this type of product")

    class Meta:
        ordering = ['name',]
        verbose_name, verbose_name_plural = "product", "products"

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('')

# class Customer(models.Model):
#     """Customer Contact Info for a JobOrder"""
#     name = models.CharField(_('name'), max_length=100, blank=True, null=True)
#     email = models.EmailField()
#
#     class Meta:
#         ordering = ['name', 'email']
#
#     def __unicode__(self):
#         return "%s" % (self.name)
#
#     @models.permalink
#     def get_absolute_url(self):
#         return ('')

# class Job(models.Model):
#     """Job connects customer to jobitems and scheduled activities"""
#
#     customer = models.ForeignKey(Customer)
#     creation_time = models.DateTimeField(_('created'), auto_now_add=True)
#
#
#     class Meta:
#         ordering = ['customer',]
#         verbose_name, verbose_name_plural = "job", "jobs"
#
#     def __unicode__(self):
#         return "%s" % (self.customer.name)
#
#     @models.permalink
#     def get_absolute_url(self):
#         return ('')

class JobItem(models.Model):
    """Job information for preparing estimate and shop work"""

    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    detail_answers = PickledObjectField()
#    detail_answers = models.CharField(_('details'), max_length=1000, help_text="")

    def _get_product_detail_spec(self):
        return self.product.detail_spec

    def save(self, *args, **kwargs):
        if not self.detail_answers:
            self.detail_answers = self._get_product_detail_spec()
        super(JobItem, self).save(*args, **kwargs)

    class Meta:
        #ordering = ['id',]
        verbose_name, verbose_name_plural = "Job item", "Job Items"

    def __unicode__(self):
        return "%s" % (self.id)

    @models.permalink
    def get_absolute_url(self):
        return ('')


