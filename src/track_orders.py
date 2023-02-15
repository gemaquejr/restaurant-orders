class TrackOrders:
    # constructor
    def __init__(self):
        self.track_orders = []

    def __len__(self):
        return len(self.track_orders)

    def add_new_order(self, customer, order, day):
        self.track_orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
