#+++++++++++++++++++++++++  STUDENT RECORD  ++++++++++++++++++++++++++++++++++++++++++++++++

class StudentRecord:
    def __init__(self,i,name):
        self.studentId=i
        self.studentName = name
        
    def Get_Student_Id(self):
        return self.studentId
    
    def Set_Student_Id(self,i):
        self.studentId=i
        
    def __str__(self):
        return str(self.studentId) + "" + self.studentName

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
#--------------------------------------Linear Probing------------------------------------  
class Hashtable:
    def __init__(self,tableSize):
        self.m=tableSize
        self.arr=[None] * self.m
        self.n=0
        
    def Hashh(self,key):
        return (key % self.m)
    
    def Insert(self,newRecord):
        key=newRecord.Get_Student_Id()
        h=self.Hashh(key)
        
        location=h
        
        for i in range(1,self.m):
            if self.arr[location] is None or self.arr[location].Get_Student_Id() == -1:
                self.arr[location]=newRecord
                self.n+=1
                return
            if self.arr[location].Get_Student_Id() == key:
                location = self.Hashh(location+1)
            location =(h + i) % self.m
        print("Table is Full : Record can't be Inserted ")
     
        
    def Search(self,key):
        h=self.Hashh(key)
        location = h
        
        for i in range(1,self.m):
            if self.arr[location] is None:
                return None
            if self.arr[location].Get_Student_Id() == key:
                return self.arr[location]
            location=(h+i) % self.m
        return None
    
    def Display_Table(self):
        for i in range(self.m):
            print("[",end="");print(i,end="");print("]",end="");
            
            if self.arr[i] is not None and self.arr[i].Get_Student_Id() != -1:
                print(self.arr[i])
            else:
                print("____")
        
    def delete(self,key):
        h=self.Hashh(key)
        location=h
        
        for i in range(1,self.m):
            if self.arr[location] is None:
                return None
            
            if self.arr[location].Get_Student_Id() == key:
                temp=self.arr[location]
                self.arr[location].Set_Student_Id(-1)
                self.n-=1
                return temp
            location=(h+i) % self.m
        return None

#-----------------------------------SEPERATE CHAINING--------------------------------------   

class Node:
    def __init__(self,value):
        self.Value = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.start=None
        
    def Display_List(self):
        if self.start is None:
            print("_______")
            return 
        p=self.start
        while p is not None:
            print(p.Value," ", end="")
            p=p.next
        print()
    def Search(self,x):
        p=self.start
        while p is not None:
            if p.Value.Get_Student_Id() == x:
                return p.Value
            p=p.next
        else:
            return None
    def Insert_First(self,data):
        temp =Node(data)
        temp.next=self.start
        self.start=temp
    
    def delete_node(self,x):
        if self.start is None:
            print("List is Empty")
            return
        
        #deletion of firs Node
        
        if self.start.Value.Get_Student_Id() == x:
            self.start = self.start.next
            return
        #deletoin in Between or at the end
        
        p=self.start
        while p.next is not None:
            if p.next.Value.Get_Student_Id() == x:
                break
            p=p.next
        if p.next is None:
            print("Element ", x ," not in list")
        else:
            p.next =p.next.next
                
class HashTabe:
    def __init__(self,tableSize):
        self.m=tableSize
        self.arr=[None] * self.m
        self.n=0
    
    def Hash(self,key):
        return (key % self.m)
    
    def Display_Table(self):
        for i in range(self.m):
            print("[", i ," ]  --> ", end=' '  )
            if self.arr[i]!=None:
                self.arr[i].Display_List()
            else:
                print("____")
    
    def Search(self,key):
        h=self.Hash(key)
        if self.arr[h] != None:
            return self.arr[h].Search(key)
        return None

        
    def insert(self,newRecord):
        key=newRecord.Get_Student_Id()
        h=self.Hash(key)
        
        if self.arr[h] == None:
            self.arr[h] = SinglyLinkedList()
        self.arr[h].Insert_First(newRecord)
        self.n+=1
        
    def delete(self,key):
        h =self.Hash(key)
        if self.arr[h] != None:
            self.arr[h].delete_node(key)
            self.n-=1
        else:
            print("Value", key,"not present")
            
            
#================================DRIVER CODE==========================================       
print("=====================BY LINEAR PROBING======================")
size=int(input("Enter size of table:"))
table=Hashtable(size)

while True:
    print("1. Insert a record")
    print("2. Search a Record")
    print("3. Delete a Record")
    print("4. Display Table")
    print("5. Exit")
    
    choice =int(input("Enter your choice : "))
    if choice == 1:
        id =int(input("Enter student id : "))
        name=input("Enter Student Name : ")
        aRecord =StudentRecord(id, name) 
        print("")
        table.Insert(aRecord)
        
    elif choice == 2:
        id=int(input("Enter a Key to be Searched : "))
        aRecord =table.Search(id)
        if aRecord is None:
            print("Key Not Found")
        else:
            print(aRecord)
            
    elif choice == 3:
        
        id=int(input("Enter a key to be deleted : "))
        table.delete(id)
    elif choice == 4:
        table.Display_Table()
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Wrong Option")
    print()
            
            
            
            
print("=====================BY SEPERATE CHAINING======================") 
size=int(input("Enter size of table:"))
table=HashTabe(size)

while True:
    print("1. Insert a record")
    print("2. Search a Record")
    print("3. Delete a Record")
    print("4. Display Table")
    print("5. Exit")
    
    choice =int(input("Enter your choice : "))
    if choice == 1:
        id =int(input("Enter student id : "))
        name=input("Enter Student Name : ")
        aRecord =StudentRecord(id, name) 
        print("")
        table.insert(aRecord)
        
    elif choice == 2:
        id=int(input("Enter a Key to be Searched : "))
        aRecord =table.Search(id)
        if aRecord is None:
            print("Key Not Found")
        else:
            print(aRecord)
            
    elif choice == 3:
        
        id=int(input("Enter a key to be deleted : "))
        table.delete(id)
    elif choice == 4:
        table.Display_Table()
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Wrong Option")
    print()
