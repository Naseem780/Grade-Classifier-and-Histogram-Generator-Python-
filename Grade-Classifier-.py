
valid_credits = [0, 20, 40, 60, 80, 100, 120]
progres=0
trailer=0
retriever=0
excluded=0
count=0
lis=[]

while True:
    

    while True:
        try:
            pas=int(input("Credit At Pass : "))
            if pas in valid_credits:
                break
            if pas>120:
                print("Out of range")
                continue
                
            
        except ValueError:
            print("Integer required")
            continue
                

    while True:
            
        try:
            defer=int(input("Credit At Defer : "))
            if defer in valid_credits:
                break
            if defer>120:
                print("Out of range")
                continue
        except ValueError:
                
            print("Integer required")
            continue

    while True:
        try:
                
            fail=int(input("Credit At Fail :"))
            if fail in valid_credits:
                break
            if fail>120:
                print("Out of range")
                continue
        except ValueError:
                
                
            print("Integer required")
            continue
             
            
        
        
        
        
        
    

    total= pas + defer + fail

    if total==120:
        if pas==120 and defer==0 and fail==0:
            print("progress")
            lis.append(["progress : ",pas,",",defer,",",fail])
            progres+=1
            count+=1
        elif pas==100 and (defer or fail==20):
            print("Progress (module trailer)")
            lis.append(["Progress (module trailer) : ",pas,",",defer,",",fail])
            trailer+=1
            count+=1
        elif (pas==40 and fail==80) or(pas==20 and (defer<=20) and (fail>=80)) or (pas==0 and defer<=40 and fail>=80):
                                        print("Exclude ")
                                        lis.append(["Exclude : ",pas,",",defer,",",fail])
                                        excluded+=1
                                        count+=1
        elif (pas==80 and (defer+fail==40)) or (pas==60 and defer+fail==60)or(pas==40 and defer+fail==80) or (pas==20 and defer+fail==100) or (pas==0 and defer+fail==120):
            print("Do not Progress – module retriever")
            lis.append(["Do not Progress – module retriever :  ",pas,",",defer,",",fail])
            retriever+=1
            count+=1
        else:
            print("Something went Wrong")
                
               
                    
                    





    else:
        print("Total Incorect")

    
    while True:
        
        cont=input("Do you want to Continue ? enter 'y' and 'q' for quit ")
        if cont =='y':
            break
        elif cont=='q':
            break
        
        
        
    
    if cont=='q':
        break

        
print("-------------------------------------------------------------------------")
print("Histogram")
print("progres"+" "+str(progres)+"\t : "+progres*"*")
print("Trailer"+" "+str(trailer)+"\t : "+trailer*"*")
print("Retriever"+" "+str(retriever)+"\t : "+retriever*"*")
print("Excluded"+" "+str(excluded)+"\t : "+excluded*"*")
print()
print(str(count)+" "+"outcomes in toal")

print("-------------------------------------------------------------------------")


for i in lis:
    for j in i:
        print(j,end=' ')
    print()    


with open("filss.txt", "w") as file:
    # Write content to the file

    for i in lis:
        for j in i:
            file.write(str(j))
            
        file.write("\n") 
'''
with open("fil.txt", "w") as file:
    for i in lis:
        for j in i:
            file.write(str(j) + ' ')
        file.write('\n')'''



    
        
    
       


























        
