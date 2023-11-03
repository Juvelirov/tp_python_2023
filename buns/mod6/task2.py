class DoubleElement:

    def __init__(self, *lst):
        self.list = lst
        self.index = 0

    def __next__(self):
        if self.index < len(self.list):
            first_value = self.list[self.index]
            second_value = None
            self.index += 1
            if self.index < len(self.list):
                second_value = self.list[self.index]
                self.index += 1
            return first_value, second_value
        else:
            raise StopIteration

    def __iter__(self):
        return self


elem = DoubleElement(1, 2, 3, 4)
for pair in elem:
    print(pair)

print()

elem = DoubleElement(1, 2, 3, 4, 5)
for pair in elem:
    print(pair)