from multiprocessing import context
from flask import Flask, render_template, request, flash
from decimal import Decimal, getcontext

# Define a precisão global
getcontext().prec = 10

app = Flask(__name__)
app.secret_key = "dev"

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
    #Valores inicias (para mostrar na tela se necessário)
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
            # Inputs brutos
            campos = ["EscolaM", "EscolaP", "Alunos1", "Aprov1", "Alunos2", "Aprov2", "Alunos3", "Aprov3"]
            valores = {}

            # Verifica se os números estão válidos
            for campo in campos:
                entrada = request.form[campo].strip()
                if not entrada.replace('.', '', 1).isdigit():
                    flash(f"O campo '{campo}' deve conter apenas números válidos.")
                    return render_template('index.html', **contexto)
                valores[campo] = Decimal(entrada)

            # Extrai os valores convertidos
            EscolaM = valores["EscolaM"]
            EscolaP = valores["EscolaP"]
            Alunos1 = valores["Alunos1"]
            Aprov1 = valores["Aprov1"]
            Alunos2 = valores["Alunos2"]
            Aprov2 = valores["Aprov2"]
            Alunos3 = valores["Alunos3"]
            Aprov3 = valores["Aprov3"]
            
            #Validação de valores não negativos
            if any(val < 0 for val in valores.values()):
                flash("Valores não podem ser negativos. Tente novamente.")
                return render_template('index.html', **contexto)

            #Validação de que os aprovados não podem possuir um valor maior que os alunos
            if Aprov1 > Alunos1 or Aprov2 > Alunos2 or Aprov3 > Alunos3:
                flash("O número de aprovados não pode ser maior que o número de alunos.")
                return render_template('index.html', **context)
                valores[campo] = Decimal(entrada)


        #Se for GET, só mostra o formulário
        except Exception as e:
            flash(f"Erro inesperado: {str(e)}")
            return render_template('index.html', **contexto)

    return render_template("index.html", **contexto)

if __name__ == '__main__':
    app.run(debug=True)