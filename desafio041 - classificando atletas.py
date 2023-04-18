from datetime import date
birth = int(input('Digite o ano de nascimento do atleta: '))
age = date.today().year - birth

if age <= 9:
    print(f'idade: {age} anos. O atleta se encaixa na categoria MIRIM.')
elif age > 9 and age <=14:
    print(f'Idade: {age} anos. O atleta se encaixa na categoria INFANTIL.')
elif age > 14 and age <= 19:
    print(f'Idade: {age} anos. O atleta se encaixa na categoria JUNIOR.')
elif age > 19 and age <= 20:
    print(f'Idade: {age} anos. O atleta se encaixa na categoria SENIOR.')
else:
    print(f'Idade: {age} anos. O atleta se encaixa na categoria MASTER.')
    