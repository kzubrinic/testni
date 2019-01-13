# Program računa ispisuje prosjek unesenih ocjena
# Pronađite i ispravite sintaksne greške
br_stud = int(input('Broj studenata: '))

suma = 0
for i in range(1, br_stud+1):
    ocj = int(input('Ocjena: '))
    suma = suma + ocj
print('Prosjek ocjena: ', suma/br_stud) 

