from t792733_fec_1_yml import load
data = load()

report = {}

# skip the first row
for row in data['rows']:
    if (isinstance(row,int)):
        pass
    else:
        record = row['record']
        result = row['result']
        newres = {}
        for x in result:
            v = x['value']
            n = x['name']
            if (len(v)):
                newres[n]=v

                if n not in report:
                    report[n]=0

                report [n] = report [n] +1

#        final.append(newres)


import pprint
fo = open("simpleout.py","w")
pp = pprint.PrettyPrinter(indent=4)
#fo.write(pp.pformat(final))

pp.pprint(report)
