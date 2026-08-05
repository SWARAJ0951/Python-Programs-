def Factorial(no):
    Fact=1
    
    for i in range(1,no+1):
        Fact = Fact*i

    return Fact

def main():
    Value = int(input("enter no :"))

    Ret = Factorial(Value)

    print(f"Factorial is {Value} is {Ret}")

if __name__ == "__main__":
    main()