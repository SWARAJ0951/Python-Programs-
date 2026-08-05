print("---------Ticket Pricing Software-----------")

print("Enter your age : ")
Age = int(input())

if(Age <= 5):
    print("Ticket is Free")
elif(Age > 5 and Age <= 18):
    print("Ticket Price is 900")
elif(Age > 18 and Age <= 40):
    print("Ticket Price is 1200")
else:
    print("Ticket Price is 500")    
