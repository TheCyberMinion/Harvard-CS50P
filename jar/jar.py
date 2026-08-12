class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return ('🍪' * self._size)

    def deposit(self, n):
        if (self._size + n) > self.capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if (self._size - n) < 0:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int):
            if capacity < 0:
                raise ValueError
            else:
                self._capacity = capacity
        else:
            raise ValueError
