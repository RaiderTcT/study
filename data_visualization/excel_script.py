import xlrd


def xl_read():
    book = xlrd.open_workbook('new_weather.xlsx')
    for sheet in book.sheets():
        print(sheet.name)


def xl_read_data():
    book = xlrd.open_workbook('new_weather.xlsx')
    sheet = book.sheet_by_name('weather')
    print(f'工作簿{sheet.name}')
    print(f'数据行：{sheet.nrows}')
    print(sheet.cell(1, 1))
#    print(sheet.cell_xf_index(2,1))
    for i in range(sheet.nrows):
        print(sheet.row_values(i))


        # print(sheet.row_slice(i))
        # print(sheet.row(i))
if __name__ == "__main__":
    xl_read()
    xl_read_data()
