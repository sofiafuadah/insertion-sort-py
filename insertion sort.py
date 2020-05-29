###Asccending
def insertionSortAsccending(data):
    print("Data awal :",data)
    print("")
    i = 1
    while i < len(data):
        key = data[i]
        j = i-1
        print("menyisipkan angka :",key)
        while j>=0:
            if key <= data[j]:
                data[j+1]=data[j]
                j -= 1
            else:
                break
            
        data[j+1] = key
        i += 1
        print(data)
        
data = [12, 5, 2, 7, 10]
insertionSortAsccending(data)

#Descending
def insertionSortDescending(data):
    print("Data awal :",data)
    print("")
    i = 1
    while i < len(data):
        key = data[i]
        j = i-1
        print("menyisipkan angka :",key)
        while j>=0:
            if key >= data[j]:
                data[j+1]=data[j]
                j -= 1
            else:
                break
            
        data[j+1] = key
        i += 1
        print(data)
print("")        
data = [12, 5, 2, 7, 10]
insertionSortDescending(data)

def ModifinsertionSortAsccending(data):
    print(" ")
    print("Data awal :",data)
    for i in range(len(data)-2,-1,-1):
        key = data[i]
        j = i+1
        print("menyisipkan angka =",key)
        while j<=len(data)-1 and key>=data[j]:
            data[j-1]=data[j]
            j+=1
        data[j-1]=key
        print(data)

data = [12, 5, 2, 7, 10]
ModifinsertionSortAsccending(data)

def ModifinsertionSortDesccending(data):
    print(" ")
    print("Data awal :",data)
    for i in range(len(data)-2,-1,-1):
        key = data[i]
        j = i+1
        print("menyisipkan angka =",key)
        while j<=len(data)-1 and key<=data[j]:
            data[j-1]=data[j]
            j+=1
        data[j-1]=key
        print(data)

data = [12, 5, 2, 7, 10]
ModifinsertionSortDesccending(data)
