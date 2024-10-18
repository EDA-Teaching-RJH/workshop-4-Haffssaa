name = input( "Enter a name")

snake_case = ""

for c in name:
     if c.islower():
        print (c,end="")
     if c.isupper() : 
        print ("_" , c.lower(),end="",sep="")

print()
