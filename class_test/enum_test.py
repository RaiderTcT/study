from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Weekday = Enum('Weekday', ('Mon', 'Tues', 'Wend',
                           'Thur', 'Fri', 'Sat', 'Sun'))
if __name__ == '__main__':
    print(Month.Jan)
    print(Month['Jan'])
