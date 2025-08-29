from decimal import Decimal, getcontext

# Define a precisão global 
getcontext().prec = 10

# Função para validar entradas não negativas
def entrada_decimal_positiva(mensagem):
    while True:
        try:
            valor = Decimal(input(mensagem))
            if valor < 0:
                print("Valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except:
            print("Entrada inválida. Digite um número válido.")

# Entradas fixas
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
escolam = entrada_decimal_positiva('Nota média da escola em matemática é: ')
escolap = entrada_decimal_positiva('Nota média da escola em português é: ')

ProficienciaP = ((escolap - SinfP) / MediaExP) * Decimal('10')
ProficienciaM = ((escolam - SinfM) / MediaExM) * Decimal('10')

print(f'A proficiência de Matemática é {ProficienciaM} e a de Português é {ProficienciaP}')

MediaTotal = (ProficienciaM + ProficienciaP) / Decimal('2')
print(f'A média total é {MediaTotal}')

print('==== SOBRE A APROVAÇÃO ====')
Alunos1 = entrada_decimal_positiva('Quantos alunos tem na 1ª série? ')
Alunos2 = entrada_decimal_positiva('Quantos alunos tem na 2ª série? ')
Alunos3 = entrada_decimal_positiva('Quantos alunos tem na 3ª série? ')

Aprovados1 = entrada_decimal_positiva('Quantos alunos aprovados na 1ª série? ')
Aprovados2 = entrada_decimal_positiva('Quantos alunos aprovados na 2ª série? ')
Aprovados3 = entrada_decimal_positiva('Quantos alunos aprovados na 3ª série? ')

TaxaDeAprovacao1 = Aprovados1 / Alunos1 if Alunos1 > 0 else Decimal('0')
TaxaDeAprovacao2 = Aprovados2 / Alunos2 if Alunos2 > 0 else Decimal('0')
TaxaDeAprovacao3 = Aprovados3 / Alunos3 if Alunos3 > 0 else Decimal('0')

print(f'Taxa de aprovação da 1ª série: {TaxaDeAprovacao1}')
print(f'Taxa de aprovação da 2ª série: {TaxaDeAprovacao2}')
print(f'Taxa de aprovação da 3ª série: {TaxaDeAprovacao3}')

Aprovacao1 = Decimal('1') / TaxaDeAprovacao1 if TaxaDeAprovacao1 > 0 else Decimal('0')
Aprovacao2 = Decimal('1') / TaxaDeAprovacao2 if TaxaDeAprovacao2 > 0 else Decimal('0')
Aprovacao3 = Decimal('1') / TaxaDeAprovacao3 if TaxaDeAprovacao3 > 0 else Decimal('0')

print(f'Aprovação da 1ª série é {Aprovacao1}, 2ª série é {Aprovacao2}, 3ª série é {Aprovacao3}')
Total = Aprovacao1 + Aprovacao2 + Aprovacao3

print(f'O total de aprovado é {Total}')

Tempo = Total / Decimal('3') if Total > 0 else Decimal('0')
print(f'O tempo de aprovado é {Tempo}')

Padronizado = Decimal('1') / Tempo if Tempo > 0 else Decimal('0')
print(f'O padronizado é {Padronizado * Decimal("100"):.2f}%')

IDEB = MediaTotal * Padronizado
print(f'A nota da IDEB é {IDEB}')
