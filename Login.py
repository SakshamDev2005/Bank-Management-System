import pandas as p
import Bank as bk
from pwinput import pwinput
import sys,time,os
from colorama import Fore
import time as ti

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
        Password = input("Enter your Password ->")

    else:
        print('Invalid Input, Try Again')
        Login()


    if df[(df["Username"] == Username) & (df["Password"] == Password)].empty:
        print("Error, Try Again")
        Login()
    else:
        bk.Func()
    

def Update():
    #update useranme or password of employee

    df = p.read_csv('Files/employees.csv')

    print('\n')
    print("<----- Updates Employee's Details ----->")
    ch=input('Want to hide password (Y/N) ->')

    if ch.upper() in ['YES','Y']:
        Username = input('Enter the Username ->')
        Password = pwinput('Enter the Password ->','*')

    elif ch.upper() in ['N','NO']:
        Username = input('Enter the Username ->')
        Password = input("Enter your Password ->")

    else:
        print('Invalid Input, Try Again')
        Update()
        

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




#Starting Page

v = '\t \t========================================================\n\
\t \t \t \t \t SBI BANK \n\
\t \t \t========================================'


for i in v:
        time.sleep(0.05)
        sys.stdout.write(Fore.CYAN+i)
        sys.stdout.flush()
      

print('\n')


line = '1 - Login Account\n\
2 - Update Details\n\
3 - Exit System'      


while True:
        print('\n')

        for i in line:
                time.sleep(0.10)
                sys.stdout.write(Fore.GREEN+i)
                sys.stdout.flush()

        #print(line)
        print('\n')

        choice=int(input('Enter the choice ->'))
        if choice==1:
                Login()
                break
        elif choice==2:
                Update()
                break
        elif choice==3:
                ti.sleep(.8)
                exit()
        else:
                print('Error, Try Again \n')
                continue