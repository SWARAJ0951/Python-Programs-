import threading

def Display():
    print("Inside Display :",threading.get_ident())

def main():
    print("Inside Main :",threading.get_ident())

    tobj = threading.Thread(target=Display)

    tobj.start()
   

if __name__ == "__main__":
    main()

#hya code mdhi tobj tayar kela ani tela sangitla thread mhanuna kaam kar .Ani function tikde call kela .start mhanla ki suru honar