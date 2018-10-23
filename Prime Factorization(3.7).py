#Created by Oranje Maan
#12 October 2018
#Prime Factorization Function


def primeFactorization(number):
    #List of variables
    beenUsed = False
    uncertainty = False
    continuation = True
    count = 0
    currentPrime = 0
    isNegative = False
    primeNumberList = []
    primesList = []
    useNumber = 0
    #Checking to see if input is an integer
    try:
        int(number)
    except:
        print("The input was not an integer.")
        return
    #Assigning a to input
    number = int(number)
    a = number
    #Reading a file with prime numbers
    primeNumberList = open("listPrime.txt","r")
    #Checking to see if number is negative
    if(number < 0):
        number = -number
        isNegative = True
        a = number
    #Looking for special cases
    if(number == 1):
        print("1 is neither a prime nor a composite number. It's only factor is itself.")
    elif(number == 0):
        print("0 is neither a prime nor composite number. It's only factor is itself.")
    else:
        #Finding the amount of prime numbers in listPrime smaller than the inputed number
        while(continuation):
            try:
                currentPrime = int(primeNumberList.readline())
            except:
                continuation = False
                uncertainty = True
            if (number <= currentPrime):
                continuation = False
            else:
                count = count + 1
                primesList.append(currentPrime)
        #Checking to see number of times dividable by every prime in primesList
        for i in range(count):
            continuation = True
            useNumber = 0
            while (continuation):
                if (a % primesList[i] == 0):
                    useNumber = useNumber + 1
                    beenUsed = True
                    a = a / primesList[i]
                else:
                    continuation = False
                    if(useNumber > 0):
                        print(str(primesList[i]) + " - " + str(useNumber))
        #Checking to see if prime
        if (beenUsed == False and isNegative == False):
            print(str(a) + " is a prime number. It's only factor is itself and one.")
    #Checking to see if negative
    if (isNegative):
        print("As this is a negative number, one and only one of the factors has to be negative.")
    #Checking if in bounds of certainty
    if (uncertainty):
        print("The number is larger than the largest prime in the list. The results may be innacurate.")

#Calling function in main()       
def main():
    number = input("Give an integer please.")
    primeFactorization(number)
    
main()
