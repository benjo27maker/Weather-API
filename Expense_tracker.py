import sys
import os
import json
from datetime import datetime
import random
import csv 


if os.path.exists('expenses.json'):
    with open('expenses.json','r') as file:
        try:
            expenses=json.load(file)
        except json.JSONDecodeError:
                expenses=[]
else:
    expenses=[]
categories=[]

if os.path.exists('categories.csv'):
    with open('categories.csv','r') as file:
        reader=csv.reader(file)
        try:
            for i in reader:
                categories.extend(i)
        except FileNotFoundError:
            categories=['misc']
else:
    categories=['misc']


            


def add_expense(expense,amount,category=None,date=None):
     
     if category==None:
         category='misc'
     
     if (category not in categories):
         print(f'{category} is not a category to add it as a category use command add category {'category'}')
         return
     
     try:
         float(amount)
     except ValueError:
         print(f'{amount} is not a valid datatype please enter a positive number with no spaces eg: e.g. £{random.uniform(0, 100):.2f}')
         return
     
     if float(amount)<0:
         print('please enter a positive number')
         return
     
     if date==None:
         date=datetime.now().strftime('%d/%m')
         


     ID=len(expenses)+1
     date_list=str(date)

     
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
     
     

    
       
        


     expenses.append({'Expense':expense,'Amount':f'\£{amount:.2f}','ID':ID,'Date':f'{date_list}/{datetime.now().year}','Category':category})
    

    


     with open('expenses.json','w') as file:
        json.dump(expenses,file,indent=4)
     


def del_expense(ID=None,category=None,date=None):



    if ID==None and category==None and date==None:
        print('no argumnt was passed please pas either ID, category or Date')
        return


    if ID!=None and category!=None:
        print('too many arguments passed delete by either ID or category not both')
        return
    elif ID!=None and date!=None:
        print('too many arguments passed delete by either ID or date not both')
        return
    elif category!=None and date!=None:
        print('too many arguments passed delete by either category or date not both')
        return






    

    if category==None and date==None:

        if type(ID)!=int:
            print(f'{ID} is not an accepted datatype please enter an interger')
            return

        for i in expenses[:]:
            if i.get('ID')==ID:
              expenses.remove(i)

              with open('expenses.json','w') as file:
                   json.dump(expenses,file,indent=4)
              return
        print(f'an expense with ID:{ID} is not in the expense list')
        return
    
    if ID==None and date==None:

        if (category not in categories):
            print(f'{category} is not a category')
            return
        
        expense_counter_1=0
        for i in expenses[:]:
            if i.get('Category')==category:
                expenses.remove(i)
                expense_counter_1+=1
        if expense_counter_1!=0:
            with open('expenses.json','w') as file:
                json.dump(expenses,file,indent=4)
            return
        else:
            print(f'there are no expenses currently in {category}')
    
    if ID==None and category==None:
        date_list=str(date)

        
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
        
        expense_counter_2=0
        for i in expenses[:]:
            if i.get('Date')==date:
                expense_counter_2+=1
                expenses.remove(i)

        if expense_counter_2!=0:
            with open('expenses.json','w') as file:
                json.dump(expenses,file,indent=4)
            return
        else:
            print(f'there are no expenses recorded on {date}')
            return
            

def del_all():
    for i in expenses[:]:
        expenses.remove(i)
    
    with open('expenses.json','w') as file:
        json.dump(expenses,file,indent=4)


    print('all expenses have been deleted')


    return
        



        
        
            


            



        
    

        
            
    
def add_category(category):
    if (category in categories):
        print(f'{category} is already a category')
        return
    
    categories.append(category)

    with open('categories.csv','w',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(categories)

