def main():
    Ans = 0

    try:
        print("Enter First Number :")
        No1 = int(input())

        print("Enter Second Number :")
        No2 = int(input())

        Ans = No1 / No2

        print("Division Is Succesfull")

    except ZeroDivisionError as zobj:      #Specific Exception Block
        print("Exception Occured due to second operand is zero :",zobj)

    except ValueError as vobj:
        print("Exception Occured Due to invalid Data type :",vobj)  

    except Exception as eobj:         #Generic Exception Block
        print("Exception Occured :",eobj)  

    print("Result is :",Ans)

if __name__ == "__main__":
    main()