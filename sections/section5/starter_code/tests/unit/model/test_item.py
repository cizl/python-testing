from unittest import TestCase

from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 10.99)

        # thrid arg is custom error message
        self.assertEqual(item.name, 'test',
                         'item name does not match')
        self.assertEqual(item.price, 10.99,
                         'item price does not match')

    def test_json(self):
        item = ItemModel('test', 10.99)
        expected = {
            'name': 'test',
            'price': 10.99
        }

        self.assertEqual(item.json(), expected)

    # cannot test database methods
    # these are not unit tests but integration tests
    # def test_find_by_name(cls, name):
    # def test_save_to_db(self):
    # def test_delete_from_db(self):
