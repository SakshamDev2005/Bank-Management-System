import pandas as pd
from datetime import date as d, datetime as dt
import time
from matplotlib import pyplot as plt
import seaborn as sns

# Global Variables
today = d.today()
open_date = today.strftime("%Y/%m/%d")

cus, accbook, trans, transfer = None, None, None, None
i2, i3, i4, i5 = None, None, None, None

def Files():
    global cus, accbook, trans, transfer, accounts, i2, i3, i4, i5
    # Tables access
    cus = pd.read_csv('Files/Customers/Customers.csv')
    accbook = pd.read_csv('Files/Customers/Acc.csv')
    trans = pd.read_csv('Files/Customers/Transaction.csv')
    transfer = pd.read_csv('Files/Customers/Transfer.csv')
    accounts = pd.read_csv('Files/Accounts.csv')

    # Index of tables
    i2, i3, i4, i5 = len(cus.index), len(accbook.index), len(trans.index), len(transfer.index)

# Calculate Age
def calculateAge(birthDate):
    today = d.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

# Send data to CSV files
def to_csv():
    global cus, accbook, trans, transfer
    
    cus.to_csv('Files/Customers/Customers.csv', index=False)
    accbook.to_csv('Files/Customers/Acc.csv', index=False)
    trans.to_csv('Files/Customers/Transaction.csv', index=False)
    transfer.to_csv('Files/Customers/Transfer.csv', index=False)

# Validates Customer ID
def validate_id(cust_id):
        if (cust_id[:2] == accounts['Symbols']).bool and len(cust_id) == 6 and cust_id[2:].isdigit():
            return True
        else:
            return False
        
#Validates the inputs of Open Acc function        
def validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp):
    global cus, accbook, trans, transfer
    Files()

    cur_bal = open_bal
    acc_type = None
    v1 = accounts[accounts['Symbols'] == cust_id[:2]].index.values
    
    acc_type = accounts.at[v1[0],'Accounts']

    if phone.isdigit():
        if len(phone) == 10:
            pass
        else:
            print('Enter a valid phone number')
            phone = input('Enter the Phone Number ->')
            validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
    else:
        print('Enter a valid Phone Number')
        phone = input('Enter the Phone Number ->')
        validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
        
    if pan_no.isalnum():
        if len(pan_no) == 10:
            if (cus['PAN_No'] == float(pan_no)).any():
                print('The PAN Number is not available, Try Again')
                pan_no = input('Enter the PAN Number ->')
                validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
            else:
                pass
        else:
            print('Enter a valid PAN Number')
            pan_no = input('Enter the PAN No ->')
            validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
    else:
        print('Enter a valid PAN Number')
        pan_no = input('Enter the PAN No ->')
        validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
        
    if acc_no.isdigit():
        if len(acc_no) == 10:
            if  (cus['Acc_No'] == float(acc_no)).any():
                print('The account number is not available, Try again')
                acc_no = input('Enter the Account Number ->')
                validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no)
            else:
                pass
        else:
            print('Enter a valid account number')
            acc_no = input('Enter the Account Number ->')
            validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
    else:
        print('Enter a valid Account Number')
        acc_no = input('Enter the Account Number ->')
        validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)

    if sex.upper() not in ['MALE','FEMALE','OTHERS','OTHER']:
        print('Invalid attempt, Try again')
        sex = input('Enter the Gender (Male/Female/Other(s)) ->')
        validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
    else:
        if sex.upper() == 'MALE':
            sex = 'Male'
        elif sex.upper() in ['OTHER','OTHERS']:
            sex = 'Other'
        else:
            sex = 'Female'
            
    subject = 'Adult'
    try:
        date_format = '%Y/%m/%d'
        dob_obj = dt.strptime(dobp, date_format)

        dob = dobp.split('/')
        age = calculateAge(d(int(dob[0]), int(dob[1]), int(dob[2])))
        if age <=0:
            print('You should have age of at least 1.')
            dobp = input('Enter the DOB (YYYY/MM/DD) ->')
            validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
        else:
            pass
            
        subject = 'Adult'
        if age < 18:
            print('You are considered Minor because your age is less than 17. ')
            subject = 'Minor'
        else:
            pass
    except ValueError:
        print('Date Format is Invalid, Try Again')
        dobp = input('Enter the DOB (YYYY/MM/DD) ->')
        validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
        
    lst = [cust_id, cust_name, phone, pan_no, acc_no, age, sex, dobp, subject]
    lis = [cust_id, acc_no, acc_type, open_date, open_bal, cur_bal]
    li = [cust_id, open_date, 'Primary Deposit', open_bal]

    cus.loc[i2,:] = lst
    accbook.loc[i3,:] = lis
    trans.loc[i4,:] = li

    to_csv()
    print(f'The Account {cust_id} in now opened with primary deposit of ₹{cur_bal}.')
    Func()

