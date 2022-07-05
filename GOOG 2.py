"""
Design a data structure to perform three operations (Restaurant is full initially):
1) waitList (int group_size, int table_size):
Add the group and table size they want to book into the waitlist
2) leave (int group_size):
Group wants to leave the waitlist so remove them.
3) serve (int table_size):
This means restaurant now has a free table of size equal to table_size. 
Find the group whose required size is less than or equal to the table_size. 
If multiple customers are matching use first come first serve. to serve from waitlist
"""

from collections import deque

class Waitlist:
    def __init__(self):
        self.q = deque()

    def add(self, party_size, party_id):
        self.q.append((party_id, party_size))

    def remove_by_idx(self, idx):
        del self.q[idx]

    def remove_by_party(self, party_id):
        for idx, (id, _) in enumerate(self.q):
            if id == party_id:
                self.remove_by_idx(idx)

    def seat_party(self, table_size):
        for idx, (_, party_size) in enumerate(self.q):
            if table_size >= party_size:
                self.remove_by_idx(idx)