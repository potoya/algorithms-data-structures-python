class FixedStack:
    def __init__(self,n):
        self.maxSize=n
        self.list = []
    
    def push(self,element):
        if len(self.list) == self.maxSize:
            self.list.pop(0)
        self.list.append(element)
    
    def toString(self):
        s = ''
        for i in range(0,len(self.list)):
            s += str( self.list[i] )
        return s