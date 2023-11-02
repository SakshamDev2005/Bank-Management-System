import pandas as p
import functions as f
from pwinput import pwinput

def Login():
    # Takes input from employee for login

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


