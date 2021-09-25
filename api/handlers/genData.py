import json, random, os


def genData(n=400):
    o = []


    for num in range(n):

        d = {}
        d['name'] = 'FN' + str(num)
        d['description'] = 'File name ' + str(num)
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
