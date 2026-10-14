
from os import name, remove
from re import match
from tarfile import NUL
from unittest import case


class Person:
    
    def person(self,name,phone,meliCode,tarikh):
        self.Name =name

        if len(phone) != 11 or phone[0] != "0" or phone[1] != "9": 
            raise Exception("Error!!")
        else:
            self.Phone =phone

        
        if len(meliCode) !=10 :
            raise Exception("Error!!")
        else:
            self.MeliCode = meliCode

        if tarikh[2] != "/" and tarikh[5] != "/":
            raise Exception("Error")
        else:
            self.Tarikh_Tavalod =tarikh
        


        ID = 1
        with open(r"C:\Users\Arad-Pc\Desktop\Person.txt","r") as f1:
            a =f1.readlines()
            if len(a)>0:
                b = a[-1].split()
                if len(b)>0:
                    last_id = int(b[0])
                    ID = last_id +1
                else:
                    ID = 1
            f1.close()
        with open(r"C:\Users\Arad-Pc\Desktop\Person.txt","a") as f2:
            f2.write(f"{ID} -- Name : {self.Name} -- MeliCode : {self.MeliCode} -- Tarikh Tavalod : {self.Tarikh_Tavalod} -- Phone : {self.Phone}\n")

            print(f"Moshakhasat ba id --> {ID}  -- Name : {self.Name} -- MeliCode : {self.MeliCode} -- Tarikh Tavalod : {self.Tarikh_Tavalod} -- Phone : {self.Phone} Sabt Shod")
            f2.close()




class Book:
   
    def book(self,name_book,writer,desc):
        self.Name_Book = name_book
        self.Writer = writer
        self.Desc = desc

        ID = 1
        with open(r"C:\Users\Arad-Pc\Desktop\Book.txt","r") as f1:
            a =f1.readlines()
            if len(a)>0:
                b = a[-1].split()
                if len(b)>0:
                    last_id = int(b[0])
                    ID = last_id +1
                else:
                    ID = 1
            f1.close()
        with open(r"C:\Users\Arad-Pc\Desktop\Book.txt","a") as f2:
            f2.write(f"{ID} -- Name Book :{self.Name_Book} -- Writer :{self.Writer} -- Desc :{self.Desc}\n")

            print(f"Book Ba ID : {ID} -- Name Book :{self.Name_Book} -- Writer :{self.Writer} -- Desc :{self.Desc} Dar System Sabt Shod")
            f2.close()







class Manager(Person , Book):

   #============ADD============

    def add_Book(self):
        name_book =input("Plz enter your Name Book :")
        writer =input("Plz enter your Name Writer Book :")
        desc =input("Plz enter your Desc Book :")

        self.book(name_book , writer , desc)



    def add_Person(self):

        name=input("Plz enter your Name :")
        tarikh=input("Plz enter your Tarikh Tavalod (**/**/**):")
        melicode=input("Plz enter your MeliCode :")
        phone=input("Plz enter your Phone :")

        self.person(name=name,tarikh=tarikh,meliCode=melicode,phone=phone)

   #========Search========    

    def Search_Book(self):
        target_id = int(input("Plz enter your ID :"))
        with open(r"C:\Users\Arad-Pc\Desktop\Book.txt","r") as f1:
            a =f1.readlines()
            
        for i in range(len(a)):
            line_id = int(a[i].split()[0])

            if line_id == target_id:
                # print(a[i])
                 return a[i] 

        return "Null"

    def Search_Person(self):
        target_id = int(input("Plz enter your ID :"))
        with open(r"C:\Users\Arad-Pc\Desktop\Person.txt","r") as f1:
            a =f1.readlines()
            
        for i in range(len(a)):
            line_id = int(a[i].split()[0])

            if line_id == target_id:
                # print(a[i])
                 return a[i] 

        return "Null"

    #========Remove========

    def remove_Book(self):
        target_id = int(input("Plz enter your ID :"))
        with open(r"C:\Users\Arad-Pc\Desktop\Book.txt","r") as f1:
            a =f1.readlines()
        
        found = False
        for i in range(len(a)):
            line_id = int(a[i].split()[0])

            if line_id == target_id:
                a.pop(i)
                found = True
                break

        if found == False :
            raise Exception(f"ID --> {target_id} Dar System peyda Nashod!!")


        with open(r"C:\Users\Arad-Pc\Desktop\Book.txt","w") as f2:
            print("List Updating !!!")
            f2.writelines(a)

    def remove_Person(self):
        target_id = int(input("Plz enter your ID :"))
        with open(r"C:\Users\Arad-Pc\Desktop\Person.txt","r") as f1:
            a =f1.readlines()
        
        found = False
        for i in range(len(a)):
            line_id = int(a[i].split()[0])

            if line_id == target_id:
                a.pop(i)
                found = True
                break

        if found == False :
            raise Exception(f"ID --> {target_id} Dar System peyda Nashod!!")


        with open(r"C:\Users\Arad-Pc\Desktop\Person.txt","w") as f2:
            print("List Updating !!!")
            f2.writelines(a)
        

    #============Print============     
    def Print_AllBook(self):
        with open(r"C:\Users\Arad-Pc\Desktop\Book.txt","r") as f1:
            a =f1.readlines()

        for i in range(len(a)):
            print(a[i])
        


    def Print_AllPerson(self):
        with open(r"C:\Users\Arad-Pc\Desktop\Person.txt","r") as f1:
            a =f1.readlines()
        
        for i in range(len(a)):
            print(a[i])





class Menu():
    def __init__(self):
        self.manager = Manager()
  
    def show_Menu(self):  
        while True:
            print("========> MENU <========")
            print("1.add Book")
            print("2.add Person")
            print("3.Search Book")
            print("4.Search Person")
            print("5.Remove Book")
            print("6.Remove Person")
            print("7.Print All Book")
            print("8.Print All Person")

            choice = int(input("Plz enter your Selection :"))

            if choice == 9:
                print("The End!!!")
                break

            self.processOption(choice)

    def processOption(self,ch):

            if ch == 1:
                self.manager.add_Book()
            elif ch == 2:
                self.manager.add_Person()
            elif ch == 3:
                print(self.manager.Search_Book())
            elif ch == 4:
                print(self.manager.Search_Person())
            elif ch == 5:
                self.manager.remove_Book()
            elif ch == 6:
                self.manager.remove_Person()
            elif ch == 7:
                self.manager.Print_AllBook()
            elif ch == 8:
                self.manager.Print_AllPerson()

       

#========= Main Code ==========
m1 =Menu()
(m1.show_Menu())