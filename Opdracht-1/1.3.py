## Weegschaal
def weegschaal(lijst):
    Schaal_A = []
    Schaal_B = []
    a_totaal = 0
    b_totaal = 0

    ##Sorteer van groot naar klein
    lijst.sort(reverse=True)
    print(lijst)

    for i in lijst:
        if a_totaal >= b_totaal:
            Schaal_B.append(i)
        else:
            Schaal_A.append(i)

        ##Get new total
        a_totaal = sum(Schaal_A)
        b_totaal = sum(Schaal_B)

    print('A = ', a_totaal, ' = ', Schaal_A)
    print('B = ', b_totaal, ' = ', Schaal_B)

gewichten = [20, 45, 23, 75, 13, 45, 52, 33, 35, 28]
weegschaal(gewichten)