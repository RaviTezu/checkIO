#!/usr/bin/python

def nonUniqueElements(array):
    """Takes a List and returns a List consisting of only 
       the non-unique elements in this list"""
    counts = {}
    for el in array:
        counts[el] = counts.get(el, 0) + 1 
    for k,v in counts.iteritems():
        if v == 1:
            array.remove(k)
    return array


x = [1, 2, 3, 1, 3]
print nonUniqueElements(x)
y = [1, 2, 3, 1, 3]
print nonUniqueElements(y)
z = [1, 2, 3, 4, 5]
print nonUniqueElements(z)
