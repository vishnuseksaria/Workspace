m={}
c={}
d={}
count=0
count2=0
from getpass import getpass

def add():      #function to add credentials
    user_a=input("\n     Enter username : ")
    pass_a=input("     Enter password : ")
    c[user_a]=pass_a
    details=input("     Enter details about credentials : ")
    d[user_a]=details

def delete(count2):       #function to delete credentials
    if count2>0:
        dlt=input("\n     Enter the username to delete : ")
        if dlt in c:
            del c[dlt]
            print("\n     DATA DELETED.")
            count2-=1
        else:
            print("\n     USERNAME NOT FOUND.")
    else:
        print("\n     NO DATA FOUND.")
    return count2

def update():       #function to add credentials
    if count2>0:
        up=input("\n     Enter username to be updated : ")
        if up in c:
            add()
            del c[up]
            print("\n     DATA UPDATED.")
        else:
            print("\n     Username not found")
    else:
        print("\n     NO DATA FOUND.")

def list1():        #function to list all the credentials
    if count2>0:
        print()
        for i in c:
            print("     Username :",i,"     Password :",c[i],"     Details :",d[i])
    else:
        print("\n     NO DATA FOUND.")
def create():       #function to create an account
    u=input("\n     Enter a username : ")
    p=getpass("     Enter a password : ")
    m[u]=p
    print("\n     ACCOUNT SUCCESSFULLY CREATED.")
def login(b=0,z=0):        #function to login to an account
    if count!=0:
        user_m=input("\n     Enter username : ")
        if user_m in m:
            z=1
            pass_m=getpass("     Enter password : ")
            if pass_m==m[user_m]:
                print("\n     WELCOME",user_m)
                b=1
            else:
                print("\n     INCORRECT PASSWORD, TRY AGAIN...")
                b=0
        else:
            z=0
            print("\n     USERNAME NOT FOUND, TRY AGAIN...")
    else:
        print("\n     NO ACCOUNTS FOUND.")
    return b,z
l1=["\n     WELCOME TO PASSWORD MANAGER.","Create Account.","Login to your account.","Delete your account.","Exit."]
while True:
    for i in range(5):
        if i==0:
            print(l1[i])
        else:
            print("\n",i,".",l1[i])
    ch=int(input("\n     Enter your choice : "))
    if ch==1:
        create()
        count+=1
    elif ch==2:
        b,z=login()
        if z==1 and b==1:
            l2=["    Here is a list of tasks that you can perform.","Add credentials.","Delete credentials.","Update credentials.","List credentials.","Exit"]
            while True:
                for i in range(6):
                    if i==0:
                        print("\n",l2[i])
                    else:
                        print("\n",i,".",l2[i])
                ch1=int(input("\n     Enter your choice : "))
                if ch1==1:
                    add()
                    print("\n     DATA ADDED.")
                    count2+=1
                elif ch1==2:
                    count2=delete(count2)
                elif ch1==3:
                    update()
                elif ch1==4:
                    list1()
                elif ch1==5:
                    break
                else:
                    print("\n     NOT APPLICABLE, TRY AGAIN...")
    elif ch==3:
        if count!=0:
            dlt_m=input("\n     Enter username to be deleted : ")
            if dlt_m in m:
                dlt_p=getpass("     Enter password : ")
                if dlt_p==m[dlt_m]:
                    del m[dlt_m]
                    print("\n     ACCOUNT SUCCESSFULLY DELETED.")
                    count-=1
                else:
                    print("\n     INCORRECT PASSWORD, TRY AGAIN...")
            else:
                print("\n     USERNAME NOT FOUND.")
        else:
            print("\n     NO ACCOUNTS FOUND.")
    elif ch==4:
        print("\n     THANK YOU FOR USING PASSWORD MANAGER.")
        break
    else:
        print("\n     NOT APPLICABLE, TRY AGAIN...")
