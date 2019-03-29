class RandomNumberTCGGenerator:
    def __init__(self, a, c, m, z0, n):
        self.a = a
        self.c = c
        self.m = m
        self.zi = z0
        self.n = n
        self.randomNumbersIntegerAndUniform = []

    def checkVariable(self):
        print("ABC")
        print("a = "+str(self.a))
        print("c = "+str(self.c))
        print("m = "+str(self.m))
        print("z0 = "+str(self.zi))
        print("n = "+str(self.n))

    def countWithTCGMethod(self,zi):
        # zi = nilai bilangan ke-i dari deretnya (RN yang baru)
        result = (self.a*zi+self.c) % self.m
        return result
    
    def resultIntegerTCGMethod(self):
        randomIntegerNumbers = []
        for i in range(0,self.n):
            self.zi = self.countWithTCGMethod(self.zi)
            randomIntegerNumbers.append(self.zi)
        
        return randomIntegerNumbers

    def resultUniformTCGMethod(self,modulo):
        randomUniformNumbers = []
        randomIntegerNumbers = self.resultIntegerTCGMethod()

        for integerNumber in randomIntegerNumbers:
            resultUniform = integerNumber / modulo
            randomUniformNumbers.append(resultUniform)

        return randomUniformNumbers

    def getRandomNumbers(self):
        randomNumbersTCG = [
            self.resultIntegerTCGMethod(),
            self.resultUniformTCGMethod(self.m),
            self.n
        ]
        return randomNumbersTCG


class RandomNumberGenerator: 
    # a = konstanta pengali
    # c = increment(angka konstan yang bersyarat)
    # m = modulus(modulo)
    # z0 = kunci pembangkit / seed
    # n = jumlah deret
    # randomIntegerNumbers
    def __init__(self):
        a = 2
        c = 7
        m = 10
        z0 = 2
        n = 10
        tcg = RandomNumberTCGGenerator(a,c,m,z0,n)
        self.randomNumbers = tcg.getRandomNumbers()
    
    def getRandomTCGRandomNumbers(self):
        return self.randomNumbers
    
    def generateRandomTCGTableNumbers(self):
        randomNumbers = self.getRandomTCGRandomNumbers()
        print("i \t\t zi \t\t Ui \t\t")
        # for r in randomNumbers:
            # print(str(r[2]))
            # i = 1
            # print(str(i) +" \t\t "+r)
            # i = i+1
        
        
rng = RandomNumberGenerator()
print(rng.getRandomTCGRandomNumbers())
rng.generateRandomTCGTableNumbers()
