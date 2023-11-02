import Loginpage as l
import sys,time,os
from colorama import Fore
import time as ti

#Starting Page
'''
v = '\t \t========================================================\n\
\t \t \t \t \t SBI BANK \n\
\t \t \t========================================'


for i in v:
        time.sleep(0.05)
        sys.stdout.write(Fore.CYAN+i)
        sys.stdout.flush()
      

print('\n')
'''

line = '1 - Login Account\n\
2 - Update Account\n\
3 - Exit System'        
while True:
        print('\n')
        '''
        for i in line:
                time.sleep(0.10)
                sys.stdout.write(Fore.GREEN+i)
                sys.stdout.flush()'''
        print(line)
        print('\n')

        choice=int(input('Enter the choice ->'))
        if choice==1:
                l.Login()
                break
        elif choice==2:
                l.Update()
                break
        elif choice==3:
                ti.sleep(.8)
                exit()
        else:
                print('Error, Try Again \n')
                continue
