import pygal
from die import Die
import matplotlib.pyplot as plt
import numpy as py
if __name__ == "__main__":
    die_6 = Die()
    die_6_2 = Die()
    results1 = []
    results2 = []
    for roll_num in range(1, 1000):
        result1 = die_6.roll()
        results1.append(result1)
        result2 = die_6_2.roll()
        results2.append(result2)
    frequencies1 = []
    frequencies2 = []
    for value in range(1, die_6.num_sides + 1):
        frequency1 = results1.count(value)
        frequencies1.append(frequency1)
        frequency2 = results2.count(value)
        frequencies2.append(frequency2)
    """ 
    hist = pygal.StackedBar()
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.title = "Result of rolling one D6 for 1000 times"
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'
    
    hist.add("D6_1", frequencies1)
    hist.add("D6_2", frequencies2)
    hist.render_to_file('die_visual.svg')
    """
    plt.bar(range(1, die_6.num_sides + 1), frequencies1)
    plt.show()
