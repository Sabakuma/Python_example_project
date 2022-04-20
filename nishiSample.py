import sampleClass
def getEvenList(targetNo:int):
    lst = []
    for i in range(1,targetNo):
        if i % 2 == 0:
            lst.append(i)
    return lst

if __name__ == '__main__':

    # result = "nnnn"
    # targetNumber = input("input : Target Number -> ")
    # while targetNumber.isnumeric() == False :
    #     targetNumber = input("input : Target Number -> ")    
    # evenList = getEvenList(int(targetNumber))
    # print(evenList)
    
    c = sampleClass.SampleClass.method1()