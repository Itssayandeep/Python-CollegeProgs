for i in range(100,200):
    isprime=" prime "
    iseven=" not even "
    num=i
    ans=0
    for j in range(2,i):
        if(i%j==0):
            isprime=" not prime "
            break
    while (num!=0):
        digit=num%10
        ans+=digit
        num//=10
    if(ans%2==0):
        iseven=" even "
    print(i,"is",isprime,"and sum of digit ",iseven)