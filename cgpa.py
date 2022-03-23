n=int(input("Enter the number of semesters you want to calculate cgpa for :"))
r=[]
for j in range(1,n+1):
    print("Enter the number of papers in semester",j)
    b=int(input())
    print("choose your grade from: O or A+ or A or B+ or B or RA or SW or W")
    sum=0
    for i in range(1,b+1):
        print("Enter the grade obtained for the paper",i)
        a=str(input())
        if(a=='O'):
            sum+=10
        elif (a=='A+'):
            sum+=9
        elif(a=='A'):
            sum+=8
        elif(a=='B+'):
            sum+=7
        elif(a=='B'):
            sum+=6
        else:
            sum+=0
    result=sum/b
    r.append(result)
#print(r)
cgpa=0
for i in range(0,len(r)):
    cgpa+=r[i]
cgpa=cgpa/n
for x in range(0,len(r)):
        print("Your gpa for semester",x+1,"is :",r[x])
print("Your cgpa is",cgpa)
