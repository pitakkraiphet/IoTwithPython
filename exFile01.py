f = open("data.txt","a")
f.write("test")
f.close()

f = open("data.txt","r")
print(f.read())
#print(f.readline())
#print(f.readline())
#print(f.readlines())