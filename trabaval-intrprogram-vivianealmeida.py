#Sobre a Euromilhões: os apostadores prognosticam o resultado sobre o acerto de 5 números em 50 possíveis, na grelha de "Números", e o acerto de 2 números/estrelas em 12 possíveis, na grelha das "Estrelas"
import random

#lista de numeros que o usuario insere
userListStars = []
userListNumbers = []
#lista de numeros sorteados - números e estrelas
listNumbers = []
listStars = []

#função para gerar números aleatórios para o sorteio
def generateRandomNumber(num1, num2):
    return random.randint(num1, num2)
#função criada para validar se o número já existe na lista
def isUniqueNumber(listNumber, number):
    for i in listNumber:
        if(i == number):
            return False
    return True

#função criada para validar se o caractere digitado é um número e se é válido (está entre o range)
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

#função criada para pedir ao usuario os 5 números do jogo.
def requestLotteryGameToUser():
    while(len(userListNumbers) < 5):
        numberAdded = requestValidNumbers(1, 50)
        if numberAdded in userListNumbers:
            print(f"O número {numberAdded} já existe.")
        else:
            userListNumbers.append(numberAdded)

#função criada para pedir ao usuario os 2 números de estrelas.
def requestNumberStarsToUser():
    while(len(userListStars) < 2):
        numberAdded = requestValidNumbers(1, 12)
        if numberAdded in userListStars:
            print(f"O número {numberAdded} já existe.")
        else:
            userListStars.append(numberAdded)

#obs: não foi utilizado 'not in' nas duas funções abaixo pois não tinha certeza se contava como função built in. Então fiz cada função de uma maneira, para prática.

#adição de números na lista aleatória
while (len(listNumbers) < 5):
    randomNumber = generateRandomNumber(1, 50)
    if(randomNumber not in listNumbers):
        listNumbers.append(randomNumber)

#adição de números na lista aleatória
while (len(listStars) < 2):
    randomNumber = generateRandomNumber(1,12)
    if(isUniqueNumber(listStars, randomNumber)):
        listStars.append(randomNumber)

###comparação das listas###
def compareLists(list1, list2):
    count = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                count += 1 
    return count
     
#main - chamada de funções
requestLotteryGameToUser()
requestNumberStarsToUser()

#verificação do numero de acertos e atribuição desses valores a variáveis
numberMatches = compareLists(listNumbers, userListNumbers) 
starsMatches = compareLists(listStars, userListStars) 

#listas sorteadas
print(f"Lista de Números Sorteados: {listNumbers}")
print(f"Lista de Estrelas Sorteadas{listStars}")
#quantidade de acertos em números e estrelas da euromilhoes
print(f"Quantidade de acerto de números: {numberMatches}") 
print(f"Quantidade de acerto de estrelas: {starsMatches}") 

#atribuição de premios (fonte: https://pt.wikipedia.org/wiki/Euromilhões)
if numberMatches == 5 and starsMatches == 2:
    print("Premio: 17.000.000€")
elif numberMatches == 5 and starsMatches == 1:
    print("Premio: 200.738€")
elif numberMatches == 5 and starsMatches == 0:
    print("Premio: 20.851€")
elif numberMatches == 4 and starsMatches == 2:
    print("Premio: 1299€")
elif numberMatches == 4 and starsMatches == 2:
    print("Premio: 120€")
elif numberMatches == 3 and starsMatches == 2:
    print("Premio: 57€")
elif numberMatches == 4 and starsMatches == 0:
    print("Premio: 39€")
elif numberMatches == 2 and starsMatches == 2:
    print("Premio: 14€")
elif numberMatches == 3 and starsMatches == 1:
    print("Premio: 11€")
elif numberMatches == 3 and starsMatches == 0:
    print("Premio: 9€")
elif numberMatches == 1 and starsMatches == 2:
    print("Premio: 7€")
elif numberMatches == 2 and starsMatches == 1:
    print("Premio: 6€")
elif numberMatches == 2 and starsMatches == 0:
    print("Premio: 4€")
else:
    print("Não ganhou prêmio")