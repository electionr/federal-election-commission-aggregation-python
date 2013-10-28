import pprint
pp = pprint.PrettyPrinter(indent=4)


class Report ():
    def __init__(self):
        self.data={}

    def add2(self,obj):
        for x in obj.keys():
            v = obj[x]
            if x not in  self.data:
                self.data[x]={}

            if v not in  self.data[x]:
                self.data[x][v]=0

            self.data[x][v]=self.data[x][v]+1
        #pass

    def add(self,obj):
        for x in obj.keys():
            v = obj[x]
            if x not in  self.data:
                self.data[x]=0
            self.data[x]=self.data[x]+1

    def report(self):
        print(pp.pformat(self.data))
