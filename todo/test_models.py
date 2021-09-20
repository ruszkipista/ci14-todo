from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_new_item_defaults_to_done_false(self):
        item = Item.objects.create(name="Test DoneFalse Item")
        self.assertFalse(item.done)