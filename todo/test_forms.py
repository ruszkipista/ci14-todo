from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    def test_name_field_is_required(self):
        # instantiate a form with empty "name" field
        form = ItemForm({'name': ''})
        # assert that the form is not valid by calling built-in validation method
        self.assertFalse(form.is_valid())
        # assert that there is a "name" key in the dictionary of errors
        self.assertIn('name', form.errors.keys())
        # assert that there is a specific error message
        self.assertEqual(form.errors['name'][0], "This field is required.")


    def test_done_field_is_not_required(self):
        # instantiate a form without "done" field
        form = ItemForm({'name': 'Test Todo Item'})
        # assert that the form is valid by calling built-in validation method
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        # assert that fields included into the form are these
        self.assertEqual(form.Meta.fields, ['name','done'])
