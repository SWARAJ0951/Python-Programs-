import threading
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

    t1=threading.Thread(target=SumEven, args=(100000000,))
    t2=threading.Thread(target=SumOdd, args=(100000000,))

    t1.start()
    t2.start()

    End_time=time.perf_counter()

    print(f"time required is : {End_time - Start_time:.4f}")#hita adhicha time yeto 

if __name__ == "__main__":
    main()