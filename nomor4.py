import math
# NIM : 10116347
# Nama : Lukmannudin
# Kelas : MOSI-08
# Catatan : Dijalankan di python versi 3

class RandomNumberMultiplicativeGenerator:
    def __init__(self, a, m, z0, n):
            self.a = a
            self.m = m
            self.zi = z0
            self.n = n
            self.randomNumbersIntegerAndUniform = []
    
    def countWithMultiplicativeMethod(self,zi):
        # zi = nilai bilangan ke-i dari deretnya (RN yang baru)
        result = (self.a*zi) % self.m
        return result
    
    def resultUniformMultiplicativeMethod(self,numbers):
        randomUniformNumbers = []
        resultUniform = []

        for numberPosition in range(0,len(numbers)):
            resultUniform = numbers[numberPosition] / self.m
            randomUniformNumbers.append(resultUniform)
        
        return randomUniformNumbers
    
    def resultIntegerMultiplicativeMethod(self):
        randomIntegerNumbers = []
        i = 0
        while i < self.n:
            self.zi = self.countWithMultiplicativeMethod(self.zi)
            randomIntegerNumbers.append(self.zi)
            i = i + 1
        
        return randomIntegerNumbers

    def getRandomNumbers(self):
        numbers = self.resultIntegerMultiplicativeMethod()
        randomNumbersMultivicate = [
            numbers,
            self.resultUniformMultiplicativeMethod(numbers)
        ]
        return randomNumbersMultivicate    

class RandomNumberGenerator: 
    # a = konstanta pengali
    # c = increment(angka konstan yang bersyarat)
    # m = modulus(modulo)
    # z0 = kunci pembangkit / seed
    # n = jumlah deret

    def __init__(self,a,m,z0,n,c=0):
        self.initilize(a,c,m,z0,n)
        self.MultiplicativeMethod = RandomNumberMultiplicativeGenerator(a,m,z0,n)
        
    def initilize(self,a,c,m,z0,n):
        self.a = a
        self.c = c
        self.m = m 
        self.zi = z0
        self.n = n 

    def generateRandomMultiplicativeNumbers(self):
        fe = 0.05
        n = self.n
        mt = RandomNumberMultiplicativeGenerator(self.a,self.m,self.zi,self.n)
    
        randomNumbers = mt.getRandomNumbers()
        
        _list = []
        # for i in range(0,len(randomNumbers[0])):
        #     _list.append({'Z':randomNumbers[0][i], 'U':randomNumbers[1][i]})

        
        print("|\ti\t|\tZi\t|\tUi\t|\tPk\t|\tPk <\t|\t X\t|")
        
        pkstatus = "S"
        X= "-"
        k = p = 0

        sumoforder = 0
        sumofcustomers = 0
        conditionSuccess = 5

        i = 0
        counter = 0
        isEnough = False
        
        while not isEnough:
            self.zi = self.countWithMultiplicativeMethod(self.zi)
            Ui = self.countUniformMultiplicativeMethod(self.zi)
            _list.append({'Z':self.zi, 'U':Ui})

            if (k==0):
                p = _list[i]['U']
            else :
                p = _list[i-1]['P'] * _list[i]['U']

            _list[i]['P'] = p

            if _list[i]['P'] < fe:
                pkstatus = "B"
                if k==0 :
                    hasil = '-'
                else :
                    hasil = k
                    sumoforder = sumoforder + k
                    sumofcustomers = sumofcustomers + 1
                    counter = counter +1
                   
                
                print("|\t{}\t|  {:.0f}\t\t|  {:.4f}\t|  {:.4f}\t|  \t{}\t|\t {} \t|"
                .format(i+1, _list[i]['Z'], _list[i]['U'],_list[i]['P'],pkstatus, hasil)
                )
                
                k=0
            else:
                pkstatus = "S"
                X = "-" 
                k = k +1    
                print("|\t{}\t|  {:.0f}\t\t|  {:.4f}\t|  {:.4f}\t|  \t{}\t|\t {} \t|"
                .format(i+1, _list[i]['Z'], _list[i]['U'],_list[i]['P'],pkstatus, X)
                ) 

            if (counter == conditionSuccess):
                isEnough = True
                
            i = i+1
            
        print()
        print("Jumlah Pelanggan yang datang adalah " + str(sumofcustomers) + " pelanggan")
        print("Rata-rata pemesanan yang dilakukan adalah "+ str( sumoforder/sumofcustomers) + " potong ayam")
            
    def countWithMultiplicativeMethod(self,zi):
    # zi = nilai bilangan ke-i dari deretnya (RN yang baru)
        result = (self.a*zi) % self.m
        return result
    
    def countUniformMultiplicativeMethod(self,number):
        resultUniform = number / self.m
        return resultUniform

class RandomVariateGenerator:
    def __init__(self, uniformNumbers):
        self.uniformNumbers = uniformNumbers
    
    def getResultEksponen(self):
        cdfNumbers = []
        for number in self.uniformNumbers:
            result = None
            result = -0.1 * math.log(number)
            cdfNumbers.append(result)

        return cdfNumbers
    
    def getPkNumbers(self,UiNumbers):
        pkNumbers= []
        for i in range(0,len(UiNumbers)):
            if i == 0:
                pkNumbers.append(UiNumbers[i])
            else:
                pkNumbers.append(UiNumbers[i]*pkNumbers[i-1])
        
        return pkNumbers

    
    

a = 7
m = 128
z0 = 12357
n = 10

i=1
k=1
rng = RandomNumberGenerator(a,m,z0,n)
rng.generateRandomMultiplicativeNumbers()
