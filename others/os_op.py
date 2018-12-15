import os

print(os.listdir())
# 目录
l = [x for x in os.listdir() if os.path.isdir(x)]
print(l)

li = [x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1] =='.py']
print(li)
print(os.cpu_count())
