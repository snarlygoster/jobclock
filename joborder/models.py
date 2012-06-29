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
class JobOrder(models.Model):
    """Job information for preparing estimate and shop work"""

    product = models.ForeignKey(Product)

    class Meta:
        #ordering = ['id',]
        verbose_name, verbose_name_plural = "Job order", "Job orders"

    def __unicode__(self):
        return "%s" % (self.id)

    @models.permalink
    def get_absolute_url(self):
        return ('')

