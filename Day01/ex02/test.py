from vector import Vector

def main():
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

    print('test __mul__:')
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    v2 = v1 * 5
    print(v1)
    print(v2, end='\n\n')

    print('test __add__:')
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    v2 = v1 + 5
    print(v1)
    print(v2, end='\n\n')

    print('test __radd__:')
    v2 = 5 + v1
    print(v1)
    print(v2, end='\n\n')


    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    print(f'Vector([0.0, 1.0, 2.0, 3.0]):\nvalues: {v1.values}\nsize: {v1.size}\n')

    v1 = Vector(3)
    print(f'Vector(3):\nvalues: {v1.values}\nsize: {v1.size}\n')

    v1 = Vector((10, 15))
    print(f'Vector((10, 15))\nvalues: {v1.values}\nsize: {v1.size}\n')

    print('Vector([0, 1, 2, 3]:')
    v1 = Vector([0, 1, 2, 3])
    print(f'values: {v1.values}\nsize: {v1.size}\n')


if __name__ == "__main__":
    main()