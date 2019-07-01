"""
Data Structures: Sets

A set is an unordered collection without duplicates.

When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.

1	Convert Iterable into Set 					=		set()
2	Set Union  									=		a_set.union()
3	Set Intersection   							=		a_set.intersection()
4	Set Difference 								=		a_set.difference()
5	Set Symmetric Difference 					=		a_set.symmetric_difference()
6	Set Union with Mutation  					=		a_set.update()
7	Set Intersection with Mutation 				=		a_set.intersection_update()
8	Set Difference with Mutation 				=		a_set.difference_update()
9	Set Symmetric Difference with Mutation      =		a_set.symmetric_difference_update()
10	Add Element into Set                        =		a_set.add()
11	Remove Specified Element from Set           =		a_set.remove(), a_set.discard()
12	Remove Arbitrary Element from Set           =       a_set.pop()
13	Test for Subset                             =		a_set.issubset()
14	Test for Superset                           =		a_set.issuperset()
15	Copy Set                                    =		a_set.copy()

# Sets
set()

var1 = '1020'
print(set(var1))

var2 = [1,2,3,4,1,2,3,4]
print(set(var2))

var3 = (1,2,3,4,1,2,3,4)
print(set(var3))

var5 = {1:10,2:10,3:10,4:10}
print(var5)

"""
a = [1,2,3,4,5]
b = [5,6,7]

print(set(a).union(set(b)))
'''Returns the union of set a_set and the set of elements in iterable an_iter.'''

print(set(a).intersection(set(b)))
'''Returns the intersection of set a_set and the set of elements in iterable an_iter.'''

print(set(a).difference(set(b)))
'''Returns a set with all elements from set a_set that are not in iterable an_iter.'''

print(set(a).symmetric_difference(b))
'''Returns a set with all elements that are in exactly one of set a_set and iterable an_iter.'''

"""
s = set((1,2,3,4,5))
s.update(set((6,7,8,9,10)))
print(s)
# Mutates a_set to be the union of set a_set and the set of elements in iterable an_iter. Returns None.
"""
"""
s = set((1,2,3,4,5))
s.intersection_update(set((6,7)))
print(s)
# Mutates a_set to be the intersection of set a_set and the set of elements in iterable an_iter. Returns None.

a1 = set((1,2,3,4,5))
a1.difference_update(set((6,7)))
print(a1)
# Mutates a_set to be the set difference of set a_set and the set of elements in iterable an_iter. Returns None.

s1 = set((1,2,3,4,5))
s1.add(6)
print(s1)


s1.remove(4)
print(s1)

s1.discard(7)
print(s1)
s1.pop()
print(s1)

s2 = set((1,2,3,4,5))
t1 = s2.copy()
print(f"s2 Values : {s2}")
print(f"t1 values : {t1}")

"""


s3 = set([1,2,3,4,5])
s4 = set([1,2])

print(s3.issuperset(s4))

print(set([1,2,3,4,5]).issuperset(set([1,2])))
print(set([1,2,3,4,5]).issuperset(set([3,4])))
print(set([1,2,3,4,5]).issuperset(set([5])))

print(set([1,2]).issubset(set([1,2,3,4,5])))
print(set([3,4]).issubset(set([1,2,3,4,5])))
print(set([5]).issubset(set([1,2,3,4,5])))
