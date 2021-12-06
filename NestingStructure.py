"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.
"""

import numpy as np


def structure_check(array):
    result = []
    for i in array:
        if isinstance(i, list):
            result.append(structure_check(i))
        else:
            result.append("1")
    return result


def same_structure_as(original, other):
    result = np.array(structure_check(original), dtype=object)
    result2 = np.array(structure_check(other), dtype=object)

    return np.array_equal(result, result2)

    # original_np = np.array(original, dtype=object)
    # other_np = np.array(other, dtype=object)

    # original_np = np.array(original)
    # other_np = np.array(other)

    # original_np = np.where(original_np < 100, 0, original_np)
    # original_np = np.where(original_np < 100, 0, original_np)

    # print(original_np)
    # print(other_np)

    # result = np.array_equal(original_np, other_np, equal_nan=False)
    return structure


# should return True
print(same_structure_as([1, "a", 1], [2, 2, 2]))
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))

# should return True
print(same_structure_as([1, 1, 1], [1, 1, 1]))
print(same_structure_as([1, [2, 2]], [1, [2, 2]]))

# should return False
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
print(same_structure_as([1, [1, 1]], [[2], 2]))

# should return True
print(same_structure_as([[[], []]], [[[], []]]))

# should return False
print(same_structure_as([[[], []]], [[1, 1]]))
