from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_new_item_defaults_to_done_false(self):
        item = Item.objects.create(name="Test DoneFalse Item")
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item_name = "Test Item StringMethod"
        item = Item.objects.create(name=item_name)
        self.assertEqual(str(item), item_name)