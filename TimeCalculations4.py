import time

def Factorial(no):
    Fact=1
    
    for i in range(1,no+1):
        Fact = Fact*i

    return Fact

def main():
    Value = int(input("enter no :"))

    Start_time = time.time()

    Ret = Factorial(Value)

    End_time = time.time()

    print(f"Factorial is {Value} is {Ret}")

    print(f"Time Required is :{End_time - Start_time:.5f} seconds ")

if __name__ == "__main__":
    main()