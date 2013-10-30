import pprint
pp = pprint.PrettyPrinter(indent=4)
import re

bundle = {
    '_DONOR' :[
        'DONOR CANDIDATE STATE',
        'DONOR CANDIDATE DISTRICT',
        'DONOR CANDIDATE OFFICE',
        'DONOR CANDIDATE FEC ID',
        'DONOR COMMITTEE FEC ID',
        'DONOR COMMITTEE NAME',
        'DONOR CANDIDATE PREFIX',
        'DONOR CANDIDATE FIRST NAME',
        'DONOR CANDIDATE MIDDLE NAME',
        'DONOR CANDIDATE LAST NAME',     
        'DONOR CANDIDATE SUFFIX',
    ],

    'GUARANTOR': [
        'GUARANTOR STATE',
        'GUARANTOR ZIP',
        'GUARANTOR CITY',
        'GUARANTOR STREET 1',
        'GUARANTOR STREET 2',

        'GUARANTOR EMPLOYER',

        'GUARANTOR PREFIX',
        'GUARANTOR FIRST NAME',
        'GUARANTOR MIDDLE NAME',
        'GUARANTOR LAST NAME',
        'GUARANTOR SUFFIX',
        'GUARANTOR OCCUPATION',
    ],

    'PCC': [
        'PCC STATE',
        'PCC ZIP',
        'PCC CITY',
        'PCC STREET 1',
        'PCC STREET 2',
        'PCC COMMITTEE ID NUMBER',
        'PCC COMMITTEE NAME',
    ],

    'SUBORDINATE' : [
        'SUBORDINATE STATE',
        'SUBORDINATE ZIP'
        'SUBORDINATE CITY',
        'SUBORDINATE STREET 1',
        'SUBORDINATE STREET 2',        
        'SUBORDINATE COMMITTEE ID NUMBER',
        'SUBORDINATE COMMITTEE NAME',    
    ],

    'TREASURER': [
        'TREASURER STATE',
        'TREASURER ZIP'
        'TREASURER CITY',
        'TREASURER STREET 1',
        'TREASURER STREET 2',

        'TREASURER TITLE',
        'TREASURER PREFIX',
        'TREASURER FIRST NAME',
        'TREASURER MIDDLE NAME',
        'TREASURER LAST NAME',
        'TREASURER SUFFIX',

        'TREASURER TELEPHONE',
    ],

    'AFFILIATED': [
        'AFFILIATED STATE',
        'AFFILIATED ZIP'
        'AFFILIATED CITY',
        'AFFILIATED STREET 1',
        'AFFILIATED STREET 2',

        'AFFILIATED CANDIDATE ID NUM',
        'AFFILIATED COMMITTEE FEC ID',
        'AFFILIATED COMMITTEE NAME',
        'AFFILIATED Committee ID NUM',
        'AFFILIATED Committee NAME',

        'AFFILIATED PREFIX',
        'AFFILIATED FIRST NAME',
        'AFFILIATED MIDDLE NAME',
        'AFFILIATED LAST NAME',
        'AFFILIATED SUFFIX',

        'AFFILIATED RELATIONSHIP CODE',  
    ],

    'AUTH': [
        'AUTH STATE',
        'AUTH ZIP'
        'AUTH CITY',
        'AUTH STREET 1',
        'AUTH STREET 2',        
        'AUTH COMMITTEE ID NUMBER',
        'AUTH COMMITTEE NAME',
    ],

    'BANK': [
        'BANK STATE',
        'BANK CITY',
        'BANK ZIP'
        'BANK STREET 1',
        'BANK STREET 2',
        'BANK NAME',    
    ],

    'CONDUIT': [
        'CONDUIT STATE',
        'CONDUIT ZIP',
        'CONDUIT CITY',
        'CONDUIT STREET 1',
        'CONDUIT STREET 2',
        'CONDUIT STREET1',
        'CONDUIT STREET2',
        'CONDUIT NAME',
    ],

    "_CUSTODIAN" : [
        'CUSTODIAN STATE',
        'CUSTODIAN ZIP',
        'CUSTODIAN CITY',
        'CUSTODIAN STREET 1',
        'CUSTODIAN STREET 2',
        'CUSTODIAN TITLE',
        'CUSTODIAN PREFIX',
        'CUSTODIAN FIRST NAME',
        'CUSTODIAN MIDDLE NAME',
        'CUSTODIAN LAST NAME',
        'CUSTODIAN SUFFIX',
        'CUSTODIAN TELEPHONE',
    ] ,

    '_SOCANDIDATEDISTRICT':  [ 
        'S/O CANDIDATE STATE',
        'S/O CANDIDATE DISTRICT',
        'S/O CANDIDATE OFFICE',
        'S/O CANDIDATE ID NUMBER',
        'S/O CANDIDATE PREFIX',
        'S/O CANDIDATE FIRST NAME',
        'S/O CANDINATE MIDDLE NAME',
        'S/O CANDIDATE LAST NAME',
        'S/O CANDIDATE SUFFIX',
    ],

    '__record_type' :
    [ 
        '_record_type',
    ],

    '_OTHER' :
    [ 
        'ZIP',
        'STATE',
        'STATE OF ELECTION',
        'STREET 1',
        'STREET 2',
    ],

    '_ELECTION' : [
        'ELECTION CODE',
        'ELECTION DISTRICT',
        'ELECTION OTHER DESCRIPTION',
        'ELECTION STATE',
    ],

    "_LENDER": [
        'LENDER STATE',
        'LENDER CANDIDATE STATE',
        'LENDER CANDIDATE DISTRICT',
        'LENDER ZIP',
        'LENDER CITY',
        'LENDER STREET 1',
        'LENDER STREET 2',
        'LENDER CANDIDATE ID NUMBER',
        'LENDER COMMITTEE ID NUMBER',
        'LENDER CANDIDATE PREFIX',
        'LENDER CANDIDATE FIRST NAME',
        'LENDER CANDIDATE MIDDLE NM',
        'LENDER CANDIDATE LAST NAME',
        'LENDER CANDIDATE SUFFIX',
        'LENDER CANDIDATE OFFICE',  
        'LENDER ORGANIZATION NAME',
        'LENDER PREFIX',
        'LENDER FIRST NAME',
        'LENDER MIDDLE NAME',
        'LENDER LAST NAME',
        'LENDER SUFFIX',
    ],

    '_CREDITOR' : [
        'CREDITOR STATE',
        'CREDITOR ZIP',
        'CREDITOR CITY',
        'CREDITOR STREET 1',
        'CREDITOR STREET 2',
        'CREDITOR ORGANIZATION NAME',
        'CREDITOR PREFIX',
        'CREDITOR FIRST NAME',
        'CREDITOR MIDDLE NAME',
        'CREDITOR LAST NAME',
        'CREDITOR SUFFIX',
    ],

    '_CONTRIBUTOR':
    [ 
        'CONTRIBUTOR STATE',
        'CONTRIBUTOR ZIP',
        'CONTRIBUTOR CITY',
        'CONTRIBUTOR STREET 1',
        'CONTRIBUTOR STREET 2',
        #
        'CONTRIBUTOR COMMITTEE FEC ID',
        'CONTRIBUTOR PREFIX',
        'CONTRIBUTOR FIRST NAME',
        'CONTRIBUTOR MIDDLE NAME',
        'CONTRIBUTOR LAST NAME',
        'CONTRIBUTOR SUFFIX',
        ##
        'CONTRIBUTOR OCCUPATION',
        'CONTRIBUTOR EMPLOYER',
        'CONTRIBUTOR ORGANIZATION NAME',
    ],

    '_BENEFICIARY_CANDIDATE':
    [ 
        'BENEFICIARY CANDIDATE STATE',
        'BENEFICIARY CANDIDATE DISTRICT',
        'BENEFICIARY CANDIDATE FEC ID',
        'BENEFICIARY CANDIDATE OFFICE',
        'BENEFICIARY COMMITTEE FEC ID',
        'BENEFICIARY COMMITTEE NAME',
        'BENEFICIARY CANDIDATE PREFIX',
        'BENEFICIARY CANDIDATE FIRST NAME',
        'BENEFICIARY CANDIDATE MIDDLE NAME',
        'BENEFICIARY CANDIDATE LAST NAME',
        'BENEFICIARY CANDIDATE SUFFIX',
    ],
    
    '_CANDIDATE': [
        'CANDIDATE STATE',
        'CANDIDATE DIST',
        'CANDIDATE DISTRICT',
        'CANDIDATE ZIP',
        'CANDIDATE CITY',
        'CANDIDATE STREET 1',
        'CANDIDATE STREET 2',
        'CANDIDATE ID NUMBER',
        ##
        'CANDIDATE OFFICE',
        'CANDIDATE PARTY CODE',
        ##
        'CANDIDATE PREFIX',
        'CANDIDATE FIRST NAME',
        'CANDIDATE LAST NAME',
        'CANDIDATE MIDDLE NAME',
        'CANDIDATE SUFFIX',
        ##
        'CANDIDATE SIGNATURE PREFIX',
        'CANDIDATE SIGNATURE FIRST NAME',
        'CANDIDATE SIGNATURE LAST NAME',
        'CANDIDATE SIGNATURE MIDDLE NAME',
        'CANDIDATE SIGNATURE SUFFIX',
        ],

    '_AUTH' :    [
        'AUTH STATE',
        'AUTH ZIP',
        'AUTH STREET 1',
        'AUTH STREET 2',
        'AUTH CITY',
        'AUTH COMMITTEE ID NUMBER',
        'AUTH COMMITTEE NAME',
    ],

    '_AGENT': [
        'AGENT STATE',
        'AGENT ZIP',
        'AGENT CITY',
        'AGENT STREET 1',
        'AGENT STREET 2',
        'AGENT TITLE',
        'AGENT PREFIX',
        'AGENT FIRST NAME',
        'AGENT MIDDLE NAME',
        'AGENT LAST NAME',
        'AGENT SUFFIX',
        'AGENT TELEPHONE',
    ],      

    '_PAYEE': [
        'PAYEE STATE',
        'PAYEE CANDIDATE STATE',
        'PAYEE CANDIDATE DISTRICT',
        'PAYEE ZIP',
        'PAYEE CITY',
        'PAYEE STREET 1',
        'PAYEE STREET 2',
        'PAYEE COMMITTEE ID NUMBER',
        'PAYEE Committee FEC ID NUMBER',
        'PAYEE ORGANIZATION NAME',
        'PAYEE CANDIDATE ID NUMBER',
        'PAYEE CANDIDATE OFFICE',
        'PAYEE CANDIDATE PREFIX',
        'PAYEE CANDIDATE FIRST NAME',
        'PAYEE CANDIDATE MIDDLE NAME',
        'PAYEE CANDIDATE LAST NAME',
        'PAYEE CANDIDATE SUFFIX',
        'PAYEE PREFIX',
        'PAYEE FIRST NAME',
        'PAYEE MIDDLE NAME',
        'PAYEE LAST NAME',
        'PAYEE SUFFIX'    
    ]
    
}

