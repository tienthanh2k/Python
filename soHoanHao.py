print("nhap so n= ")
n= int(input())
s= 0
if n<=0:
    print("gia tri khong thoa man. hay nhap gia tri duong")
else:
    for i in range(1,n):
        if n%i==0:
            s+=i
    if n==s:
        print(n, " la so hoan hao")
    else:
        print(n, " khong la so hoan hao")
