from datetime import date

from django.test import TestCase

from joborder.models import *


class JobOrderTest(TestCase):
    """test for joborders"""
    def setUp(self):
        self.ssproduct = Product.objects.get(name__istartswith='smyth-sewn')
        self.johndoe = Customer(name='John Doe')

    def test_job_has_quantity(self):
        """
        Set quantity of product
        """
        joborder = JobOrder(product=self.ssproduct)

        joborder.quantity = 1
        joborder.save()
        self.assertEqual(JobOrder.objects.get(pk=joborder.pk).quantity, 1)

    def test_joborder_has_covermaterial(self):

        joborder = JobOrder()

        joborder.product = Product.objects.get(pk=1)
        joborder.save()
        self.assertFalse(joborder.covermaterial,'should have covermaterial')
        joborder.covermaterial = 'Blue Silk'
        joborder.save()
        self.assertTrue(joborder.covermaterial,'product should have covermaterial')

    def test_joborder_has_duedate(self):

        joborder = JobOrder(product=self.ssproduct)
        self.assertIsNone(joborder.duedate,'joborder should have a due date')
        joborder.duedate = date.today()
        joborder.save()
        self.assertIsNotNone(joborder.duedate)

    def test_scheduledjob_has_customer(self):
        sjo = ScheduledJob()
        sjo.customer = self.johndoe
