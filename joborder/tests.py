
from django.test import TestCase

from joborder.models import JobOrder

class ProductTest(TestCase):
        
    def test_can_create_new_joborder(self):
        """
        Create a job order
        """
        joborder = JobOrder()
        joborder.add_item(JobItem())
        
#     def test_add_item_to_joborder(self):
#         
#         joborder.add_item()
#     def test_list_products(self):
#         productlist = Product.objects.all()
