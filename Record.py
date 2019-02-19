class Record:
    '''
    Objective: To represent a record entity
    '''
    count = 0
    def __init__(self,key):
        '''
        Objective: To instantiate a Record object
        Input:
            self: Implicit parameter
            key: key value for the record
          others: other information 
        '''
        self.key = key
        Record.count +=1
        self.others = str(self.key)*2#random.randint(50,250)

    def __str__(self):
        '''
        Objective: To override string function
        Input:
            self: Implicit parameter
        Return: STring representation of object
        '''
        return "Record Key "+str(self.key)+" ==> "+self.others

    def getKey(self):
        '''
        Objective: To return key value of a record
        Input:
            self: Implicit paramter
        Return: Key value
        '''
        return self.key
