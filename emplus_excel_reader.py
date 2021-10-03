from openpyxl import load_workbook
from datetime import datetime
import json



def formatdate(s):
    return datetime.strptime(s, '%d.%m.%y').strftime('%m/%d/%Y')

def get_val(r):
    o = []
    for k in r:
        o.append(k.value)
    return o


def standardize_headers(headers):

    o = []
    for k in headers:
        if k:
            h = k.replace(' ','_').replace('/','_').lower()
            print("k:" + str(k) + "  h:" + str(h))
            o.append(h)


    return o
def parse_edi(filename):
    workbook = load_workbook(filename=filename)

    sheet = workbook.active

    data = []
    details = []
    for row in sheet.rows:

        if row[0].row == 1:

            headers = standardize_headers(get_val(row))
        else:
            details.append(get_val(row))


    for detail in details:
        record = {}
        zipped = zip(headers,detail)
        for z in zipped:
            record[z[0]] = str(z[1])
        data.append(record)


    return data

filename = 'tasks.xlsx'
data = parse_edi(filename)
print(data[0])
with open('tasks.json','w') as fo:
    json.dump(data,fo,indent=4)
