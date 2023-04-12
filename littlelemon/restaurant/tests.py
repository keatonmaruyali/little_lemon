from django.test import TestCase

from .models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title='IceCream',
            price=2.50,
            inventory=100,
        )
        itemstr = item.get_item()

        self.assertEqual(itemstr, 'IceCream : 2.5')


class MenuViewTest(TestCase):
    new_items = [
        {
            'title': 'IceCream',
            'price': 2.50,
            'inventory': 100,
        },
        {
            'title': 'Coffee',
            'price': 1.50,
            'inventory': 100,
        },
        {
            'title': 'Donut',
            'price': 2.00,
            'inventory': 100,
        },
    ]

    def setUp(self) -> None:
        for item in self.new_items:
            Menu.objects.create(
                title=item['title'],
                price=item['price'],
                inventory=item['inventory'],
            )

    def test_getall(self):
        items = list(Menu.objects.values('title', 'price', 'inventory'))
        # items = MenuSerializer(items)
        self.assertEqual(items, self.new_items)
