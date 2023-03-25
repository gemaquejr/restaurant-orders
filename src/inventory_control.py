class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.current_inventory = {
            ingredient: self.MINIMUM_INVENTORY[ingredient]
            for ingredient in self.MINIMUM_INVENTORY}
        self.orders = {}

    def add_new_order(self, customer, order, day):
        if order not in self.orders:
            self.orders[order] = []
        self.orders[order].append(
            {
                "customer": customer,
                "order": order,
                "day": day
            }
        )

        for ingredient in self.INGREDIENTS[order]:
            if self.current_inventory[ingredient] < 1:
                return False
            else:
                self.current_inventory[ingredient] -= 1

        return True

    def get_quantities_to_buy(self):
        return {ingredient: max(0, self.MINIMUM_INVENTORY[ingredient]
                                - self.current_inventory[ingredient])
                for ingredient in self.MINIMUM_INVENTORY}

    def get_available_dishes(self):
        dishes = {'hamburguer', 'misto-quente', 'pizza', 'coxinha'}

        available_dishes = set()
        for dish in dishes:
            ingredients = self.get_ingredients_for_dish(dish)

            available = True
            for ingredient, amount in ingredients.items():
                if self.current_inventory[ingredient] < amount:
                    available = False
                    break

            if available:
                available_dishes.add(dish)

        return available_dishes

    def get_ingredients_for_dish(self, dish):
        if dish == 'hamburguer':
            return {
                'pao': 1,
                'carne': 1,
                'queijo': 1,
                'molho': 1,
            }
        elif dish == 'misto-quente':
            return {
                'pao': 1,
                'queijo': 1,
            }
        elif dish == 'pizza':
            return {
                'massa': 1,
                'molho': 1,
                'queijo': 1,
            }
        elif dish == 'coxinha':
            return {
                'massa': 1,
                'frango': 1,
            }
        else:
            raise ValueError(f'Prato "{dish}" não encontrado')