#Open the Account for new Customer
def OpenAcc():
    global cus,accounts
    Files()

    print('\n')
    print('<----- Creation of New Account ----->')
    cust_id = input('Enter the Customer Id ->')
    if validate_id(cust_id):
        if (cus['Cust_Id'] == cust_id).any():
            print('Id is not available')
            OpenAcc()
        else:
            cust_name = input('Enter the Customer Name ->')
            open_bal = float(input('Enter Opening Balance ->'))
    else:
        print('Enter the valid Id')
        OpenAcc()
        
    phone = input('Enter the Phone no ->')
    sex = input('Enter the Gender (Male/Female/Other) ->')
    pan_no = input('Enter the PAN Number ->')
    acc_no = input('Enter the Account No ->')
    dobp = input('Enter the DOB (YYYY/MM/DD) ->')
    validOpenAcc(cust_id,cust_name,open_bal,phone,sex,pan_no,acc_no,dobp)
    
# Deposition of Amount by the Customer
def Deposit():
    global cus,accbook,transaction
    Files()
    
    print('\n')
    print('<----- Deposit of Amount ----->')
    cust_id = input('Enter the Customer Id ->')
    if validate_id(cust_id):
        if (accbook.loc[:, "Cust_Id"] == cust_id).any():
            depo_am = int(input('Enter the Amount ->'))
            v = accbook[(accbook["Cust_Id"] == cust_id)].index.values
            li = [cust_id, open_date, 'Extra Deposits', depo_am]
            trans.loc[i4,:] = li
            accbook.at[v[0], 'Current_Balance'] += depo_am

            to_csv()
            numstr = str(depo_am)
            print(f'The Amount deposited is ₹{numstr}.')
            Func()
        else:
            print('Id is not available')
            Deposit()
    else:
        print('Enter the valid Id')
        Deposit()

#Validates the inputs of Withdraw function
def validWithdraw(cust_id):
    global cus,accbook,transaction
    Files()

    if (accbook.loc[:, "Cust_Id"] == cust_id).any():
        v = accbook[(accbook["Cust_Id"] == cust_id)].index.values
        withdraw_am = float(input('Enter the Amount ->'))
        if withdraw_am > accbook.at[v[0], 'Current_Balance']:
            print('Insufficient balance')
            validWithdraw(cust_id)
        else:
            li = [cust_id, open_date, 'Withdrawl', withdraw_am]
            trans.loc[i4, :] = li
            accbook.at[v[0], 'Current_Balance'] -= withdraw_am

            to_csv()
            numstr = str(withdraw_am)
            print(f'The Amount Withdrawn is ₹{numstr}.')
            Func()
    else:
        print('Id is not available')
        Withdraw()

# Withdrawl of Amount by the Customer
def Withdraw():
    global cus,accbook,transaction
    Files()

    print('\n')
    print('<----- Withdraw of Amount ----->')
    cust_id = input('Enter the Customer Id ->')
    if validate_id(cust_id):
        validWithdraw(cust_id)
    else:
        print('Enter the valid Id')
        Withdraw()

