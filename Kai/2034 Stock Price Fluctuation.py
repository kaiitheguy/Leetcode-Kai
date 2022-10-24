# https://leetcode.com/problems/stock-price-fluctuation/

from collections import defaultdict

class StockPrice:

    def __init__(self):
        self.price_map = defaultdict(int)
        self.latest_timestamp = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.price_map[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.price_map[self.latest_timestamp]

    def maximum(self) -> int:
        price, timestamp = heappop(self.max_heap)
        while -price != self.price_map[timestamp]:
            price, timestamp = heappop(self.max_heap)
        heappush(self.max_heap, (price, timestamp))
        return -price

    def minimum(self) -> int:
        price, timestamp = heappop(self.min_heap)
        while price != self.price_map[timestamp]:
            price, timestamp = heappop(self.min_heap)
        heappush(self.min_heap, (price, timestamp))
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()