from flask import Flask, render_template, request, flash, os
from decimal import Decimal, getcontext

# Define a precisão global
getcontext().prec = 10

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Constantes
MediaM = Decimal('288.7')
MediaP = Decimal('283.9')
DPm = Decimal('59')
DPp = Decimal('56')

SinfM = MediaM - Decimal('3') * DPm
SinfP = MediaP - Decimal('3') * DPp
SsupM = MediaM + Decimal('3') * DPm
SsupP = MediaP + Decimal('3') * DPp

MediaExM = SsupM - SinfM
MediaExP = SsupP - SinfP


@app.route("/", methods=["GET", "POST"])
def index():
    contexto = {
        'SinfM': float(SinfM),
        'SinfP': float(SinfP),
        'SsupM': float(SsupM),
        'SsupP': float(SsupP),
        'MediaExM': float(MediaExM),
        'MediaExP': float(MediaExP)
    }

    if request.method == "POST":
        try:
            campos = ["EscolaM", "EscolaP", "Alunos1", "Aprov1", "Alunos2", "Aprov2", "Alunos3", "Aprov3"]
            valores = {}

            for campo in campos:
                entrada = request.form[campo].strip()
                if not entrada.replace('.', '', 1).isdigit():
                    flash(f"O campo '{campo}' deve conter apenas números válidos.")
                    return render_template('index.html', **contexto)
                valores[campo] = Decimal(entrada)

            EscolaM = valores["EscolaM"]
            EscolaP = valores["EscolaP"]
            Alunos1, Aprov1 = valores["Alunos1"], valores["Aprov1"]
            Alunos2, Aprov2 = valores["Alunos2"], valores["Aprov2"]
            Alunos3, Aprov3 = valores["Alunos3"], valores["Aprov3"]

            # Proficiencias
            ProficM = ((EscolaM - SinfM) / MediaExM) * Decimal('10') if MediaExM != 0 else Decimal('0')
            ProficP = ((EscolaP - SinfP) / MediaExP) * Decimal('10') if MediaExP != 0 else Decimal('0')
            MediaTotal = (ProficM + ProficP) / Decimal('2')

            # Taxas de aprovação
            Tx1 = Aprov1 / Alunos1 if Alunos1 > 0 else Decimal('0')
            Tx2 = Aprov2 / Alunos2 if Alunos2 > 0 else Decimal('0')
            Tx3 = Aprov3 / Alunos3 if Alunos3 > 0 else Decimal('0')

            Ap1 = Decimal('1') / Tx1 if Tx1 > 0 else Decimal('0')
            Ap2 = Decimal('1') / Tx2 if Tx2 > 0 else Decimal('0')
            Ap3 = Decimal('1') / Tx3 if Tx3 > 0 else Decimal('0')

            Total = Ap1 + Ap2 + Ap3
            Tempo = Total / Decimal('3') if Total > 0 else Decimal('0')
            Padronizado = Decimal('1') / Tempo if Tempo > 0 else Decimal('0')

            IDEB = MediaTotal * Padronizado

            contexto.update(dict(
                ProficM=float(ProficM),
                ProficP=float(ProficP),
                MediaTotal=float(MediaTotal),
                Tx1=float(Tx1),
                Tx2=float(Tx2),
                Tx3=float(Tx3),
                Ap1=float(Ap1),
                Ap2=float(Ap2),
                Ap3=float(Ap3),
                Total=float(Total),
                Tempo=float(Tempo),
                Padronizado=float(Padronizado * Decimal('100')),
                IDEB=float(IDEB),
                enviado=True
            ))

            # validações
            if any(val < 0 for val in valores.values()):
                flash("Valores não podem ser negativos. Tente novamente.")
                return render_template('index.html', **contexto)

            if Aprov1 > Alunos1 or Aprov2 > Alunos2 or Aprov3 > Alunos3:
                flash("O número de aprovados não pode ser maior que o número de alunos.")
                return render_template('index.html', **contexto)

            return render_template("result.html", **contexto)

        except Exception as e:
            flash(f"Erro inesperado: {str(e)}")
            return render_template('index.html', **contexto)

    return render_template("index.html", **contexto)


if __name__ == '__main__':
    app.run()
