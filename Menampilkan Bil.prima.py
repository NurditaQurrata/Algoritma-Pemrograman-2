n=int(input("Masukkan berapa banyak bilangan prima yang akan ditampilkan: "))
count=0
angka=2
while count != n:
    p=1
    p+=1
    while angka%p!=0:
        p+=1
    if p == angka:
        print(angka,end=",")
        count+=1
    angka+=1
