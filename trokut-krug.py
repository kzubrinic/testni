# Program računa i ispisuje opseg i površinu trokuta ili kruga
lik = input('Lik (T/K): ')
str_pol = int(input('Stranica/polumjer: '))
              
if lik == 'T':
    ops = 3 * str_pol
    pov = 1.73 * str_pol ** 2 / 4
    lik_tekst = 'trokuta'
else:
    ops = 2 * str_pol * 3.14
    pov = str_pol ** 2 * 3.14
    lik_tekst = 'kruga'

print('Opseg',lik_tekst,'je',ops,', a površina',pov )
