import sys
import os
import json
from datetime import datetime
import random


if os.path.exists('expenses.json'):
    with open('expenses.json','r') as file:
        try:
            expenses=json.load(file)
        except json.JSONDecodeError:
                expenses=[]
else:
    expenses=[]

def add_expense(expense,amount,category=None,date=None):
     
     try:
         float(amount)
     except ValueError:
         print(f'{amount} is not a valid datatype please enter a positive number with no spaces eg: e.g. £{random.uniform(0, 100):.2f}')
         return
     
     if float(amount)<0:
         print('please enter a positive number')
         return
     
     ID=len(expenses)+1
     date_list=str(date)


     if category==None:
         category='misc'
     
     
     if len(date_list)==5:
         date_list=date_list
     elif len(date_list)==4 and date_list[2]=='/':
         date_list=[date_list[0:3],0,date_list[3]]
         date_list=("".join(map(str, date_list)))
     elif len(date_list)==4 and date_list[1]=='/':
         date_list=[0,date_list[0],date_list[1:4]]
         date_list=("".join(map(str, date_list)))
     elif len(date_list)==3:
         date_list=[0,date_list[0],date_list[1],0,date_list[2]]
         date_list=("".join(map(str, date_list)))
    
     try:
        check1,check2=int(date_list[0:2]),int(date_list[3:5])
     except ValueError:
         print(f'{date} is not a valid date give the date in the form of dd/mm')
         return
         
    
     if int(date_list[0:2])>31 or int(date_list[3:5])>12 or int(date_list[3:5])<0 or int(date_list[0:2])<0:
         print(f'{date} is not a valid date give the date in the form of dd/mm')
         return
     
     

     if date!=None:
       
        


        expenses.append({'expense':expense,'amount':f'\£{amount}','ID':ID,'Date':f'{date_list}/{datetime.now().year}','Category':category})
    
     else:

         expenses.append({'expense':expense,'amount':f'\£{amount}','ID':ID,'Date':datetime.now().strftime('%d/%m/%Y'),'Category':category})


    


     with open('expenses.json','w') as file:
        json.dump(expenses,file,indent=4)
     


def del_expense(ID):

    if type(ID)!=int:
        print(f'{ID} is not an accepted datatype please enter an interger')
    for i in expenses:
        if i('ID')==ID:
            expenses.remove(i)

            with open('expenses.json','w') as file:
                json.dump(expenses,file,indent=4)
                return
    print(f'an expense with ID:{ID} is not in the expense list')
    return
        
            
    
        
  
