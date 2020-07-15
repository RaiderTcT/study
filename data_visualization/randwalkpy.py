from random import choice

import matplotlib.pyplot as plt

import pygal


class RandWalk:
    def __init__(self, total_point = 10000):
        # 1000步
        self.point = total_point
        # 初始坐标（0，0）
        self.x = [0]
        self.y = [0]
        self.xy = [(0,0)]
    
    def walk(self):
        while len(self.x) < self.point:
            # 向左或右
            x_direction = choice([-1,1])
            # 步幅
            x_distance = choice([0, 1, 2, 3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([-1,1])
            y_distance = choice([0, 1, 2, 3,4])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step
            self.x.append(next_x)
            self.y.append(next_y)
            self.xy.append((next_x, next_y))


if __name__ == "__main__":

        run = RandWalk()
        run.walk()
        point_num = list(range(run.point))
        
        plt.figure(dpi=100, figsize=(10, 6))
        plt.scatter(run.x, run.y, c=point_num, cmap=plt.cm.Reds,
            edgecolor='none', s=10)
        plt.scatter(0, 0, s=30, c='blue', edgecolors='none')
        plt.scatter(run.x[-1], run.y[-1], s= 30, c='green', edgecolors='none')
        plt.axis([-1000,1000,-1000,1000])
        #plt.axes().get_xaxis().set_visible(False)
        #plt.axes().get_yaxis().set_visible(False)
        plt.savefig("RandWalk")
        plt.show()
        """
        print(run.xy[1])
        xy_chart = pygal.XY(stroke = False)
        xy_chart.title = "RandWalk"
        xy_chart.add("walk",run.xy)
        xy_chart.render_to_file("RandWalk.svg")

        """
