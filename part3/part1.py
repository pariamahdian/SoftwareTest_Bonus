
class InputDomainModeler: 
    def __init__(self,char,blockAbs): 
        self.characteristics = char 
        self.blocks_abstracts = blockAbs
    
    def getBlockAbs(self):
        return self.blocks_abstracts 
        

def generate_model(objects,working_mode):
    lists = []
    base =[]
    for i in objects:
        obj = i.getBlockAbs()
        lists.append(obj)
        base.append(obj[0])
    if working_mode == 'BCC':
        print("Base:",base)
        for i in range(len(objects)):
            for j in range(1,len(objects[i].getBlockAbs())):
                changedBase = base.copy()
                changedBase[i] = objects[i].getBlockAbs()[j]
                print(changedBase)
    elif working_mode == 'ACoC':
        for k in range(len(objects)):
            for i in range(k,len(objects)):
                for j in range(len(objects[i].getBlockAbs())):
                    changedBase = base.copy()
                    changedBase[i] = objects[i].getBlockAbs()[j]                        
                    print(changedBase)
    elif working_mode == 'ECC':
        size = 0
        index = 0
        for i in range(len(objects)):
           if len(objects[i].getBlockAbs()) > size:
               size = len(objects[i].getBlockAbs())
               index = i
        for i in objects[index].getBlockAbs():
            changedBase = base.copy()
            changedBase[index] = i
            print(changedBase) 
    else:
        print("invalid mode")
    return
    
            
if __name__ == "__main__":  
    

    # Example input 
    char1 = 'A'
    block1 = ['a1', 'a2']
    obj1 = InputDomainModeler(char1,block1)
    
    char2 = 'B'
    block2 = ['b1', 'b2']
    obj2 = InputDomainModeler(char2,block2)
    
    char3 = 'C'
    block3 = ['c1', 'c2', 'c3']
    obj3 = InputDomainModeler(char3,block3)
    
    char4 = 'D'
    block4 = ['d1', 'd2']
    obj4 = InputDomainModeler(char4,block4)

    objects = [obj1, obj2, obj3, obj4] 
    mode = input("Please enter the working mode:")   
    generate_model(objects,mode)
