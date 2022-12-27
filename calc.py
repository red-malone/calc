def add(a,b):
    c=a+b
    print("\nSum is ",c,"\n")
def subtract(a,b):
    c=a-b
    print("\nDifference is ",c,"\n")
def multiply(a,b):
    c=a*b
    print("\nProduct is ",c,"\n")
def divide(a,b):
    c=a/b
    d=a%b
    e=a//b
    print("\nValue is ",c,"\n")
    print("Quotient is ",e,"\n")
    print("Remainder is ",d,"\n")

    

if __name__=="__main__":
        y="y"
        while(y=='y'or y=='Y'):
            print("--------Simple Calculator--------")
            print("1)Add\n2)Subtract\n3)Multiple\n4)Divide\n")
            op=int(input("Enter your choice :"))
            a=float(input("Enter the number : "))
            b=float(input("Enter the second number : "))
            if(op==1):
                add(a,b)
            elif(op==2):
                subtract(a,b)
            elif(op==3):
                multiply(a,b)
            elif(op==4):
                divide(a,b)
            else:
                print("Invalid operation")
            y=input("Do you want to continue?(Y/N)")
            
            
