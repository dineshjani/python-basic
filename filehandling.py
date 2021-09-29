#file =open("geek.txt","w")
#file.write("this is thw write")
with open("geek.txt") as file:
    data=file.read()
    print(data)

#dump
