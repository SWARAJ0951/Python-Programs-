CheckEven = lambda No:(No % 2 == 0)

def main():
    Value = int(input("Enter no :"))

    Ret = CheckEven(Value)    #RET = (Value % 2 == 0)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")    

if __name__ == "__main__":
    main()