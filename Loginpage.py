import pandas as p
import functions as f
from pwinput import pwinput

def Login():
    # Takes input from employee

    df = p.read_csv('Files/employees.csv')

    print('\n')
    print("<----- Employee's Login Page ----->")
    ch=input('Want to hide password (Y/N) ->')
    if ch.upper() in ['YES','Y']:
        Username = input('Enter the Username ->')
        Password = pwinput('Enter the Password ->','*')
    elif ch.upper() in ['N','NO']:
        Username = input('Enter the Username ->')
        Password = input("Enter your password ->")
    else:
        print('Invalid Input, Try Again')
        Login()
    
    if df[(df["Username"] == Username) & (df["Password"] == Password)].empty:
        print("Error, Try Again")
        Login()
    else:
        f.Func()
    

def Create():
    #creates an account if employee doesn't have

    df = p.read_csv('Files/employees.csv')
    i = len(df.index)
    print('\n')
    print("<----- Creates Employee's Account ----->")
    User = input('Enter the Username ->')  
    if (df.loc[:,"Username"]==User).any():
        print('Try For Another Username')
        Create()
    else:
        Pass = input('Enter the Password ->')
        df.loc[i,"Username"]=User
        df.loc[i,"Password"]=Pass
        df.to_csv('Files/employees.csv', index=False)
        print('Data Entered Successfully')
        print('\n')
        c=input('Do you want to Login or not ? -> ').upper()
        if c in ['YES','Y']:
            Login()
        else:
            exit()

def Update():
    #update useranme or password of employee

    df = p.read_csv('Files/employees.csv')

    print('\n')
    print("<----- Updates Employee's Details ----->")
    Username = input('Enter the Username ->')
    Password = input('Enter the Password ->')
        
    if df[(df["Username"] == Username) & (df["Password"] == Password)].empty:
        print('Error, Try Again')
        Update()  
    else:
        print('1 - Username \n2 - Password')
        ch = int(input('What you want to update ->'))
        c = df[(df["Username"] == Username) & (df["Password"] == Password)].index.values

        if ch==1:
            User = input('Enter the Username ->')
            df.at[c[0],"Username"]=User
            print('Username Updated')
            df.to_csv('Files/employees.csv',index=False)
            l= input('Do you want to login or not ->').upper()
            if l in ['YES','Y']:
                Login()
            else:
                exit()
        elif ch==2:
            Pass = input('Enter the Password ->')
            df.at[c[0],"Password"]=Pass
            print('Password Updated')
            df.to_csv('Files/employees.csv',index=False)
            
            l= input('Do you want to login or not ->').upper()
            if l in ['YES','Y']:
                Login()
            else:
                exit()    
        else:
            print('Error, Try Again')

def Delete():
    #delete account of employee
    print('\n')
    df = p.read_csv('Files/employees.csv')

    print("<----- Deletes Employee's Account ----->")
    Username = input('Enter the Username ->')
    Password = input('Enter the Password ->')
    if df[(df["Username"] == Username) & (df["Password"] == Password)].empty:
        print("Error, Try Again")
        Delete()
    else:
        c = df[(df["Username"] == Username) & (df["Password"] == Password)].index.values
        print(df.loc[c[0],:])
        df.drop(c,inplace=True)
        df.to_csv('Files/employees.csv',index=False)
        print('\nThe Account is Closed')
        print('\nTable Updated - ')
        print(df)

def AddOns():
    #manipulate data of some csv files
    print('\n')
    accounts = p.read_csv('Files/Accounts.csv')
    i1 = len(accounts)

    print("<----- Making Changes in Files ----->")

    entry1 = input('Enter the Account Name ->')
    entry2 = input('Enter the Symbols ->')

    li = [entry1,entry2]
    accounts.loc[i1,:] = li
    accounts.to_csv('Files/Accounts.csv',index=False)
    print('Entry is inserted in the File')


