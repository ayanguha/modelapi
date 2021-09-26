import json, random, os
file_part_1_choices = ['part_' + str(x) for x in range(10,19)]
file_part_2_choices = ['part_' + str(x) for x in range(20,29)]
file_part_3_choices = ['part_' + str(x) for x in range(30,39)]
file_part_4_choices = ['part_' + str(x) for x in range(40,49)]
file_period_choices = ['202006', '202007', '202007']


def genData(n=400):
    o = []


    for num in range(n):

        d = {}
        d['name'] = 'FN' + str(num)
        d['description'] = 'File name ' + str(num)
        d['file_details'] = {}
        d['file_details']['file_part_1'] = random.choice(file_part_1_choices)
        d['file_details']['file_part_2'] = random.choice(file_part_2_choices)
        d['file_details']['file_part_3'] = random.choice(file_part_3_choices)
        d['file_details']['file_part_4'] = random.choice(file_part_4_choices)

        d['file_details']['file_period'] = random.choice(file_period_choices)
        d['latest'] = {}


        d['versions'] = []
        for k in range(3):
            ver = {'version': 'Version ' + str(k), "version_no": str(k), "processed": "2021-09-20 20:00:01"}

            d['latest']['version'] = ver['version']
            status = random.choice([True, True,True,False])
            validations = []
            if status:
                ver['number_of_errors'] = 0
                ver['success'] = True
                for k in ['A','B','C']:
                    val = {'rule_name': 'Rule ' + k, 'msg': "All Good", 'rule_id': 'id'+k, 'succes': True}
                    validations.append(val)

            else:
                ver['number_of_errors'] = 3
                ver['success'] = False
                for k in ['A','B','C']:
                    val = {'rule_name': 'Rule ' + k, 'msg': "Failed", 'rule_id': 'id'+k, 'succes': False}
                    validations.append(val)
            ver['validations'] = validations
            d['latest']['version'] = ver
            d['versions'].append(ver)

        o.append(d)

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_uri = os.path.join(SITE_ROOT, 'file_details.json')
    with open(json_uri, "w") as fo:
        json.dump(o,fo,indent=4)

genData(1000)