class Report ():
    def __init__(self):
        self.data={}
        self.data_b={}
        self.data_id={}

    def add2(self,obj):
        for x in obj.keys():
            v = obj[x]
            if x not in  self.data:
                self.data[x]={}

            if v not in  self.data[x]:
                self.data[x][v]=0

            self.data[x][v]=self.data[x][v]+1
        #pass

    def add1(self,obj):
        for x in obj.keys():
            v = obj[x]
            if x not in self.data_id:
                self.data_id[x]=0
            self.data_id[x]=self.data_id[x]+1

    def add_bundle(self,obj):
        for b in bundle.keys():
            v2=[]
            for x in bundle[b]:
                if x in obj:
                    v = obj[x]
                else:
                    v= ""
                v2.append(v)
            v="|".join(v2)
            if b not in self.data_b:
                self.data_b[b]={}
            if v not in self.data_b[b]:
                self.data_b[b][v]=1
            else:
                self.data_b[b][v]=self.data_b[b][v]+1

    def add(self,obj):
      #  self.add2(obj)
      #  self.add1(obj)
        self.add_bundle(obj)

    def report_file(self,fname,name,data):
        f=open (fname,"w")
        f.write("def load() :\n\t return {'name':u'''%s''', 'data'=" % name)
        f.write(pp.pformat(data))
        f.flush()
        f.close()

    def report(self):
        self.report_file("simple.py","simple",self.data_id)

        for x in self.data_b.keys():
            fname="report_b/%s.py" % x
            self.report_file(fname,x,self.data_b[x])

        for x in self.data.keys():
            n=x 
            n = re.sub(r'\W', "_", n)
            fname="report/tmp_%s.py" % n
            self.report_file(fname,x,self.data[x])