#Validates the inputs of Tranfer function
def validTransfer(cust_id,acc_no,pay_mode,bank,ifsc):
    global cus,accbook,transaction,transfer
    Files()

    if cus.loc[:, "Cust_Id"].eq(cust_id).any():
        if not acc_no.isdigit():
            print('Enter the valid account number')
            acc_no = input('Enter the Account no ->')
            validTransfer(cust_id,acc_no,pay_mode,bank,ifsc)   
        else:
            if ifsc.isalnum() and len(ifsc) == 11:
                v = accbook[accbook["Cust_Id"] == cust_id].index.values
                trans_amount = float(input('Enter the Amount ->'))
                if trans_amount > accbook.at[v[0], 'Current_Balance']:
                    print('Insufficient balance')
                    validTransfer(cust_id,acc_no,pay_mode,bank,ifsc)
                else:
                    print(f'The Amount of ₹{trans_amount} is transferred to {bank} bank account.')

                    accbook.at[v[0], 'Current_Balance'] -= trans_amount
                    lis = [cust_id, bank, ifsc, acc_no, pay_mode, trans_amount]
                    li = [cust_id, open_date, 'Transfer', trans_amount]
                    trans.loc[i4, :] = li
                    transfer.loc[i5, :] = lis
                        
                    to_csv()
                    Func()    
            else:
                print('Enter the valid IFSC code')
                ifsc = input('Enter the IFSC Code ->')
                validTransfer(cust_id,acc_no,pay_mode,bank,ifsc)            
    else:
        print('Customer Id is not available')
        Transfer()        

# Transfer the Amount to the other Account
def Transfer():
    global cus,accbook,transaction,transfer
    Files()

    print('\n')
    print('<----- Transfer of Amount ----->')
    cust_id = input('Enter the Customer Id ->')
    if validate_id(cust_id):
        acc_no = input('Enter the Account Number ->')
        pay_mode = input('Enter the mode of payment ->').upper()
        bank = input('Enter the Bank Name ->')
        ifsc = input('Enter the IFSC Code ->')
        validTransfer(cust_id,acc_no,pay_mode,bank,ifsc)
    else:
        print('Enter the valid Id')
        Transfer()

# Check Account Details of the Customer       
def See_Acc(): 
    global accbook,accounts
    Files()

    print('\n')
    print('<----- Account Details Enquiry ----->')
    cust_id = input('Enter the Customer Id ->')

    if not validate_id(cust_id):
        print('Enter the valid Id')
        See_Acc()
    else:
        if (accbook.loc[:, "Cust_Id"] == cust_id).any():
            v = accbook[accbook["Cust_Id"] == cust_id].index.values
            print('\n')
            print(accbook.loc[v[0], :])
            Func()
        else:
            print("Id is not available")
            See_Acc()

# Check Customer Details of the Customer
def Cus_Det():
    global cus,accounts
    Files()

    print('\n')
    print('<----- Customer Details Enquiry ----->')
    cust_id = input('Enter the Customer Id ->')

    if not validate_id(cust_id):
        print('Enter the valid Id')
        Cus_Det()
    else:
        if (cus.loc[:, "Cust_Id"] == cust_id).any():
            v = accbook[accbook["Cust_Id"] == cust_id].index.values
            print('\n')
            print(cus.loc[v[0],:])
            Func()
        else:
            print("Id is not available")
            Cus_Det()

