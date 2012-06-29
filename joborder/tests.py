
from django.test import TestCase

from joborder.models import *

class JobOrderTest(TestCase):
    """test for joborders"""
    def setUp(self):
        ss = Product.objects.get_or_create(name='smyth-sewn')


    def test_create_new_joborder_and_save(self):
        """
        Create a job order
        """
        joborder = JobOrder()
        joborder.product = Product.objects.get(name='smyth-sewn')
        joborder.save()
        # our new joborder should be the only one in test db
        self.assertEqual(len(JobOrder.objects.all()),1)
        self.assertEqual(JobOrder.objects.all()[0], joborder)

    def test_pick_symth_sewn_job(self):
        """
        Set type of job to smyth-sewn
        """
        symthsewn = Product.objects.filter(name='smyth-sewn')

#         joborder = JobOrder()
#
#         joborder.product = 'smyth-sewn'
#         joborder.save()
#
#         ss = JobOrder.objects.filter(product = 'smyth-sewn')
#         self.assertEqual(len(ss), 1)

