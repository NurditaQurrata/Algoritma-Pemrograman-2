a=int(input("Masukkan bilangan: "))
p=1
if a==2:
    print("Bilangan prima")
else:
    if a==1 or a==0:
        print("Bukan bilangan prima")
    else:
        p=p+1
        while a%p!=0:
            p=p+1
        if p==a:
            print("Bilangan prima")
        else:
            if a%p==0:
                print("Bukan bilangan prima")
