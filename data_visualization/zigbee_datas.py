import csv

if __name__=="__main__":
    filename = "zigbee_out.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, value in enumerate(header_row):
            print(index, value)
        
        data = []
        for row in reader :
            data.append(row)
            #print(reader.line_num, row)
        print(data[1:10])