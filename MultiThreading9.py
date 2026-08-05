import threading
import time

#2+4+6+8 = 20
def SumEven(no):
    print("PID OF SumEven Thread is :",threading.get_ident())

#1+3+5+7+9=25
def SumOdd(no):
    print("PID OF SumOdd Thread is :",threading.get_ident())

def main():

    print("TID OF MainThread Thread is :",threading.get_ident())


    Start_time=time.perf_counter()

    t1=threading.Thread(target=SumEven, args=(100000000,))
    t2=threading.Thread(target=SumOdd, args=(100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    End_time=time.perf_counter()

    print(f"time required is : {End_time - Start_time:.4f}")

if __name__ == "__main__":
    main()