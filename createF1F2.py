from createFile import *
from Record import Record

def createF1F2(fileName,nRecords):
    '''
    Objective : To create blocks of four records
    Input:
        nRecords : Total number of records
        fileName : Name of file which contains the record
    '''
    f = open('File.txt','rb')
    f1 = open('File1.txt','wb')
    f2 = open('File2.txt','wb')
    nodes = nRecords
    blockSize = 4
    times = nodes//blockSize
    remainder = nodes%blockSize
    fh = f1

    #Creating nodes of blockSize
    for i in range(times):
        
        temp = []
        #Writing sorted records in the file1 and file2 alternatively

        for j in range(blockSize):
            temp.append(pickle.load(f))

        temp = sorted(temp, key = lambda x:x.getKey())

        for j in temp:
            pickle.dump(j,fh)
            
        if fh.name == 'File1.txt':
            fh = f2
        else:
            fh = f1

    #If there are any remainder nodes then write those as well
    temp =[]        
    for i in range(remainder):
        temp.append(pickle.load(f))

    temp = sorted(temp, key = lambda x:x.getKey())
    for j in temp:
        pickle.dump(j,fh)
        
    f1.close()
    f2.close()

if __name__ == "__main__":
    createF1F2('File.txt',nRecords)
    print('************ FILE 1 ************')
    readFile('File1.txt')
    print('************ FILE 2 ************')
    readFile('File2.txt')
