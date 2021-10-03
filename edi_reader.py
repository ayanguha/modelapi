from openpyxl import load_workbook
from datetime import datetime
import json

def getFileDetails(fname):
    tokens = fname.split(".")[0].split('-')
    file_details = {}
    file_details['vendor_short_name'] = tokens[0]
    file_details['period'] = tokens[1]
    file_details['post_type'] = tokens[2]
    file_details['file_id'] = tokens[3]
    file_details['file_category'] = tokens[4]
    file_details['invoice'] = tokens[5]
    file_details['invoice'] = tokens[5]

    return file_details


def parse_edi(filename):
    file_details = getFileDetails(filename)
    version = datetime.now().strftime('%Y%m%d%H%M%S')
    workbook = load_workbook(filename=filename, data_only=True)

    sheet = workbook.active
    top = {}
    top['header_text'] = sheet["C4"].value
    top['document_type'] = sheet["C5"].value
    top['document_date'] = sheet["C6"].value
    top['calc_tax'] = sheet["F4"].value
    top['company_code'] = sheet["F5"].value
    top['posting_date'] = sheet["F6"].value
    top['document_reference'] = sheet["I4"].value
    top['currency'] = sheet["I5"].value
    top['vendor_code'] = sheet["C12"].value
    top['total_amount'] = sheet["D12"].value

    top['version'] = version
    top['filename'] = filename



    headers = {**top, **file_details}

    details = []
    for row in sheet.rows:
        if row[0].row >= 14:
            record = {}
            record['posting_key'] = row[1].value
            record['gl_account'] = row[2].value
            record['line_amount'] = row[3].value
            record['costcenter'] = row[4].value
            record['line_text'] = row[6].value

            record['line_number'] = row[0].row
            record['filename'] = filename
            record['version'] =  version

            if (row[6].value):
                record['emplus_ref'] = (row[6].value).split('-')[0]
                record['site_name_line_text'] = (row[6].value).split('-')[2]
                record['task_type'] = (row[6].value).split('-')[4]

            details.append(record)

    data = {}
    data['headers'] = headers
    data['details'] = details

    return data

filename = 'Car_Kleen-202107-DR-All-PPM-66986.xlsx'
data = parse_edi(filename)

with open('data.json','w') as fo:
    json.dump(data,fo,indent=4)
