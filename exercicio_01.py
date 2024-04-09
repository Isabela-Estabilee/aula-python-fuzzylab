idade = int(input('Digite a sua idade: '))

if idade < 12 :
    print('Criança')
elif idade >= 12 and idade < 18 :
    print('Adolescente')
elif idade >= 18 and idade < 60 :
    print('Adulto')
else :
    print('Idoso')