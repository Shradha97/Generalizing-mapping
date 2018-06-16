import random
import math

def getData():                              # this function generates random numbers lying in the specified ranges
    T = random.randint(94, 103)
    HR = random.randint(30, 130)
    BP = random.randint(20, 230)
    #print("T:", T)
    #print("HR:", HR)
    #print("BP:", BP)
    return (T, HR, BP)

def update(M1, M2, M3, S1, S2, S3, n):      # Welford's method of computing mean and variance
    for k in range(1, n+1):                 # It continuously computes the variance and mean without knowing the whole set of observations
        (T, HR, BP) = getData()
        oldM1 = M1                          # M1, M2, M3 are the means of Temperature, Heart rate, Blood Pressure observations respectively
        oldM2 = M2
        oldM3 = M3
        M1 = M1 + (T - M1)/k                # Recursive formula for calculating mean
        S1 = S1 + (T - M1)*(T - oldM1)      # Recursive formula for calculating N*variance
        M2 = M2 + (HR - M2)/k
        S2 = S2 + (HR - M2)*(HR - oldM2)
        M3 = M3 + (BP - M3)/k
        S3 = S3 + (BP - M3)*(BP - oldM3)
    return (M1, M2, M3, S1, S2, S3)

def getAdditionalFactor(M1, M2, M3):        # This function calculates the deviation of mean of the observations and the supposed mid values of the observations
    d1 = (M1 - float(99))**2                # 99, 75, 120 are the supposed mid values of Temperature, Heart rate and Blood Pressure respectively
    d2 = (M2 - float(75))**2
    d3 = (M3 - float(120))**2
    return (d1, d2, d3)

def getMaxRangeT(listT):                    # This function calculates maximum allowed ranges for the conditons for Temperature
    listT.append(abs(float(97) - float(99)))
    listT.append(abs(float(96) - float(99)))
    listT.append(abs(float(95) - float(99)))

def getMaxRangeHR(listHR):                  # This function calculates maximum allowed ranges for the conditons for Heart Rate
    listHR.append(abs(float(85) - float(75)))
    listHR.append(abs(float(100) - float(75)))
    listHR.append(abs(float(110) - float(75)))

def getMaxRangeBP(listBP):                  # This function calculates maximum allowed ranges for the conditons for Blood Pressure
    listBP.append(abs(float(141) - float(120)))
    listBP.append(abs(float(170) - float(120)))
    listBP.append(abs(float(200) - float(120)))

def mappingT(d1, S1, listT):                # These functions output the mapped values and the corresponding condition
    varNew = math.sqrt(S1 + d1)
    print("The mapped value is:", varNew)
    #print(varNew)
    if varNew < listT[0] and varNew >= 0:
        print("Condition is Normal")

    if varNew < listT[1] and varNew >= listT[0]:
        print("Condition is of Low Severity")

    if varNew < listT[2] and varNew >= listT[1]:
        print("Condition is Grave")

    if varNew >= listT[2]:
        print("Condition is Critical")

def mappingHR(d2, S2, listHR):
        varNew = math.sqrt(S2 + d2)
        print("The mapped value is:", varNew)
        #print(varNew)
        if varNew <= listHR[0] and varNew >= 0:
            print("Condition is Normal")

        if varNew <= listHR[1] and varNew > listHR[0]:
            print("Condition is of Low Severity")

        if varNew <= listHR[2] and varNew > listHR[1]:
            print("Condition is Grave")

        if varNew > listHR[2] :
            print("Condition is Critical")

def mappingBP(d3, S3, listBP):
        varNew = math.sqrt(S3 + d3)
        print("The mapped value is:", varNew)
        #print(varNew)
        if varNew <= listBP[0] and varNew >= 0:
            print("Condition is Normal")

        if varNew <= listBP[1] and varNew > listBP[0]:
            print("Condition is of Low Severity")

        if varNew <= listBP[2] and varNew > listBP[1]:
            print("Condition is Grave")

        if varNew > listBP[2] :
            print("Condition is Critical")

##########################################

sample_size = input("Enter the number of observations required:")

type(sample_size)

listT = []
listHR = []
listBP = []

(M1, M2, M3, S1, S2, S3) = update(0, 0, 0, 0, 0, 0, int(sample_size))

getMaxRangeT(listT)
getMaxRangeHR(listHR)
getMaxRangeBP(listBP)

(d1, d2, d3) = getAdditionalFactor(M1, M2, M3)

mappingT(d1, S1/int(sample_size), listT)
print('\n')
mappingHR(d2, S2/int(sample_size), listHR)
print('\n')
mappingBP(d3, S3/int(sample_size), listBP)
print('\n')
