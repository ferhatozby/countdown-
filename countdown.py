import time
def zaman():
    x=int(input("sayı giriniz: "))
    for i in range(x,0,-1):
        time.sleep(1)
        print(i)


zaman()

