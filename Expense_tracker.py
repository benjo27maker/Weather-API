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

if os.path.exists('budgets.json'):
    with open('budgets.json','r') as file:
        try:
            budgets=json.load(file)
        except json.JSONDecodeError:
            budgets=[]
else:
    budgets=[]


            


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
     
     

    
       
        


     expenses.append({'Expense':expense,'Amount':f'£{amount:.2f}','ID':ID,'Date':f'{date_list}/{datetime.now().year}','Category':category})
    

     with open('expenses.json','w') as file:
            json.dump(expenses,file,indent=4)


     budget_date=[date_list[3:5],'/',str(datetime.now().year)[-2:]]
     budget_date=("".join(map(str,budget_date)))

     budget_counter=0
     remain_arr=0
     for i in budgets:
         if i.get('Date')==budget_date:
             budget_counter+=1
             remain_arr=['£', round(float(i['Remaining'][1:]) - float(amount), 2)]
             (i['Remaining'])=("".join(map(str,remain_arr)))
     if remain_arr[1]<0:
         print(f'{expense} has been added to expenses the budget of {i['Budget']} for {i["Date"]} has now been exceeded by £{abs(remain_arr[1])}')
         return
        
     print(f"{expense} has been added to expenses the remaining budget for {budget_date} is now {i['Remaining']}")
     if budget_counter==0:
         print(f'{expense} has been added to expenses there is no budget currently set for {budget_date}')



     
     


     


     with open('budgets.json','w') as file:
        json.dump(budgets,file,indent=4)
     


def del_expense(ID=None,date=None):



    if ID==None and date==None:
        print('no argument was passed please pas either ID or Date')
        return

    elif ID!=None and date!=None:
        print('too many arguments passed delete by either ID or date not both')
        return






    

    if date==None:

        if type(ID)!=int:
            print(f'{ID} is not an accepted datatype please enter an interger')
            return

        budget_date=0
        budget_amount=0
        ID_counter=0
        for i in expenses[:]:
            if i.get('ID')==ID:
                ID_counter+=1
                budget_date=i["Date"]
                budget_amount=i["Amount"][1:]
                print(f'the expense with ID:{ID} has bee deleted')
                expenses.remove(i)

                with open('expenses.json','w') as file:
                   json.dump(expenses,file,indent=4)

        
        if ID_counter==0:
            print(f'there is no expense with ID:{ID} in the expense list')
            return
        




                
        budget_date=[budget_date[3:5],'/',str(datetime.now().year)[-2:]]
        budget_date=("".join(map(str,budget_date)))


        sign=''
        if abs(budget_amount)<0:
            sign='-'
            


        for i in budgets:
            if i['Date']==budget_date:
                remain_arr=['£', round(float(i['Remaining'][1:]) + float(budget_amount), 2)]
                (i['Remaining'])=("".join(map(str,remain_arr)))

                print(f'the new remaining budget is {sign} £{remain_arr[1]}')


                with open('budgets.json','w') as file:
                    json.dump(budgets,file,indent=4)

                return

        
        


        
        
 
    
    
    if ID==None:
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
        

        
def del_category(category):

    if category=='misc':
        print('misc category cannot be deleted because it is the default category')
        return

    if category not in categories:
        print(f'{category} is not in categories please enter a valid category')
        return

    expense_counter_3=0
    for i in expenses:
        if i.get('Category')==category:
            expense_counter_3+=1
    if expense_counter_3!=0:
        print(f'{category} category cannot be deleted because there are still {expense_counter_3} expenses in {category}')
        return
    else:
        for i in categories:
            if i==category:
                categories.remove(i)
                print(f'{category} has been removied from categories list')
                break
            
        with open('categories.csv', 'w', newline='') as file:
             writer = csv.writer(file)
             writer.writerow(categories)
    
            
    
