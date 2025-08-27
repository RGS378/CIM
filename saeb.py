from decimal import Decimal, getcontext

# Define a precisão global 
getcontext().prec = 10

# Entradas com Decimal
MediaM = Decimal('288.7')
MediaP = Decimal('283.9')

DPm = Decimal('59')
DPp = Decimal('56')

SinfM = MediaM - Decimal('3') * DPm
SinfP = MediaP - Decimal('3') * DPp

SsupM = MediaM + Decimal('3') * DPm
SsupP = MediaP + Decimal('3') * DPp

print('==== SOBRE SUAS NOTAS ====')
print(f'Sua menor nota em Matemática é: {SinfM}')
print(f'Sua menor nota em Português é: {SinfP}')
print(f'Sua maior nota em Matemática é: {SsupM}')
print(f'Sua maior nota em Português é: {SsupP}')

MediaExM = SsupM - SinfM
MediaExP = SsupP - SinfP

print('==== SOBRE SUAS MÉDIAS ====')
print(f'A média extrema de Matemática é {MediaExM}')
print(f'A média extrema de Português é {MediaExP}')

print('==== SOBRE A ESCOLA ====')
escolam = Decimal(input('Nota média da escola em matemática é: '))
escolap = Decimal(input('Nota média da escola em português é: '))

ProficienciaP = ((escolap - SinfP) / MediaExP) * Decimal('10')
ProficienciaM = ((escolam - SinfM) / MediaExM) * Decimal('10')

print(f'A proficiência de Matemática é {ProficienciaM} e a de Português é {ProficienciaP}')

MediaTotal = (ProficienciaM + ProficienciaP) / Decimal('2')
print(f'A média total é {MediaTotal}')

print('==== SOBRE A APROVAÇÃO ====')
Alunos1 = Decimal(input('Quantos alunos tem na 1ª série? '))
Alunos2 = Decimal(input('Quantos alunos tem na 2ª série? '))
Alunos3 = Decimal(input('Quantos alunos tem na 3ª série? '))

Aprovados1 = Decimal(input('Quantos alunos aprovados na 1ª série? '))
Aprovados2 = Decimal(input('Quantos alunos aprovados na 2ª série? '))
Aprovados3 = Decimal(input('Quantos alunos aprovados na 3ª série? '))

TaxaDeAprovacao1 = Aprovados1 / Alunos1
TaxaDeAprovacao2 = Aprovados2 / Alunos2
TaxaDeAprovacao3 = Aprovados3 / Alunos3

print(f'Taxa de aprovação da 1ª série: {TaxaDeAprovacao1}')
print(f'Taxa de aprovação da 2ª série: {TaxaDeAprovacao2}')
print(f'Taxa de aprovação da 3ª série: {TaxaDeAprovacao3}')

Aprovacao1 = Decimal('1') / TaxaDeAprovacao1
Aprovacao2 = Decimal('1') / TaxaDeAprovacao2
Aprovacao3 = Decimal('1') / TaxaDeAprovacao3

print(f'Aprovação da 1ª série é {Aprovacao1}, 2ª série é {Aprovacao2}, 3ª série é {Aprovacao3}')
Total = Aprovacao1 + Aprovacao2 + Aprovacao3

print(f'O total de aprovado é {Total}')

Tempo = Total / Decimal('3')
print(f'O tempo de aprovado é {Tempo}')

Padronizado = Decimal('1') / Tempo
print(f'O padronizado é {Padronizado * Decimal("100"):.2f}%')

IDEB = MediaTotal * Padronizado
print(f'A nota da IDEB é {IDEB}')
