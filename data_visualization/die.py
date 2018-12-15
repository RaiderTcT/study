from random import randint

class Die:
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides 
    
    def roll(self):
        return randint(1,self.num_sides)
        
if __name__ == "__main__":
    die_6 = Die()
    
    results = []
    for roll_num in range(1, 1000):
        result = die_6.roll()
        results.append(result)
    frequencies = []
    for value in range(1, die_6.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    print(frequencies)