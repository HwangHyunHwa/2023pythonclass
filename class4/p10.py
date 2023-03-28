arr = [20, 30, 10, 5, 20, 9]

arr.append(50)
print('.append(50) >', arr)

b = arr.pop()
print('.pop() >', arr, b)

arr.insert(1, 60)
print('.insert(1,60) >', arr)

arr.remove(20)
print('.delete(20) >', arr)

arr.clear()
print('.clear() >', arr)

arr = [20, 30, 10, 5, 20, 9]

x = arr.index(30)
print('.index(30) >', x)

x = arr.count(20)
print('.count(20) >', x)

arr.sort()
print('.sort() >', arr)

arr.reverse()
print('.reverse() >', arr)