#Graphs of Data
def Graph():
    global accbook
    Files()
    
    colors = sns.color_palette("Set2")
    colors2 = sns.color_palette("Set1")
    print('\n')
    print('<----- Data Graphs ----->')
    print('1 - Deposits under Each Kind of Account\n2 - Number of Accounts Opened under each Kind')
    ch = int(input('Enter Option ->'))

    if ch == 1:
        acc_data = accbook
        grouped_data = acc_data.groupby('Acc_Type')['Current_Balance'].sum()

        if not grouped_data.empty:
            plt.bar(grouped_data.index, grouped_data.values, width=0.3, color=colors2)
            plt.xlabel('Kind of Accounts')
            plt.ylabel('Deposits')
            plt.title('Deposits made under Kind of Acccount')
            plt.show()
        else:
            print("Data is not available, Try later")

    elif ch==2:
        data = accbook
        grouped_data = data.groupby('Acc_Type')['Acc_Type'].value_counts()

        if not grouped_data.empty:
            plt.bar(data['Acc_Type'],grouped_data,width=0.3,color=colors)
            plt.xlabel('Kind of Accounts')
            plt.ylabel('No. of Accounts Opened')
            plt.title('No. of accounts opened under Kind of Acccount')
            plt.show()
        else:
            print('Data is not available, Try Later')

    else:
        print('Invalid option')
    Func()

# Validates the inputs of the Update function
def validUpdate(ch, cust_id):
    global cus
    Files()

    v = cus[cus["Cust_Id"] == cust_id].index.values
    if ch == 1:
        dobp = cus.at[v[0], 'DOB']
        dob = str(dobp).split('/')
        age = calculateAge(d(int(dob[0]), int(dob[1]), int(dob[2])))
        cus.at[v[0], 'Age'] = age
        to_csv()
        print('The Age is updated.')
    elif ch == 2:
        phone = input('Enter the Phone Number ->')
        if phone.isdigit():
            if len(phone) == 10:
                cus.at[v[0], 'Phone_No'] = int(phone)
                to_csv()
                print('The Phone number is updated.')
            else:
                print('Enter a valid phone number')
                validUpdate(ch, cust_id)
        else:
            print('Enter a valid phone number')
            validUpdate(ch, cust_id)
    Func()

# Updates Information of the Customer
def Update():
    global cus
    Files()

    print('\n')
    print('<----- Update Information of Customers ----->')
    cust_id = input('Enter the Customer Id ->')
    if validate_id(cust_id):
        if not (cus['Cust_Id'] == cust_id).any():
            print('Id is not available')
            Update()
        else:
            print('1 - Age \n2 - Phone Number ')
            ch = int(input('Enter the Choice ->'))
            validUpdate(ch, cust_id)
    else:
        print('Enter the valid Id')
        Update()

#Closes the Account of Customer
def Close():
    global cus,accbook,trans
    Files()

    print('\n')
    print('<----- Close the Account ----->')
    cust_id = input('Enter the Cusotmer Id ->')
    if validate_id(cust_id):
        if (cus.loc[:,'Cust_Id'] == cust_id).any():
            v = cus[cus["Cust_Id"] == cust_id].index.values
            c = accbook.at[v[0],'Current_Balance']
            if c<0:
                print('Pay the outstanding amount to  the Bank before Account Closure.')
                Func()
            else:
                li = [cust_id,open_date,'Account Closure',c]
                trans.loc[i4,:] = li
                cus.drop(index=v[0],axis=0,inplace=True)
                accbook.drop(index=v[0],axis=0,inplace=True)
                print(f'The Account {cust_id} is closed and the Amount ₹{c} is returned.')
                to_csv()
                Func()
        else:
            print('Customer Id is not avaiable, Try Again')
            Close()
    else:
        print('Enter the Valid Id')
        Close()

# Main Functions of the Bank           
def Func():
    print('\n')
    print('1 - Create New Account\n2 - Deposit\n3 - Withdraw\n4 - Transfer\n5 - Customer Details\n6 - Account Details\n7 - Graphs\n8 - Update\n9 - Close\n10 - Exit')
    ch = int(input('Enter Option ->'))
    Files()
    
    if ch == 1:
        OpenAcc()
    elif ch == 2:
        Deposit()
    elif ch == 3:
        Withdraw()
    elif ch == 4:
        Transfer()
    elif ch == 5:
        Cus_Det()
    elif ch == 6:
        See_Acc()
    elif ch == 7:
        Graph()
    elif ch == 8:
        Update()
    elif ch==9:
        Close()
    elif ch == 10:
        exit()
    else:
        print('Invalid Option')
        Func()

