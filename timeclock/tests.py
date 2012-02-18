"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


from timeclock.models import Worker

class SimpleTest(TestCase):
  
  def test_create_worker(self):
    jh = Worker(name = 'John Henry')
    jh.save
    print 'create!'
    self.assertEqual(jh.name, 'John Henry')
    
# create Worker (Johnhenry)
# create Job
# assign Job to customer/account
# list Workers
# list Jobs
# Punch Worker changing to Job
# Show duration of Worker between changes