def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False
         
def main():
    Value = int(input("Enter no :"))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is False")    

if __name__ == "__main__":
    main()