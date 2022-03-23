from statistics import NormalDist as ND
import statistics as st
s=[]
n=int(input("Enter the number of data points"))
for i in range(0,n):
    a=int(input())
    s.append(a)
Mean=st.mean(s)
sd=st.stdev(s)
print("Mean :",Mean)
print("Standard deviation :",sd)
a=ND(mu=Mean,sigma=sd)
n=int(input("range points  :"))
if n==1:
    A=int(input())
    print("choose if 1) at the point or 2) above or 3) lower")
    choice=input()
    if choice=='at the point':
        print(0)
    elif choice=='above':
        print(1-a.cdf(A))
    else:
        print(a.cdf(A))
else:
    for i in range(n):
        l=int(input("lowerrange :"))
        u=int(input("upperrange :"))
        print(a.cdf(u)-a.cdf(l))
