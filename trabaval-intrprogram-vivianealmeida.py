#os apostadores prognosticam o resultado sobre o acerto de 5 números em 50 possíveis, na grelha de "Números", e o acerto de 2 números/estrelas em 12 possíveis, na grelha das "Estrelas"

import random

userListStars = []
userListNumbers = []
listNumbers = []
listStars = []

#função para gerar números aleatórios
def generateRandomNumber(num1, num2):
    return random.randint(num1, num2)
#função criada para validar se o número já existe na lista
def isUniqueNumber(listNumber, number):
    for i in listNumber:
        if(i == number):
            return False
    return True

#função criada para validar se o caractere digitado é um número e se é válido (entre o range)
def requestValidNumbers(minValue, maxValue):
    while True:
        numberUser = (input(f"Indique um numero entre {minValue}  e {maxValue}:"))
        if numberUser.isdigit():
            numberInt = int(numberUser)
            if numberInt < minValue or numberInt > maxValue:
                print(f"O número {numberInt} não é válido.")
            else:
                return numberInt
        else:
            print("Esse não é um digito válido.")

        
def requestLotteryGameToUser():
    while(len(userListNumbers) < 5):
        numberAdded = requestValidNumbers(1, 50)
        if numberAdded in userListNumbers:
            print(f"O número {numberAdded} já existe.")
        else:
            userListNumbers.append(numberAdded)

def requestNumberStarsToUser():
    while(len(userListStars) < 2):
        numberAdded = requestValidNumbers(1, 12)
        if numberAdded in userListStars:
            print(f"O número {numberAdded} já existe.")
        else:
            userListStars.append(numberAdded)

#obs: não foi utilizado 'not in' nas duas funções pois não tinha certeza se contava como função built in (como choices). Então fiz uma de cada, para prática.
while (len(listNumbers) < 5):
    randomNumber = generateRandomNumber(1, 50)
    if(randomNumber not in listNumbers):
        listNumbers.append(randomNumber)


while (len(listStars) < 2):
    randomNumber = generateRandomNumber(1,12)
    if(isUniqueNumber(listStars, randomNumber)):
        listStars.append(randomNumber)


        

print(listNumbers)
print(listStars)
print(userListNumbers)