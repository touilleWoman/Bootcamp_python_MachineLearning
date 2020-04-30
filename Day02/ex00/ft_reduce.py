from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    ret = list_of_inputs[0]
    for x in range(1, len(list_of_inputs)):
        ret = function_to_apply(ret, list_of_inputs[x])
    return ret

def test():
    nbs = [1, 2, 3, 4, 5]
    print(reduce(lambda a, b: a * b, nbs))
    print(ft_reduce(lambda a, b: a * b, nbs))

    nbs = [1, 2]
    print(reduce(lambda a, b: a * b, nbs))
    print(ft_reduce(lambda a, b: a * b, nbs))


if __name__ == "__main__":
    test()
