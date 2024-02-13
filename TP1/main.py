import sys
from atleta import Atleta


def main():
    athletes = []
    sys.stdin.readline()
    for line in sys.stdin:
        athletes.append(newAthlete(line))
    sortedModalidades = getModalidades(athletes)
    apt,inapt = getAptInapt(athletes)
    agesDict = distributeAgeRange(athletes)

    for m in sortedModalidades:
        print(m)
    
    print(f"\nAptos: {apt}%\nInaptos: {inapt}%\n")

    for key,value in agesDict.items():
        print(f"{key}-{key+4}: {value}")



def newAthlete(line) -> Atleta:
    line_iter = iter(line.split(","))
    return Atleta(next(line_iter),int(next(line_iter)),next(line_iter),next(line_iter),next(line_iter),int(next(line_iter)),next(line_iter),next(line_iter),next(line_iter),next(line_iter),next(line_iter),next(line_iter) == "true",next(line_iter).rstrip() == "true")

def getModalidades(athletes):
    modalidades_set = set()
    for athlete in athletes:
        modalidades_set.add(athlete.modalidade) 
    return sorted(list(modalidades_set),key=str.lower)

def getAptInapt(athletes):
    apt,inapt = 0,0
    for athlete in athletes:
        if (athlete.resultado):
            apt += 1
        else:
            inapt += 1
    return (apt*100)/len(athletes),(inapt*100)/len(athletes)

def distributeAgeRange(athletes):
    agesDict = {}
    minAge, maxAge = 200,0
    for a in athletes:
        if a.idade < minAge:
            minAge = a.idade
        if a.idade > maxAge:
            maxAge = a.idade
    
    curr_lowest_group = minAge - (minAge % 5)
    highest_group = maxAge - (maxAge % 5)
    while curr_lowest_group <= highest_group:
        agesDict[curr_lowest_group] = 0
        curr_lowest_group += 5 # próximo mínimo de um intervalo

    for athlete in athletes:
        agesDict[athlete.idade - (athlete.idade % 5)] += 1

    return agesDict

if __name__ == "__main__":
    main()