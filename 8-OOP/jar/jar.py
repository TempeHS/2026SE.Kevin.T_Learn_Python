class Jar:
    def __init__(self, capacity=12, amount=0):
        self.capacity = capacity
        self.amount = amount

    def __str__(self):
        # return n * "🍪"
        ...

    def deposit(self, n):
        if (n + self.amount) > self.capacity:
            raise ValueError("Too many cookies")
        self.amount += n

    def withdraw(self, n):
        if n > self.amount:
            raise ValueError("Not enough cookies left")
        self.amount -= n

    # getter
    @property
    def capacity(self):
        return self._capacity
    
    # setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity cannot be lower than 1")
        self._capacity = capacity

    # # Getter for house
    # @property
    # def house(self):
    # 	return self._house

    # # Setter for house
    # @house.setter
    # def house(self, house):
    # 	if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    # 		raise ValueError("Invalid house")
    # 	self._house = house

    @property
    def size(self):
        return self._amount
    
    @size.setter
    def size(self, size):
        if 