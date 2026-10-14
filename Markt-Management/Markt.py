import json
class Markt:
    def Mahsool(self,name,price,mojoodi):
        self.Name=name
        
        if price <= 0 :
            raise Exception("Error!!")
        else:
            self.Price=price

        if mojoodi <= 0:
            raise Exception("Error!!")
        else:    
            self.Mojoodi = mojoodi
            
        
        ID = 1
        with open(r"C:\Users\Arad-Pc\Desktop\Markt.txt","r") as f1:
            a = f1.readlines()
            if len(a) >0:
                b = a[-1].split()
                if len(b)>0:
                    last_id = int(b[0]) 
                    ID = last_id +1           
                else:
                    ID =1
            f1.close()
            
        with open(r"C:\Users\Arad-Pc\Desktop\Markt.txt","a") as f2 :
            f2.write(f"{ID} --> {self.Name} --> {self.Mojoodi} --> {self.Price}\n")     
            
            print(f"Mahsool {self.Name} Ba ID {ID} Va Price {self.Price} -- {self.Mojoodi} TA Sharzh Shod")        
             
            f2.close() 
            

class Costomer:
    def costomer(self,phone,kif):
        if len(phone) != 11 or phone[0] != "0" or phone[1] != "9": 
            raise Exception("Error!!")
        else:
            self.Phone =phone
            
        if kif <= 10000:
            raise Exception("Go Out!!!")
        else:
          self.Kif = kif
        
        ID = 1
        with open(r"C:\Users\Arad-Pc\Desktop\Costomer.txt","r") as f1 :
             a = f1.readlines()
             if len(a) >0:
                b = a[-1].split()
                if len(b)>0:
                    last_id = int(b[0]) 
                    ID = last_id +1           
                else:
                    ID =1
             f1.close()
        
        with open(r"C:\Users\Arad-Pc\Desktop\Costomer.txt","a") as f2 :
            f2.write(f"{ID} --> {self.Phone} --> {self.Kif}\n")     
            
            
            print(f"Costomer Ba Phone {self.Phone} Va ID {ID} Va Kif Pool {self.Kif} Vared Markt Shod")        
             
            f2.close()   
