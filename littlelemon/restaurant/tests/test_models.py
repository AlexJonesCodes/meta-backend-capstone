from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        Menu.objects.create(title="Pasta", price=9.99, inventory=30)
        Menu.objects.create(title="Burger", price=8.99, inventory=20)

    def test_getall(self):
        # Retrieve all Menu objects
        menu_items = Menu.objects.all()
        # Serialize the data
        serialized_data = MenuSerializer(menu_items, many=True).data
        
        # Assert the serialized data is as expected
        self.assertEqual(len(serialized_data), 3)
        self.assertEqual(serialized_data[0]['title'], 'Pizza')
        self.assertEqual(serialized_data[1]['title'], 'Pasta')
        self.assertEqual(serialized_data[2]['title'], 'Burger')