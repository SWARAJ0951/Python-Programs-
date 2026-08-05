import time

#2+4+6+8 = 20
def SumEven(no):
    Sum = 0

    for i in range(2,no,2):
        Sum = Sum + i

    print("Summation of Even :",Sum)


#1+3+5+7+9=25
def SumOdd(no):
    Sum = 0

    for i in range(1,no,2):
        Sum = Sum + i

    print("Summation of Odd :",Sum)


def main():

    Start_time=time.perf_counter()
    SumEven(100000000)
    SumOdd(100000000)
    End_time=time.perf_counter()

    print(f"time required is : {End_time - Start_time:.4f}")

if __name__ == "__main__":
    main()