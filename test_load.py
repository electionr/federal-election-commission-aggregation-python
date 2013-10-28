from t792733_fec_1_yml import load

data = load()

#(count,rows)= data['rows']

final = []
filename = data['filename']

# skip the first row
for row in data['rows']:
    if (isinstance(row,int)):
        #print type( row )
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
        newres['_filename']=filename
        newres['_record_type']=record
        final.append(newres)


import pprint
fo = open("simpleout.py","w")
pp = pprint.PrettyPrinter(indent=4)
fo.write(pp.pformat(final))
