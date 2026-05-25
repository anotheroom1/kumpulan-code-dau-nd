#buat class dan def
class prime:
    def __init__(self):
        self.b=[]
    def default(self,a):
        for i in range(1,a+1):
            if(a%i==0):
                self.b.append(i)
    def factor(self,a):
        self.default(a)
        return self.b
    def isprime(self,a):
        return (len(self.b)==2)

#panggil fungsi+loop
while True:
    a = int(input("Masukan angka :"))
    c = prime()
    print("Faktor pembagi :", c.factor(a))
    d=""
    if (c.isprime(a)==False):
        d = "Bukan "
    print(d+ "Prima")
