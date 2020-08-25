import unittest


class InventoryAllocator():
    '''Produces cheapest shipment'''

    def __init__(self, orders, inventory):
        self.orders = orders
        self.inventory = inventory

    # output is name: {item: quantity}
    def shipment_details(self):
        shipment = []
        # access data: self.orders, self.inventory
        return shipment


class InventoryAllocatorTest(unittest.TestCase):
    '''Test cases for InventoryAllocator'''

    def test_exact_match(self):
        orders = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        ia = InventoryAllocator(orders, inventory)
        self.assertEqual(ia.shipment_details(), output)

    def test_not_enough_inventory(self):
        orders = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []
        ia = InventoryAllocator(orders, inventory)
        self.assertEqual(ia.shipment_details(), output)

    def test_split_across_warehouses(self):
        orders = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}},
                     {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'dm': {'apple': 5}}, {'owd': {'apple': 5}}]
        ia = InventoryAllocator(orders, inventory)
        self.assertEqual(ia.shipment_details(), output)


unittest.main()
