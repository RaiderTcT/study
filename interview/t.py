# coding=utf-8
'''
@Author: Ulysses
@Description: 
@Date: 2020-06-24 20:07:43
@LastEditors: Ulysses
@LastEditTime: 2020-06-25 10:59:10
'''

category_id = 2
resource_num = 10
res_dict = {}
cate_dict = {}

with open('resource.txt', 'r') as res_f:
  line = res_f.readline()
  for line in res_f.readlines():
    ip, cpu, mem = line.split(" | ")
    res_dict[ip] = (int(cpu), int(mem))
print(res_dict)
with open('category.txt', 'r') as cate_f:
  line = cate_f.readline()
  for line in cate_f.readlines():
    cat_id, cpus, mems = line.split(" | ")
    cate_dict[cat_id] = (int(cpus), int(mems))

print(cate_dict)
cpus, mems = cate_dict[str(category_id)]

num_list = [0] * len(res_dict)

for i, ip in enumerate(res_dict):
  num = min(res_dict[ip][0] // cpus, res_dict[ip][1] // mems)
  if num != 0:
    if resource_num > num:
      resource_num -= num
      num_list[i] = num
    else:
      num_list[i] = resource_num
      break

for num, ip in zip(num_list, res_dict.keys()):
  if num != 0:
  	print("{}: {}".format(ip, num))