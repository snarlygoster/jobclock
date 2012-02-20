"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


from timeclock.models import Worker

class SimpleTest(TestCase):
  def setUp(self):
    self.client = Client()
 
  def test_create_worker(self):
    response = self.client.get('/')
    self.assertEqual(len(response.context['worker_list']), 0)
    jh = Worker(name = 'John Henry')
    jh.save()
    self.assertEqual(jh.name, 'John Henry')
    response = self.client.get('/')
    self.assertEqual(len(response.context_data['worker_list']), 1)
    

class NavigationTest(TestCase):
  def setUp(self):
    self.client = Client()
  
  def test_root(self):   
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 200)
    
    
        
# create Worker (Johnhenry)
# create Job
# assign Job to customer/account
# list Workers
# list Jobs
# Punch Worker changing to Job
# Show duration of Worker between changes