"""
Because the foreign key for store is defined as
    store = db.relationship('StoreModel')
if we create
    item = ItemModel('test', 19.99, 1)
the program doesn't recognize StoreModel because it isn't
imported anywhere.
To combat this, we create a UnitBaseTest, where we have
only one unused import, instead of having an unused import
of StoreModel in every test file.
"""
from tests.unit.unit_base_test import UnitBaseTest
from models.item import ItemModel


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument.")

    def test_item_json(self):
        item = ItemModel('test', 19.99, 1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))
