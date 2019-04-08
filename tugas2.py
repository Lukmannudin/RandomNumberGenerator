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
    
    def resultUniformMultiplicativeMethod(self):
        randomUniformNumbers = []
        resultUniform = []
        randomIntegerNumbers = self.resultIntegerMultiplicativeMethod()

        for integerNumber in randomIntegerNumbers:
            resultUniform = integerNumber / self.m
            randomUniformNumbers.append(resultUniform)

        return randomUniformNumbers
    
    def resultIntegerMultiplicativeMethod(self):
        randomIntegerNumbers = []
        i = 0
        while i<= self.n:
            self.zi = self.countWithMultiplicativeMethod(self.zi)
            randomIntegerNumbers.append(self.zi)
            i = i + 1
        
        return randomIntegerNumbers

    def getRandomNumbers(self):
            
        randomNumbersMultivicate = [
            self.resultIntegerMultiplicativeMethod(),
            self.resultUniformMultiplicativeMethod()
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
        n = self.n
        mt = RandomNumberMultiplicativeGenerator(self.a,self.m,self.zi,self.n)
        RVG = RandomVariateGenerator(self.MultiplicativeMethod.resultUniformMultiplicativeMethod())
    
        randomNumbers = mt.getRandomNumbers()
        randomNumbers.append(RVG.getResultCDF())

        ZiRandomNumbers = randomNumbers[0]
        UiRandomNumbers = randomNumbers[1]
        XiRandomNumbers = randomNumbers[2]
        ZiLoopedPosition = self.periodikCheck(ZiRandomNumbers)
        UiLoopedPosition = self.periodikCheck(UiRandomNumbers)
        XiLoopedPosition = self.periodikCheck(XiRandomNumbers)
        if (ZiLoopedPosition + UiLoopedPosition + XiLoopedPosition) > 0 :
            print("Zi terulang di posisi "+str(ZiLoopedPosition))
            print("Ui terulang di posisi "+str(UiLoopedPosition))
            print("t terulang di posisi "+str(XiLoopedPosition))

        print("|\ti\t|\tZi\t|\tUi\t|\tt\t|")
        for i in range(0,n):
            print("|\t{}\t|  {:.0f}\t\t|  {:.4f}\t|  {:.4f}\t|"
                .format(i+1, randomNumbers[0][i], randomNumbers[1][i],randomNumbers[2][i])
                )
      

    def getAverageMultiplicative(self):
        RVG = RandomVariateGenerator(self.MultiplicativeMethod.resultUniformMultiplicativeMethod())
        
        return RVG.getAverage()


    def periodikCheck(self,numbers):
        loopedPosition = 0
        tempNumber = numbers[0]
        for i in range(1,len(numbers)):
            if (numbers[i] == tempNumber):
                loopedPosition = i+1
                break

        return loopedPosition

class RandomVariateGenerator:
    def __init__(self, uniformNumbers):
        self.uniformNumbers = uniformNumbers
    
    def getResultCDF(self):
        cdfNumbers = []
        for number in self.uniformNumbers:
            result = None
            result = -0.1 * math.log(number)
            cdfNumbers.append(result)

        return cdfNumbers

    def getAverage(self):
        result = []
        n = len(self.getResultCDF())
        for r in self.getResultCDF():
            print(r)

        return n
    


a = 7
m = 128
z0 = 12357
n = 5
rng = RandomNumberGenerator(a,m,z0,n)
# rng.generateRandomLCGTableNumbers()
rng.generateRandomMultiplicativeNumbers()
print(rng.getAverageMultiplicative())
