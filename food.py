class Food:
    def __init__(self, quantifier):
        self.quantifier = quantifier

    def calories(self, calories) -> int:
        calories = 0

        # raise NotImplementedError()

    def weight(self, weight) -> int:
        weight = 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Food):
            return NotImplemented

        # TODO

    def __lt__(self, other: object) -> int:
        if not isinstance(other, Food):
            return NotImplemented

        # TODO


class Apples(Food):
    # def __init__(self, amount):
    #     self.weight = self.weight
    #     self.calories = self.calories
    #     self.amount = amount

    def calories(self):
        Food.calories = 102 * self.amount
        return Food.calories

    def weight(self):
        Food.weight = 200 * self.amount
        return Food.weight


class Oranges(Food):
     # def __init__(self, amount):
     #    self.amount = amount

    def calories(self):
        Food.calories = 94 * self.amount
        return Food.calories

    def weight(self):
        Food.weight = 200 * self.amount
        return Food.weight






class CookieDough(Food):
    # def __init__(self, weight):
    #    self.weight = weight

    def calories(self):
     Food.calories = int(2.44 * self.weight)
     return Food.calories

def weights(self):
    Food.weight = int(self.weight)
    return Food.weight


if __name__ == "__main__":
    A1 = Apples(4)
    print(A1.calories())
    print(A1.weight())
    A2 = Oranges(3)
    print(A2.calories())
    print(A2.weight())
    A3 = CookieDough(5)
    print(A3.calories())
    print(A3.weights())

# TODO: Remove all lines, that contain "# TODO:"...
