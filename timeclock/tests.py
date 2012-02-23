"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


from timeclock.models import Worker

class WorkerTest(TestCase):
  def setUp(self):
    self.client = Client()
 
  def test_create_worker(self):
    jh = Worker(name = 'John Henry')
    jh.save()
    self.assertEqual(jh.name, 'John Henry')
    # self.assertEqual(len(response.context_data['worker_list']), 1, 'expected one Worker')
    
    

class NavigationTest(TestCase):
  def setUp(self):
    self.client = Client()
  
  def test_root(self):   
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 200)
    self.assertContains(response, '<title>ClockPunch</title>',status_code = 200)
    
    
        
# create Worker (Johnhenry)
# create Job
# assign Job to customer/account
# list Workers
# list Jobs
# Punch Worker changing to Job
# Show duration of Worker between changes