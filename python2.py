#luodaan lista tilitapahtumista
tilitapahtumat = []
#ja lista sallituista operaattoreista
sallitutOperaattorit = set(['o','p','O','P'])

def Task2Function():
    saldo = 0
    while True:
        userInput = input("Anna toiminto: ")
        toimitus = userInput[0:1]
        summa = userInput[1:]
        print("Antamasi toiminto: "+toimitus + " "+ summa)
        if toimitus in sallitutOperaattorit:
            if toimitus is 'p':
                saldo += int(summa)
                tilitapahtumat.append(str(toimitus)+" "+str(summa))
            if toimitus is 'o':
                saldo -= int(summa)
                tilitapahtumat.append(str(toimitus)+" "+str(summa))
        else:
            print("Antamasi toiminto on virheellinen")

        print("Saldo: "+str(saldo)+"\nTilitapahtumat: "+str(tilitapahtumat))
        print("\n***********************************\n")

if __name__== "__main__":

    Task2Function()
