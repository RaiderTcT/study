import json
import pickle


class Student(object):

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'id': std.id
    }


if __name__ == '__main__':

    std_1 = Student('jk', 22, 1234)
    std_2 = Student('jane', 22, 12)

    with open(r'dump.txt', 'wb') as f:
        pickle.dump(student2dict(std_1), f)

    with open(r'dump.txt', 'rb') as f:
        d = pickle.load(f)
        print(d)

    with open(r"D:\python_project\data_visualization\std.json", 'w') as f:

        # json.dump([std_1, std_2], f, default=student2dict, ensure_ascii=False)
        # 是否对中文进行ascii编码
        json.dump([std_1, std_2], f, default=lambda x: x.__dict__,
                  ensure_ascii=True)

    with open(r"D:\python_project\data_visualization\std.json") as f:
        print(json.load(f))