def add_category(category):


    if (category in categories):
        print(f'{category} is already a category')
        return
    
    categories.append(category)

    with open('categories.csv','w',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(categories)


def list_expenses(expense=None,category=None,date=None):


    if date!=None:
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
    

    if expense==None and category==None and date==None:
        counter=0
        for i in expenses:
            print(i['Amount'],i['Expense'],i['Category'],i['Date'],'ID =',i['ID'])
            counter+=1

        if counter==0:
            print('there are no expenses add expenses to see them here')
            return
        else:
            return

    

    if expense!=None and category==None and date==None:
        counter=0
        for i in expenses:
            if i.get('Expense')==expense:
                print(i['Amount'],i['Expense'],i['Category'],i['Date'],'ID =',i['ID'])
                counter+=1
        if counter==0:
            print(f'{expense} does not appear in expenses')
            return
        else:
            return
           

    if expense==None and category!=None and date==None:
        counter=0    
        for i in expenses:
            if i.get('Category')==category:
                print(i['Amount'],i['Expense'],i['Category'],i['Date'],'ID =',i['ID'])
                counter+=1
        if counter==0:
            print(f'there are no expenses in {category}')
            return
        else:
            return
        

        



    if expense==None and category==None and date!=None:  
        counter=0
        for i in expenses:
            if i.get('Date')==date:
                print(i['Amount'],i['Expense'],i['Category'],i['Date'],'ID =',i['ID'])
                counter+=1
        if counter==0:
            print(f'there are no expenses recorded for {date}')
            return
        else:
            return
    

    if expense==None and category!=None and date!=None:
        counter=0
        for i in expenses:
             if i.get('Date')==date and i.get('Category')==category:
                 print(i['Amount'],i['Expense'],i['Category'],i['Date'],'ID =',i['ID'])
                 counter+=1
        if counter==0:
            print(f'there are no expenses recorded for in {category} on {date}')
            return
        else:
            return
    
        


    if expense!=None and category==None and date!=None:
        counter=0
        for i in expenses:
             if i.get('Date')==date and i.get('Expense')==expense:
                 print(i['Amount'],i['Expense'],i['Category'],i['Date'],'ID =',i['ID'])
                 counter+=1
        if counter==0:
            print(f'{expenses} does not appear on expenses on {date}')
            return
        else:
            return



def list_by_ID(ID):
    try:
        int(ID)
    except ValueError:
        print(f'{ID} is not a valid ID please enter an interger number e.g {random.uniform(0,20):.0f}')
        return
    counter=0
    for i in expenses:

        if i.get('ID')==ID:
            print(i['Amount'],i['Expense'],i['Category'],i['Date'],'ID =',i['ID'])
            counter+=1
    if counter==0:
        print(f'there are no expenses with ID: {ID}')
        return
    else:
        return


def update_expense(ID,update):





    if type(ID)!=int:
        print(f'{ID} is not an accepted ID type please enter an interger e.g: {random.uniform(0,100):.0f}')
        return



    for i in expenses:
        if i.get('ID')==ID:
            old_expense=i['Expense']
            i['Expense']=update
            print(f'{old_expense} has been updated to {update}')
            with open('expenses.json','w') as file:
                json.dump(expenses,file,indent=4)
            return
    
    print(f'expense with ID: {ID} does not appear in expenses list')


def add_budget(amount,date):

    budget_date_list=str(date)


    if len(budget_date_list)==5:
        budget_date_list=budget_date_list
    elif len(budget_date_list)==4 and budget_date_list[1]=='/':
         budget_date_list=[0,budget_date_list[0],budget_date_list[1:4]]
         budget_date_list=("".join(map(str, budget_date_list)))


    try:
        check_budget_1,check_budget_2=int(budget_date_list[0:2]),int(budget_date_list[3:5])
    except ValueError:
         print(f'{date} is not a valid date give the date in the form of mm/yy')
         return
         
    
    if int(budget_date_list[0:2])>12 or int(budget_date_list[3:5])<0 or int(budget_date_list[0:2])<0:
         print(f'{date} is not a valid date give the date in the form of mm/yy')
         return
    
    for i in budgets:
        if i.get('Date')==budget_date_list:
            print(f'there is already a budget of {i['Budget']} set for {budget_date_list} to set a new budget update or delete the current budget')
            return


    

    try:
        int(amount)
    except ValueError:
        print(f'{amount} is not a valid budget please enter an amount in ponds eg: £{random.uniform(0,100):.2f}')
        return
    amount=f'£{amount}'

    if int(amount[1:])<0:
        print(f'please enter a positive budget eg: £{random.uniform(0,100):.2f}')
        return



    


    budgets.append({'Date':budget_date_list,'Budget':amount,'Remaining':amount})
    with open('budgets.json','w') as file:
        json.dump(budgets,file,indent=4)

    print(f'a budget of {amount} has been added for {budget_date_list}')

def del_budget(date):


    budget_date_list=str(date)


    if len(budget_date_list)==5:
        budget_date_list=budget_date_list
    elif len(budget_date_list)==4 and budget_date_list[1]=='/':
         budget_date_list=[0,budget_date_list[0],budget_date_list[1:4]]
         budget_date_list=("".join(map(str, budget_date_list)))


    try:
        check_budget_1,check_budget_2=int(budget_date_list[0:2]),int(budget_date_list[3:5])
    except ValueError:
         print(f'{date} is not a valid date give the date in the form of mm/yy')
         return
         
    
    if int(budget_date_list[0:2])>12 or int(budget_date_list[3:5])<0 or int(budget_date_list[0:2])<0:
         print(f'{date} is not a valid date give the date in the form of mm/yy')
         return
    
    for i in budgets:
        if i.get('Date')==budget_date_list:
            budgets.remove(i)
            with open('budgets.json','w') as file:
                json.dump(budgets,file,indent=4)
            
            print(f'budget for {budget_date_list} has been deleted')
            return
        
    print(f'there is no budget currently set for {budget_date_list}')

def update_budget(update,date):



    if len(budgets)==0:
        print('there are no budgets currently in place add a budget first to update it')
        return



    budget_date_list=str(date)


    if len(budget_date_list)==5:
        budget_date_list=budget_date_list
    elif len(budget_date_list)==4 and budget_date_list[1]=='/':
         budget_date_list=[0,budget_date_list[0],budget_date_list[1:4]]
         budget_date_list=("".join(map(str, budget_date_list)))


    try:
        check_budget_1,check_budget_2=int(budget_date_list[0:2]),int(budget_date_list[3:5])
    except ValueError:
         print(f'{date} is not a valid date give the date in the form of mm/yy')
         return
         
    
    if int(budget_date_list[0:2])>12 or int(budget_date_list[3:5])<0 or int(budget_date_list[0:2])<0:
         print(f'{date} is not a valid date give the date in the form of mm/yy')
         return
    

    try:
        int(update)
    except ValueError:
        print(f'{update} is not a valid budget please enter an amount in ponds eg: £{random.uniform(0,100):.2f}')
        return
    update=f'£{update}'

    if int(update[1:])<0:
        print(f'please enter a positive budget eg: £{random.uniform(0,100):.2f}')
        return
    
    
    for i in budgets:
        if i.get('Date')==budget_date_list:
            if i['Budget']==update:
                print(f'the budget for {budget_date_list} ia already {update}')
                return
            i['Budget']=update

            with open('budgets.json','w') as file:
                json.dump(budgets,file,indent=4)
            print(f'the budget for {budget_date_list} has been updated to {update}')
            return

    print(f'there is no budget currently set for {budget_date_list}')
    return


add_expense('goop',25,None,'04/11')