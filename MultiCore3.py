import time

def Sumcube(no):
    Sum = 0

    for i in range (1,no+1):
        Sum = Sum +(i**3)
    return Sum

def main():
    Data = [10000000,20000000,30000000,40000000,5000000]
    Result = []

    Start_time=time.perf_counter()

    for value in Data:
        Ret = Sumcube(value)
        Result.append(Ret)

    end_time=time.perf_counter()

    print("Result is :")
    print(Result)
    print(f"Time Required :{end_time - Start_time :4f} seconds")



if __name__ == "__main__":
    main()