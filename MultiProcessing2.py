import multiprocessing
import time
import os

def SumEven(no):
    print(f"PID OF SumEven:{os.getpid()} PPID OF SumEven :{os.getppid()} ")
    Sum = 0

    for i in range(2,no,2):
        Sum = Sum + i

    print("Summation of Even :",Sum)

def SumOdd(no):
    print(f"PID OF SumOdd:{os.getpid()} PPID OF SumOdd :{os.getppid()} ")
    Sum = 0

    for i in range(1,no,2):
        Sum = Sum + i

    print("Summation of Odd :",Sum)

def main():
    print(f"PID OF Main:{os.getpid()} PPID OF Main:{os.getppid()} ")

    Start_time=time.perf_counter()

    t1=multiprocessing.Process(target=SumEven, args=(100,))
    t2=multiprocessing.Process(target=SumOdd, args=(100,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    End_time=time.perf_counter()

    print(f"time required is : {End_time - Start_time:.4f}")

if __name__ == "__main__":
    main()