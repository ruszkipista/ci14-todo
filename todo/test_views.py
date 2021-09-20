from django.test import TestCase
from .models import Item

class TestItemViews(TestCase):

    def test_output_todo_list_page(self):
        response = self.client.get("/")
        # the response was code 200 OK, success, the request has succeeded
        self.assertEqual(response.status_code, 200)
        # the template was used to create the response
        self.assertTemplateUsed(response, "todo/todo_list.html")


    def test_get_create_todo_item_manual_page(self):
        response = self.client.get("/add_item_manual")
        # the response was code 200 OK, success, the request has succeeded
        self.assertEqual(response.status_code, 200)
        # the template was used to create the response
        self.assertTemplateUsed(response, "todo/add_item_manual.html")


    def test_get_create_todo_item_auto_page(self):
        response = self.client.get("/add_item_auto")
        # the response was code 200 OK, success, the request has succeeded
        self.assertEqual(response.status_code, 200)
        # the template was used to create the response
        self.assertTemplateUsed(response, "todo/add_item_auto.html")


    def test_get_update_todo_item_auto_page(self):
        item = Item.objects.create(name="Test Item", done=False)
        response = self.client.get(f"/edit_item_auto/{item.id}")
        # the response was code 200 OK, success, the request has succeeded
        self.assertEqual(response.status_code, 200)
        # the template was used to create the response
        self.assertTemplateUsed(response, "todo/edit_item_auto.html")

    def test_create_todo_item(self):
        item_name = "Test Create Item"
        item = {"name": item_name, "done":False}
        response = self.client.post("/add_item_auto", item)
        # the response was code 302 Moved Temporarily (redirected)
        self.assertEqual(response.status_code, 302)
        # redirected to root "/"
        self.assertRedirects(response, "/")
        # get all items with given name
        stored_items = Item.objects.filter(name=item_name)
        # there is exactly 1
        self.assertEqual(len(stored_items), 1)


    def test_edit_todo_item(self):
        item = Item.objects.create(name="Test Edit Item", done=False)
        # update item
        update_item = {"name":item.name, "done":True}
        response = self.client.post(f"/edit_item_auto/{item.id}", update_item)
        # the response was code 302 Moved Temporarily (redirected)
        self.assertEqual(response.status_code, 302)
        # redirected to root "/"
        self.assertRedirects(response, "/")
        # get updated item
        stored_items = Item.objects.filter(id=item.id)
        # there is exactly 1
        self.assertEqual(len(stored_items), 1)
        # "done" is True
        self.assertTrue(stored_items[0].done)


    def test_delete_todo_item(self):
        item = Item.objects.create(name="Test Delete Item", done=False)
        # delete item
        response = self.client.post(f"/remove_item/{item.id}")
        # the response was code 302 Moved Temporarily (redirected)
        self.assertEqual(response.status_code, 302)
        # redirected to root "/"
        self.assertRedirects(response, "/")
        # get deleted item
        stored_items = Item.objects.filter(id=item.id)
        # there is exactly 0
        self.assertEqual(len(stored_items), 0)


    def test_toggle_todo_item(self):
        item = Item.objects.create(name="Test Toggle Item", done=True)
        # toggle "done" in item
        response = self.client.get(f"/toggle_done/{item.id}")
        # the response was code 302 Moved Temporarily (redirected)
        self.assertEqual(response.status_code, 302)
        # redirected to root "/"
        self.assertRedirects(response, "/")
        # get updated item
        stored_items1 = Item.objects.filter(id=item.id)
        # there is exactly 1
        self.assertEqual(len(stored_items1), 1)
        # "done" is False
        self.assertFalse(stored_items1[0].done)
        # toggle "done" in item
        response = self.client.get(f"/toggle_done/{item.id}")
        # get updated item
        stored_items2 = Item.objects.filter(id=item.id)
        # there is exactly 1
        self.assertEqual(len(stored_items2), 1)
        # "done" is True
        self.assertTrue(stored_items2[0].done)
