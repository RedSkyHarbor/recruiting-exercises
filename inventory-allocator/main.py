import unittest


class InventoryAllocator():
    '''Produces cheapest shipment'''

    def __init__(self, orders, inventory):
        self.orders = orders
        self.inventory_distribution = inventory

    def shipment_details(self):
        shipments = []
        for i_d in self.inventory_distribution:
            for item in self.orders:
                if item in i_d["inventory"]:
                    if i_d["inventory"][item] == 0:
                        continue
                    if i_d["inventory"][item] >= self.orders[item]:
                        i_d["inventory"][item] -= self.orders[item]
                        shipments.append(
                            {i_d["name"]: {item: self.orders[item]}})
                        self.orders[item] = 0
                    else:
                        self.orders[item] -= i_d["inventory"][item]
                        shipments.append(
                            {i_d["name"]: {item: i_d["inventory"][item]}})
                        i_d["inventory"][item] = 0
        return shipments


class InventoryAllocatorTest(unittest.TestCase):
    '''Test cases for InventoryAllocator'''

    def test_exact_match(self):
        orders = {'apple': 1}
        inventory_distribution = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        ia = InventoryAllocator(orders, inventory_distribution)
        self.assertEqual(ia.shipment_details(), output)

    def test_not_enough_inventory(self):
        orders = {'apple': 1}
        inventory_distribution = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []
        ia = InventoryAllocator(orders, inventory_distribution)
        self.assertEqual(ia.shipment_details(), output)

    def test_split_across_warehouses(self):
        orders = {'apple': 10}
        inventory_distribution = [{'name': 'owd', 'inventory': {'apple': 5}},
                                  {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'dm': {'apple': 5}}, {'owd': {'apple': 5}}]
        ia = InventoryAllocator(orders, inventory_distribution)
        self.assertCountEqual(ia.shipment_details(), output)


unittest.main()
