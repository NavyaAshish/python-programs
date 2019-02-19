import random,pickle,os
nRecords=10000
class Record:
    '''
    OBJECTIVE: To represent a record.
    '''
    
    def __init__(self):
        '''
        OBJECTIVE: To instantiate a Record object.
        INPUT PARAMETERS:
                        self: Implicit object of type Record.
                        key: Key value for the record.(key in the range: (1000000,2000000)
                        others: Other information.
        RETURN VALUE: None.
        '''
        
        self.key=random.randint(1000000,2000000)#(1000000,2000000)
        self.others=str(self.key)*2#random.randint(50,250)

    def __str__(self):
        '''
        OBJECTIVE: To return string of Record.
        INPUT PARAMETERS:
                        self: Implicit object.
        RETURN VALUE: String representation of object.
        '''

        return str(self.key)+":"+self.others

    def getKey(self):
        '''
        OBJECTIVE: To return key value of the Record.
        INPUT PAAMETERS:
                        self: Implicit parameter.
        RETURN VALUE: None.
        '''
        return self.key
 

    def enterRecords(self, nRecords):
        '''
        OBJECTIVE: To enter records in file.
        INPUT PARAMETERS:
                        self: Implicit object.
        RETURN VALUE: None.
        '''
        #os.remove("RecordsNew.txt")
        f=open("RecordsNew.txt","wb")
        lst=[]
        for i in range(0,nRecords):
            flag=True
            while flag:
                r=Record()
                key=r.getKey()
                if key not in lst:
                    flag=False
                    lst.append(key)
                    pickle.dump(r,f)
        f.close()
        

    def createF1F2(self):
        '''
        OBJECTIVE: To create 2 files f1 and f2 and store records of blockSize=4.
        INPUT PARAMETERS:
                        self: Implicit object.
        RETURN VALUE: None.
        '''
        blockSize=4
        f=open("RecordsNew.txt","rb")
        f1=open("File1.txt","wb")
        f2=open("File2.txt","wb")
        r1=[]

        times=nRecords//blockSize
        left=nRecords%blockSize
        fx=f1
        for i in range(0,times):
            r1=[]
            for j in range(0,blockSize):
                r1.append(pickle.load(f))
            t=sorted(r1, key=lambda r:r.key)
            for y in range(0,blockSize):
                pickle.dump(t[y],fx)
            if fx==f1:
                fx=f2
            else:
                fx=f1
        r1=[]
        for i in range(0,left):
            r1.append(pickle.load(f))
        t=sorted(r1, key=lambda r:r.key)
        for y in range(0,left):
            pickle.dump(t[y],fx)
        f1.close()
        f2.close()
        
        f1=open("File1.txt","rb")
        f2=open("File2.txt","rb")
        

    def sortMerge(self,blockSize,f1,f2,fx):
        '''
        OBJECTIVE: To merge records in sorted order.
        INPUT PARAMETER:
                        self: Implicit object.
                        blockSize: Size of block.
                        f1: File1.txt
                        f2: File2.txt
                        fx: File in which to insert the sorted records.
        RETURN VALUE: None.
        '''
        r1=[]
        r2=[]
        x=0
        y=0
        lenR1=0
        lenR2=0
        #print(fx.name)
        for i in range(0,blockSize):
            try:
                r1.append(pickle.load(f1))
                r2.append(pickle.load(f2))
            except:
                continue
        lenR1=len(r1)
        lenR2=len(r2)
        #for i in r1:
         #   print(i.getKey())
        while x<lenR1 and y<lenR2:
            if r1[x].key<r2[y].key:
                pickle.dump(r1[x],fx)
                x+=1
            else:
                pickle.dump(r2[y],fx)
                y+=1
        while x<lenR1:
            pickle.dump(r1[x],fx)
            x+=1
        while y<lenR2:
            pickle.dump(r2[y],fx)
            y+=1

    
            
    def mergeFile(self):
        '''
        OBJECTIVE: To merge records of file f1 ad f2 in sorted form.
        INPUT PARAMETER:
                        self: Implicit object.
        RETURN VALUE: None
        '''
        f1=open("File1.txt","rb")
        f2=open("File2.txt","rb")
        f3=open("File3.txt","ab")
        f4=open("File4.txt","ab")
        temp=0
        blockSize=4
        while nRecords//blockSize:
            count=0
            while count<nRecords:
                self.sortMerge(blockSize,f1,f2,f3)
                self.sortMerge(blockSize,f1,f2,f4)
                count+=blockSize*4
            f1Name=f1.name
            f1.close()
            f2Name=f2.name
            f2.close()
            os.remove(f1Name)
            os.remove(f2Name)
            f3.close()
            f4.close()
            if temp==0:
                f1=open("File3.txt","rb")
                f2=open("File4.txt","rb")
                f3=open("File1.txt","ab")
                f4=open("File2.txt","ab")
                temp=1
            else:
                f1=open("File1.txt","rb")
                f2=open("File2.txt","rb")
                f3=open("File3.txt","ab")
                f4=open("File4.txt","ab")
                temp=0

            blockSize=blockSize*2
        c=0
        if temp==0:
            f1=open("File1.txt","rb")
        else:
            f1=open("File3.txt","rb")

        lower= int(input('Enter the lower limit of record:'))
        upper= int(input('Enter the upper limit of record:'))
        #if upper>nRecords:
        #    print("Out of range")
        #    return
        pickle.load(f1)
        size = f1.tell()
        f1.seek(size*(lower))
        for i in range(lower,upper):
            print(pickle.load(f1).getKey())

if __name__=="__main__":
    ob=Record()
    ob.enterRecords(nRecords)
    ob.createF1F2()
    ob.mergeFile()
    
