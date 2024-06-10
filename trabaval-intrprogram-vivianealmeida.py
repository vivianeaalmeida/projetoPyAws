#os apostadores prognosticam o resultado sobre o acerto de 5 números em 50 possíveis, na grelha de "Números", e o acerto de 2 números/estrelas em 12 possíveis, na grelha das "Estrelas"

import random

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