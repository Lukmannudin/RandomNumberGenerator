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

    def __init__(self):
        a = 913
        c = 112
        m = 10000
        z0 = 2
        n = 300
        self.initilize(a,c,m,z0,n)
        tcg = RandomNumberTCGGenerator(self.a,self.c,self.m,self.z0,self.n)
        self.randomNumbers = tcg.getRandomNumbers()
    
    def initilize(self,a,c,m,z0,n):
        self.a = a
        self.c = c
        self.m = m 
        self.z0 = m
        self.n = n

    def getRandomTCGRandomNumbers(self):
        return self.randomNumbers
    
    def generateRandomTCGTableNumbers(self):
        if (self.a < self.m and self.c < self.m):
            randomNumbers = self.getRandomTCGRandomNumbers()
            n = self.n

            ZiRandomNumbers = randomNumbers[0]
            UiRandomNumbers = randomNumbers[1]
            ZiLoopedPosition = self.periodikCheck(ZiRandomNumbers)
            UiLoopedPosition = self.periodikCheck(UiRandomNumbers)
            
            if (ZiLoopedPosition + UiLoopedPosition) > 0:
                print("Zi terulang di posisi "+str(ZiLoopedPosition))
                print("Ui terulang di posisi "+str(UiLoopedPosition))
            else: 
                print("|  i\t|   Zi\t |    Ui    |")
                for i in range(0,n):
                    print("|  {}\t| {:.0f} \t | {:.4f}".format(i+1, randomNumbers[0][i], randomNumbers[1][i])
                        + "   |"
                        )
        else:
            print("Seharusnya a < m dan c < m")        

    def periodikCheck(self,numbers):
        loopedPosition = 0
        tempNumber = numbers[0]
        for i in range(1,len(numbers)):
            if (numbers[i] == tempNumber):
                loopedPosition = i+1
                break

        return loopedPosition


rng = RandomNumberGenerator()
rng.generateRandomTCGTableNumbers()
