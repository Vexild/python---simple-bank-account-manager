import requests
import json
def Task4Function(cityname):

    print("Kysymys: Kuinka monta osakeyhtiötä on rekisteröity paikkakunnalla: "+cityname+" 14.03.1978 jälkeen?")

    #haetan firmojen määrä
    urlForCompanies = 'https://avoindata.prh.fi/bis/v1?totalResults=true&maxResults=1000&resultsFrom=0&registeredOffice='+cityname+'&companyForm=OY&companyRegistrationFrom=1978-03-14'
    listOfCompanies = requests.get(urlForCompanies).json()
    length_of_companies = listOfCompanies["totalResults"]

    print("Osakeyhtiöitä yhteensä: \n"+str(length_of_companies))

    print("\nKuinka moni näistä on lopettanu toimintansa syystä \
tai toisesta?\n")

    #lopettaneiden firmojen määrän muuttuja
    dismissedCompanyCount = 0

    #firmojen businesId
    companyIDs = []

    #lista firmoista joita seulotaan lopettaneet
    dataOfCompanies = []

    #haetaan kaikki companyIDt ja asetetaan ne listaan
    for i in range(0,length_of_companies):
        companyID = listOfCompanies["results"][i]["businessId"]
        companyIDs.append(companyID)

    #haettavien urlien lista
    listOfUrl = []

    #luodaan osoitelista
    for i in range(0,length_of_companies):
        endDateCheckUrl = 'https://avoindata.prh.fi/bis/v1/'+companyIDs[i]
        listOfUrl.append(str(endDateCheckUrl))


    print("Osoitelista luotu! Seuraavana haetaan näistä osoitteista dataa\nTämä voi kestää hetken\n")
    for i in range(0,len(listOfUrl)):
        endDateCheck = requests.get(str(listOfUrl[i])).json()
        dataOfCompanies.append(endDateCheck)

    print("Data haettu ja asetettu listaan. Seuraavana haetaan näistä lista itemeistä \
dataa 'endDate' avaimesta. Jos päivämäärä löytyy niin merkataan se ylös\n")

    #käydään läpi datalistasta "endDate" avaimet
    for i in range(0,len(dataOfCompanies)):
        hasCompanyEndDate = dataOfCompanies[i]
        endDate = endDateCheck["results"][0]["registeredEntries"][0]["endDate"]
        #jos päivämäärä löytyy niin merkataan se ylös
        if endDate is not None:
            dismissedCompanyCount += 1

    print("Lopettaneita yhteensä paikkakunnalla "+cityname+": \n"+ str(dismissedCompanyCount)+"\n")
    print("\n***********************************************")
    print("\n")

if __name__== "__main__":
    Task4Function('Ylitornio')
    Task4Function('Merikarvia')
    Task4Function('Parikkala')
