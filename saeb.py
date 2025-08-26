MediaM = float(input('Nota de matemática: '))
MediaP = float(input('Nota de Português: '))

DPm = 59
DPp = 56

SinfM = MediaM - 3 * (DPm)
SinfP = MediaP - 3 * (DPp)

SsupM = MediaM + 3 * (DPm)
SsupP = MediaP + 3 * (DPp)

print('==== SOBRE SUAS NOTAS ====')
print('Sua menor nota em Matemática é: {} '.format(SinfM))
print('Sua menor nota em Português é: {} '.format(SinfP))
print('Sua maior nota em Matemática é: {} '.format(SsupM))
print('Sua maior nota em Português é: {} '.format(SsupP))

MediaExM = SsupM - SinfM
MediaExP = SsupP - SinfP

print('==== SOBRE SUAS MÉDIAS ====')
print('A media extrema de Matematica é {}'.format(MediaExM))
print('A media extrema de Português é {}'.format(MediaExP))

print('==== SOBRE A ESCOLA ====')
EscolaM = float(input('Nota média da escola em matématica é: '))
EscolaP = float(input('Nota média da escola em português é: '))

ProficienciaP = ((EscolaP - SinfP) / MediaExP) * 10
ProficienciaM = ((EscolaM - SinfM) / MediaExM) * 10

print('A proficiência de Matematica é {} e a de Português é {} '.format(ProficienciaM, ProficienciaP))

MediaTotal = (ProficienciaM + ProficienciaP) / 2

print('A media total é {}'.format(MediaTotal))

print('==== SOBRE A APROVAÇÃO ====')
Alunos1 = float(input('Quantos alunos tem na 1 série? '))
Alunos2 = float(input('Quantos alunos tem na 2 série? '))
Alunos3 = float(input('Quantos alunos tem na 3 série? '))

Aprovados1 = float(input('Quantos alunos aprovados na 1ª série? '))
Aprovados2 = float(input('Quantos alunos aprovados na 2ª série? '))
Aprovados3 = float(input('Quantos alunos aprovados na 3ª série? '))

TaxaDeAprovacao1 = Aprovados1 / Alunos1
TaxaDeAprovacao2 = Aprovados2 / Alunos2
TaxaDeAprovacao3 = Aprovados3 / Alunos3


print('Taxa de aprovação da 1ª série:', TaxaDeAprovacao1)
print('Taxa de aprovação da 2ª série:', TaxaDeAprovacao2)
print('Taxa de aprovação da 3ª série:', TaxaDeAprovacao3)

Aprovacao1 = 1/TaxaDeAprovacao1
Aprovacao2 = 1/TaxaDeAprovacao2
Aprovacao3 = 1/TaxaDeAprovacao3

print('Aprovaçaõ do 1 série é {}, 2 série é {}, 3 série é {}. '.format(Aprovacao1, Aprovacao2, Aprovacao3))
Total = Aprovacao1 + Aprovacao2 + Aprovacao3

print('O total de aprovado {}'.format(Total))

Tempo = Total/3
print('O tempo de aprovado {}'.format(Tempo))

Padronizado = 1/Tempo
print('O padronizado {}'.format(Padronizado))

IDEB = MediaTotal * Padronizado
print('A nota da IDEB é {}'.format(IDEB))
