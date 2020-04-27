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

    def __rtruediv__(self, op):
        if isinstance(op, (int, float)):
            return Vector([op / x for x in self.values])


