# from curses.ascii import isdigit, islower, isupper
import email
import random
class Bank:
    
    Bank={
        "Saderat" :"60376976",
        "Refah" : "58946311",
        "Saman":"62198618"
        }

    def sabt(self,Name,Name_P,meli_code,telefon,date,rand,cvv2,bank,email):
        a = self.Bank.get(bank)
        rand = str(rand)
        sh_kart= a + rand
        Counter_C = 0
        Counter_c = 0
        Counter_N = 0
        Counter_x = 0
        g ="@gmail.com"
        for i in email:
            if i.isupper():
                Counter_C+=1
            elif i.islower():
                Counter_c+=1
            elif i.isdigit():
                Counter_N+=1
            else:
                Counter_x+=1
        if Counter_C < 1 or Counter_c < 1 or Counter_x < 1 or Counter_N < 1:
            raise Exception("Error!!")
        else:
            Email = email + g
        print(f"{Email} Sabt Shod")
      
          
        for i in meli_code:
            if len(meli_code) < 10:
                raise Exception("Error!!")
        
        print(f"{meli_code} Sabt Shod")   
        
        for i in telefon:
            if len(telefon) < 11:
                raise Exception("Error!!")
            if "0" != telefon[0] or "9" != telefon[1]:
                raise Exception("Error!!")
    
        print(f"{telefon} Sabt Shod")

        for i in date :
            if len(date) < 10 :
                raise Exception("Error!!")
            if "/" != date[2] or "/" != date[5]:
                raise Exception("Error!!")
                
        print(f"{date} Sabt Shod")
                
        with open (r"C:\Users\Arad-Pc\Desktop\Bank.txt","r") as datebank:
            List =datebank.readlines()
            if len(List)>0:
                last = List[-1].split(" ")
                if len(last)>0:
                    last_id = int(last[0])
                    ID = last_id + 1
                else:
                    ID = 1
            else:
                ID = 1

        datebank = open(r"C:\Users\Arad-Pc\Desktop\Bank.txt","a")
        datebank.write(f"{ID}  Name --> {Name} * father Name --> {Name_P} * Meli_Code --> {meli_code} * telefon --> {telefon}  * Date --> {date}  * Email --> {Email}  * Shomare Kart --> {sh_kart}  * cvv2 --> {cvv2} Sader Shod")
        datebank.close()





b1 =Bank()
Name =input("Plz enter your name:")
Name_P =input("Plz enter your father name:")
meli_code=input("Plz enter your MeliCode:")
telefon=input("Plz enter your telefon:")
date=input("Plz enter your tarikh tavalod (**/**/****):")
email=input("Plz enter your Email:")
rand =random.randint(10000000,99999999) 
cvv2=random.randint(100,10000)
bank=input("Plz enter your Bank (Saderat/Refah/Saman):")
b1.sabt(Name,Name_P,meli_code,telefon,date,rand,cvv2,bank, email)