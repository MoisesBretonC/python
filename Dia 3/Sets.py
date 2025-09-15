mi_set = set({1,2,3,4,5,6,7,2,2,2,2,8,9,2})
print(type(mi_set))
print(mi_set)

mi_set2 = set({1,2,3,4,5,6,7})
print(len(mi_set2))

mi_set3 = set({1,2,3,4,5,6,7})
print(2 in mi_set3)

s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)

s4 = {1,2,3}
s4.add(45)
print(s4)

s5 = {1,2,3}
s5.remove(1)
print(s5)

s6 = {1,2,3}
s6.discard(2)
print(s6)

s7 = {1,2,3}
sorteo = s7.pop()
print(sorteo)

s8 = {1,2,3}
s8.clear()
print(s8)