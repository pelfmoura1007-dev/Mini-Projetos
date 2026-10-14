# Mini sistema de notas de estudantes

print('Bem-vindo ao sistema de notas de estudantes!')

Nota1 = float(input('Digite a primeira nota: '))

if Nota1 < 0 or Nota1 > 100:
    print('Nota inválida! Digite uma nota entre 0 e 100.')
elif Nota1 >= 80:
    print('O aluno está aprovado e foi aluno destaque no bimestre!')
elif Nota1 >= 70:
    print('O aluno está aprovado!')
else:
    print('O aluno está de recuperação!')


Nota2 = float(input('Digite a segunda nota: '))

if Nota2 < 0 or Nota2 > 100:
    print('Nota inválida! Digite uma nota entre 0 e 100.')
elif Nota2 >= 80:
    print('O aluno está aprovado e foi aluno destaque no bimestre!')
elif Nota2 >= 70:
    print('O aluno está aprovado!')
else:
    print('O aluno está de recuperação!')


Nota3 = float(input('Digite a terceira nota: '))

if Nota3 < 0 or Nota3 > 100:
    print('Nota inválida! Digite uma nota entre 0 e 100.')
elif Nota3 >= 80:
    print('O aluno está aprovado e foi aluno destaque no bimestre!')
elif Nota3 >= 70:
    print('O aluno está aprovado!')
else:
    print('O aluno está de recuperação!')


Nota4 = float(input('Digite a quarta nota: '))

if Nota4 < 0 or Nota4 > 100:
    print('Nota inválida! Digite uma nota entre 0 e 100.')
elif Nota4 >= 80:
    print('O aluno está aprovado e foi aluno destaque no bimestre!')
elif Nota4 >= 70:
    print('O aluno está aprovado!')
else:
    print('O aluno está de recuperação!')


Media = (Nota1 + Nota2 + Nota3 + Nota4) / 4

print(f'A média final do aluno é: {Media:.2f}')

if Media >= 80:
    print('O aluno foi destaque no ano!')
elif Media >= 70:
    print('O aluno foi aprovado no ano!')
else:
    print('O aluno foi reprovado no ano!')