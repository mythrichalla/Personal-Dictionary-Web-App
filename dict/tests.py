from django.test import TestCase
from .models import Set, Entry

# Create your tests here.
# class EntryTestCase(TestCase):
#     set= None
#     entry1 = None
#     entry2 = None
#     entry3 = None

#     def setUp(self):    # sets up testing structure to create objects to be used in future tests 
#         self.set = Set.objects.create(title='test_set_1')
#         self.entry1= Entry.objects.create(set=self.set, term='e1Term', definition='e1Def')
#         self.entry2= Entry.objects.create(set=self.set, term='e2Term', definition='e2Def')
#         self.entry3= Entry.objects.create(set=self.set, term='e3Term', definition='e3Def')

#     def test_starting_conditions(self):     # just checking if set and terms are in database properly stored
#         self assertIsInstance(self.set, Set)
#         self assertIsInstance(self.entry1, Entry)
#         self assertIsInstance(self.entry2, Entry)
#         self assertIsInstance(self.entry3, Entry)