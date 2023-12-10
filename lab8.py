import threading
import time
import random
from datetime import datetime, timedelta


class Visitor:
    def __init__(self, name):
        self.name = name
        self.order_status = "waiting"

    def leave_cafe(self, cafe):
        cafe.current_visitors -= 1
        cafe.total_income += random.randint(5, 40)


class Table:
    def __init__(self):
        self.visitors = []
        self.capacity = 4

    def is_occupied(self):
        return bool(self.visitors)

    def is_order_taken(self):
        return all(visitor.order_status != "waiting" for visitor in self.visitors)


class Waiter:
    def __init__(self):
        self.is_busy = False

    def take_order(self, table, cafe):
        if not self.is_busy and table.visitors and not table.is_order_taken():
            self.is_busy = True
            threading.Timer(0.2, self.process_order, args=[table, cafe]).start()

    def process_order(self, table, cafe):
        for visitor in table.visitors:
            visitor.order_status = "cooking"
            threading.Timer(
                0.4, self.complete_order, args=[visitor, cafe, table]
            ).start()

    def complete_order(self, visitor, cafe, table):
        visitor.order_status = "eating"
        threading.Timer(0.4, lambda: visitor.leave_cafe(cafe)).start()
        if visitor in table.visitors:
            table.visitors.remove(visitor)
        if not table.visitors:
            self.is_busy = False


class Cafe:
    def __init__(self, num_tables, num_waiters):
        self.tables = [Table() for _ in range(num_tables)]
        self.waiters = [Waiter() for _ in range(num_waiters)]
        self.current_visitors = 0
        self.total_income = 0
        self.total_visitors = 0
        self.not_satisfied = 0

    def enter(self, visitors):
        for table in self.tables:
            if not table.is_occupied():
                self.total_visitors += len(visitors)
                self.current_visitors += len(visitors)
                table.visitors = visitors
                free_waiter = next(
                    (waiter for waiter in self.waiters if not waiter.is_busy), None
                )
                if free_waiter:
                    free_waiter.take_order(table, self)
                return
        self.not_satisfied += 1

    def simulation(self, start_hour, end_hour):
        current_time = datetime.now().replace(
            hour=start_hour, minute=0, second=0, microsecond=0
        )
        end_time = datetime.now().replace(
            hour=end_hour, minute=0, second=0, microsecond=0
        )

        while current_time < end_time:
            self.handle_visitors(current_time)

            if current_time.minute == 0:
                occupied_tables = sum(table.is_occupied() for table in self.tables)
                busy_waiters = sum(waiter.is_busy for waiter in self.waiters)
                print(
                    f"{current_time.strftime('%I:%M %p')}: Occupied Tables: {occupied_tables}/{len(self.tables)}, Current Visitors: {self.current_visitors}, Busy Waiters: {busy_waiters}/{len(self.waiters)}, Total Income: {self.total_income}"
                )

            current_time += timedelta(minutes=5)
            time.sleep(0.1)
        print(
            f"Statistics: \n Total Visitors: {self.total_visitors}, Total Income: {self.total_income}, Left because no place: {self.not_satisfied}"
        )

    def handle_visitors(self, current_time):
        if 17 <= current_time.hour <= 20:
            probability = 0.7
        else:
            probability = 0.3

        if random.random() < probability:
            visitors_quantity = random.randint(1, 4)
            visitors = [Visitor(f"Visitor{i}") for i in range(visitors_quantity)]
            self.enter(visitors)


num_tables = 10
num_waiters = 3
cafe = Cafe(num_tables, num_waiters)
cafe.simulation(9, 23)
