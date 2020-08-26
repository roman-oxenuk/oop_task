class Vector:
    def __init__(self, *args):
        self.values = sorted([value for value in args if isinstance(value, int)])
​
    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        return 'Пустой вектор'
​
    def __add__(self, another):
        if isinstance(another, int):
            new_values = [value + another for value in self.values]
            return Vector(*new_values)
​
        elif isinstance(another, Vector):
            if len(self.values) == len(another.values):
                new_values = [first_value + second_value for first_value, second_value in
                              zip(self.values, another.values)]
                return Vector(*new_values)
​
            return print("Сложение векторов разной длины недопустимо")
        return print(f"Вектор нельзя сложить с {another}")
​
    def __mul__(self, another):
        if isinstance(another, int):
            new_values = [value * another for value in self.values]
            return Vector(*new_values)
​
        elif isinstance(another, Vector):
            if len(self.values) == len(another.values):
                new_values = [first_value * second_value for first_value, second_value in
                              zip(self.values, another.values)]
                return Vector(*new_values)
​
            return print("Умножение векторов разной длины недопустимо")
        return print(f"Вектор нельзя умножать с {another}")
