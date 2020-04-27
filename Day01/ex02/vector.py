class Vector:
    def __init__(self, values):
        if isinstance(values, list) and all(isinstance(x, float) for x in values):
            self.values = values
            self.size = len(self.values)
        elif isinstance(values, int):
            self.values = [float(x) for x in range(0, values)]
            self.size = values
        elif isinstance(values, tuple) and len(values) == 2:
            self.values = [float(x) for x in range (values[0], values[1])]
            self.size = len(self.values)
        else:
            raise TypeError

    def __str__(self):
        return 'Vector ' + str(self.values)
    
    def __repr__(self):
        return {'values':self.values, 'size':self.size}

    def __mul__(self, op):
        if isinstance(op, (int, float)):
            return(Vector([x * op for x in self.values]))

    def __rmul__(self, op):
        return(self.__mul__(op))

    def __add__(self, op):
        if isinstance(op, (int, float)):
            return Vector([x + op for x in self.values])

    __radd__ = __add__

    def __sub__(self, op):
        if isinstance(op, (int, float)):
            return Vector([x - op for x in self.values])

    def __rsub__(self, op):
        if isinstance(op, (int, float)):
            return Vector([op - x for x in self.values])

    def __truediv__(self, op):
        if isinstance(op, (int, float)):
            return Vector([x / op for x in self.values])


print('test __truediv__:')
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 / 5.0
print(v1)
print(v2, end='\n\n')

print('test __sub__:')
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 - 2.0
print(v1)
print(v2, end='\n\n')

print('test __rsub__:')
v2 = 2 - v1
print(v1)
print(v2, end='\n\n')

# print('test __mul__:')
# v1 = Vector([0.0, 1.0, 2.0, 3.0])
# v2 = v1 * 5
# print(v1)
# print(v2, end='\n\n')

print('test __add__:')
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 + 5
print(v1)
print(v2, end='\n\n')

print('test __radd__:')
v2 = 5 + v1
print(v1)
print(v2, end='\n\n')


# v1 = Vector([0.0, 1.0, 2.0, 3.0])
# print(f'Vector([0.0, 1.0, 2.0, 3.0]):\nvalues: {v1.values}\nsize: {v1.size}\n')

# v1 = Vector(3)
# print(f'Vector(3):\nvalues: {v1.values}\nsize: {v1.size}\n')

# v1 = Vector((10, 15))
# print(f'Vector((10, 15))\nvalues: {v1.values}\nsize: {v1.size}\n')

# print('Vector([0, 1, 2, 3]:')
# v1 = Vector([0, 1, 2, 3])
# print(f'values: {v1.values}\nsize: {v1.size}\n')
