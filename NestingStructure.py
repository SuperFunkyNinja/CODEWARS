"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""

from _typeshed import NoneType
import numpy as np


def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, (int, NoneType, str)):
        yield "number"
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield 
    else:
        yield 1

def reader(o, tree_types=(list, tuple)):
    if 

def same_structure_as(original, other):
    # original_np = np.array(original, dtype=object)
    # other_np = np.array(other, dtype=object)

    result = traverse(original)

    print(list(result))
    # print(original_np)
    # print(other_np)

    # result = np.array_equal(original_np, other_np, equal_nan=False)
    return result


# should return True
print(same_structure_as([1, 1, 1], [2, 2, 2]), "1")
print(same_structure_as([1, [1, 1]], [2, [2, 2]]), "2")

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
