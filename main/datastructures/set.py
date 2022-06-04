def intersection_native(set_a, set_b):
    return set_a.intersection(set_b)


def intersection_custom(set_a, set_b):
    result = set()
    for element in set_a:
        if element in set_b:
            result.add(element)
    return result


def union_custom(set_a, set_b):
    result = set()
    for element in set_a:
        result.add(element)
    for element in set_b:
        result.add(element)
    return result


def union_native(set_a, set_b):
    return set_a.union(set_b)
