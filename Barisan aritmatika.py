suku_awal=int(input("Masukkan suku awal: "))
beda=int(input("Masukkan beda: "))
batasan_suku=int(input("Masukkan batasan suku: "))
temp=suku_awal
for i in range(batasan_suku):
    print(temp, end=" , ")
    temp+=beda
