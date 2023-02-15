class TrackOrders:
    # constructor
    def __init__(self):
        self.track_orders = []

    def __len__(self):
        return len(self.track_orders)

    def add_new_order(self, customer, order, day):
        self.track_orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        count = {}
        request_by_custom = [i for i in self.track_orders if i[0] == customer]

        for index in request_by_custom:
            if index[1] not in count:
                count[index[1]] = 1
            else:
                count[index[1]] += 1

        most_requested = max(count, key=count.get)
        return most_requested

    def get_never_ordered_per_customer(self, customer):
        all_plates = set()
        never_plates_orders = set()

        for index in self.track_orders:
            all_plates.add(index[1])
            if index[0] == customer:
                never_plates_orders.add(index[1])
        return all_plates.difference(never_plates_orders)

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
