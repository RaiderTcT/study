import csv
from collections import namedtuple
def txt_write():
    """写
    """
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write('时间')
        lines = [
            'Ulysses\n',
            '2276777056',
            '2018-08-01',
        ]
        f.writelines(lines)
    
    
def csv_read():
    with open('death_valley_2014.csv',encoding='utf-8')as f:
        reader = csv.reader(f)
        head = next(reader)
        for row in reader:
            print(row[0])

def csv_read_by_namedtuple():
    with open('death_valley_2014.csv',encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        Row =namedtuple('Row',head)
        for r in reader:
            row = Row(*r)
            print(row)

def csv_read_by_list():
    with open('death_valley_2014.csv',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            print(r.get('Max TemperatureF', 0))
            
if __name__ == '__main__':
    csv_read()
    #csv_read_by_namedtuple()
    csv_read_by_list()
    