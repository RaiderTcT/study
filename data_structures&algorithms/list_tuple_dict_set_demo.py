l1 = [1, 2, 3, 4]
d1 = {"name": "jack", "id": 1}
l1.extend(d1)
print(l1)

l2 = [x for x in range(20)]
print(l2[3:15:2])


t1 = ("id", "name", ["A", "B"])
t1[2][0] = "x"
t1[2][1] = "y"
print(t1)

print("\031[显示方式;前景色;背景色m正文\031[0m")
