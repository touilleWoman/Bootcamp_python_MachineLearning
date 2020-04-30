def ft_map(function_to_apply, list_of_inputs):
    return (function_to_apply(x) for x in list_of_inputs)


def test():
    def square(n):
        return n * n

    nbs = [0, 1, 2]

    print(map(square, nbs))
    print(set(map(square, nbs)))

    print(ft_map(square, nbs))
    print(set(ft_map(square, nbs)))


if __name__ == "__main__":
    test()
