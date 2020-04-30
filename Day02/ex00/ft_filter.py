def ft_filter(function_to_apply, list_of_inputs):
    return (x for x in list_of_inputs if function_to_apply(x))


def test():
    nbs = [0, 1, 2, 3, 4, 5, 100]

    print(filter(lambda p: p % 2 == 0, nbs))
    print(list(filter(lambda p: p % 2 == 0, nbs)))

    print(ft_filter(lambda p: p % 2 == 0, nbs))
    print(list(ft_filter(lambda p: p % 2 == 0, nbs)))


if __name__ == "__main__":
    test()