class Manager(Markt,Costomer):
    
    #=======ADD=======
    def add_Mahsool(self):
        name = input("Plz enter your Name KALA :")
        price = int(input("Plz enter your Price KALA :"))
        mojoodi = int(input("Plz enter your Mojoodi KALA :"))
        
        self.Mahsool(name,price,mojoodi)
        
    def add_Costomer(self):
        phone = input("Plz enter your Phone :")     
        kif = int(input("Plz enter your Mojoodi :"))     
        
        self.costomer(phone,kif)
    
    #========Search========
    def Search_Mahsool(self):
        target_id = int(input("Plz enter your ID :"))
        print("1.Chips \n 2.Bastani \n 3.Energy Drink")
        
        with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","r") as f1:
            a = f1.readlines()
        
        for i in range (len(a)):
            line_id = int(a[i].split()[0])
            
            if line_id == target_id :
                return a[i]
        return "Null"
            

    def Search_Costomer(self):
        target_id = int(input("Plz enter your ID :"))
        with open (r"C:\Users\Arad-Pc\Desktop\Costomer.txt","r") as f1:
            a = f1.readlines()
        
        for i in range (len(a)):
            line_id = int(a[i].split()[0])
            
            if line_id == target_id :
                return a[i]
        return "Null"
    
    #========Remove========
    def Remove_Mahsool(self):
        target_id = int(input("Plz enter your ID :"))
        
        print("1.Chips \n 2.Bastani \n 3.Energy Drink")
        
        with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","r") as f1:
            a = f1.readlines()
        found = False  
        for i in range(len(a)):
            line_id = int(a[i].split()[0])
            if line_id == target_id:
                a.pop(i)
                found = True    
                break
        if found == False :
            raise Exception(f"ID --> {target_id} Dar System peyda Nashod!!")
        with open(r"C:\Users\Arad-Pc\Desktop\Markt.txt","w") as f2:
            print("List Updating !!!")
            f2.writelines(a)
                  
                    
    def Remove_Costomer(self):
        target_id = int(input("Plz enter your ID :"))
         
        with open (r"C:\Users\Arad-Pc\Desktop\Costomer.txt","r") as f1:
            a = f1.readlines()
        found = False  
        for i in range(len(a)):
            line_id = int(a[i].split()[0])
            if line_id == target_id:
                a.pop(i)
                found = True    
                break
        if found == False :
            raise Exception(f"ID --> {target_id} Dar System peyda Nashod!!")
          
        with open(r"C:\Users\Arad-Pc\Desktop\Costomer.txt","w") as f2:
            print("List Updating !!!")
            f2.writelines(a)
                  
    #========Print All========
    def Print_AllMahsool(self):
        with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","r") as f1:
            a = f1.readlines()
            
        for i in range (len(a)):
            print(a[i])    
        
    def print_AllCostomer(self):
        with open (r"C:\Users\Arad-Pc\Desktop\Costomer.txt","r") as f1:
            a = f1.readlines()
        for i in range(len(a)):
            print(a[i])

    #========Afzayesh & Kahesh========
    def Afzayesh_Mahsool(self):
        print("1.Chips \n 2.Bastani \n 3.Energy Drink")

        target_id = int(input("Plz enter your ID :"))


        Afzayesh = int(input("Enter Meghdar Afzayesh KALA :"))

        with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","r") as f1:
            a = f1.readlines()
        found = False    
        for i in range (len(a)):
            parts = a[i].strip().split(" --> ")
            if len(parts) > 0 :
                line_id = int(parts[0])
                if line_id == target_id:
                    current_mojoodi = int(parts[2])
                    new_Mojoodi = current_mojoodi+Afzayesh
                    new_line= f"{parts[0]} --> {parts[1]} --> {new_Mojoodi} --> {parts[3]}\n"
                    a[i] = new_line
                    found = True
                    break
        if found == False:
            raise Exception(f"ID --> {target_id} Dar System peyda Nashod!!")
        
        with open (r"C:\Users\Arad-PC\Desktop\Markt.txt","w") as f2:      
             f2.writelines(a)
             print("List Updating !!!")


    def Kahesh_Mahsool(self):
          print("1.Chips \n 2.Bastani \n 3.Energy Drink")

          target_id = int(input("Plz enter your ID :"))


          Kahesh = int(input("Enter Meghdar Kahesh KALA :"))

          with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","r") as f1:
            a = f1.readlines()
          found = False    
          for i in range (len(a)):
                parts = a[i].strip().split(' --> ')
                if len(parts) > 0 :
                    line_id = int(parts[0])
                    if line_id == target_id:
                        current_mojoodi = int(parts[2])
                        new_Mojoodi = current_mojoodi - Kahesh
                        new_line= f"{parts[0]} --> {parts[1]} --> {new_Mojoodi} --> {parts[3]}\n"
                        a[i] = new_line
                        found = True
                        break
          if found == False:
                 raise Exception(f"ID --> {target_id} Dar System peyda Nashod!!")
        
          with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","w") as f2:      
                 f2.writelines(a)
                 print("List Updating !!!")


    #========Select========

    def Select(self):
          print("1.Chips \n 2.Bastani \n 3.Energy Drink")
          target_id = int(input("Plz enter your Select MAhsool ID :"))
          target_id1 = int(input("Plz enter your Costomer ID :"))

          Select_Kala = int(input("Enter Meghdar Select KALA :"))

          with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","r") as f1:
             a = f1.readlines()
          
          with open (r"C:\Users\Arad-Pc\Desktop\Costomer.txt","r") as f1:
             b = f1.readlines()

          product_price = 0

          found = False    
          for i in range (len(a)):
                parts = a[i].strip().split(' --> ')
                if len(parts) > 0 :
                    line_id = int(parts[0])
                    if line_id == target_id:
                        current_mojoodi = int(parts[2])

                        if current_mojoodi < Select_Kala :
                            raise Exception(f"Mojoodi Mahsool Kafi Nist! Mojoodi Feli:{current_mojoodi}")

                        new_Mojoodi = current_mojoodi - Select_Kala

                        product_price = int(parts[3])

                        new_line= f"{parts[0]} --> {parts[1]} --> {new_Mojoodi} --> {parts[3]}\n"
                        a[i] = new_line
                        found = True
                        break
          if found == False:
                 raise Exception(f"ID --> {target_id} Dar System peyda Nashod!!")
        

          total_cost = product_price * Select_Kala
 
          found = False    
          for i in range (len(b)):
                parts = b[i].split(' --> ')
                if len(parts) > 0 :
                    line_id = int(parts[0])
                    if line_id == target_id1:
                        current_kif = int(parts[2])

                        if current_kif < total_cost:
                            raise Exception(f"Mojoodi kif kafi nist! Hazine:{total_cost} , Mojoodi Kif :{current_kif}")

                        new_kif = current_kif - total_cost
                        new_line= f"{parts[0]} --> {parts[1]} --> {new_kif}\n"
                        b[i] = new_line
                        found = True
                        break
          if found == False:
                 raise Exception(f"Costomer ID --> {target_id} Dar System peyda Nashod!!")          
          
          with open (r"C:\Users\Arad-Pc\Desktop\Markt.txt","w") as f2:      
                 f2.writelines(a)
                 print("List Updating !!!")



          with open (r"C:\Users\Arad-Pc\Desktop\Costomer.txt","w") as f2:      
                 f2.writelines(b)
                 print("List Updating !!!")

          print(f"Select Ba Movafaghiat Anjam Shod! Hazine: {total_cost} az kif kam shod")


class Menu():
    def __init__(self):
        self.manager = Manager()
  
    def show_Menu(self):  
        while True:
            print("---------- MENU ----------")
            print("1.add Mahsool")
            print("2.add Costomer")
            print("3.Search Mahsool")
            print("4.Search Costomer")
            print("5.Remove Mahsool")
            print("6.Remove Costomer")
            print("7.Print All Mahsool")
            print("8.Print All Costomer")
            print("9.Afyazesh Mahsool")
            print("10.Kahesh Mahsool")
            print("11.Select Mahsool")
            print("12.EXIT")


            choice = int(input("Plz enter your Selection :"))

            if choice == 12:
                print("The End!!!")
                break

            self.processOption(choice)

    def processOption(self,ch):

            if ch == 1:
                self.manager.add_Mahsool()
            elif ch == 2:
                self.manager.add_Costomer()
            elif ch == 3:
                print(self.manager.Search_Mahsool())
            elif ch == 4:
                print(self.manager.Search_Costomer())
            elif ch == 5:
                self.manager.Remove_Mahsool()
            elif ch == 6:
                self.manager.Remove_Costomer()
            elif ch == 7:
                self.manager.Print_AllMahsool()
            elif ch == 8:
                self.manager.print_AllCostomer()
            elif ch == 9:
                self.manager.Afzayesh_Mahsool()
            elif ch == 10:
                self.manager.Kahesh_Mahsool()
            elif ch == 11:
                self.manager.Select()       

#========= Main Code ==========
m1 =Menu()
(m1.show_Menu())




