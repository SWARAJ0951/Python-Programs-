def main():
    Size=0
    Arr = list()

    print("enter the no elements:")
    Size=int(input())

    print("Enter the Elements")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

if __name__ == "__main__":
    main()