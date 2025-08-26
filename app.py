from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "dev"  

DPm, DPp = 59, 56  # constantes

@app.route("/", methods=["GET", "POST"])
def index():
    contexto = {}
    if request.method == "POST":
        try:
            # Inputs
            EscolaM  = float(request.form["EscolaM"])
            EscolaP  = float(request.form["EscolaP"])
            Alunos1  = float(request.form["Alunos1"])
            Aprov1   = float(request.form["Aprov1"])
            Alunos2  = float(request.form["Alunos2"])
            Aprov2   = float(request.form["Aprov2"])
            Alunos3  = float(request.form["Alunos3"])
            Aprov3   = float(request.form["Aprov3"])

            # Notas
            SinfM = 111.70
            SinfP = 115.90
            SsupM = 465.70
            SsupP = 451.90
            MediaExM = SsupM - SinfM
            MediaExP = SsupP - SinfP

            # Proficiências
            ProficM = ((EscolaM - SinfM) / MediaExM) * 10 if MediaExM != 0 else float("nan")
            ProficP = ((EscolaP - SinfP) / MediaExP) * 10 if MediaExP != 0 else float("nan")
            MediaTotal = (ProficM + ProficP) / 2

            # Aprovação (com checagem pra evitar divisão por zero)
            Tx1 = Aprov1 / Alunos1 if Alunos1 else float("nan")
            Tx2 = Aprov2 / Alunos2 if Alunos2 else float("nan")
            Tx3 = Aprov3 / Alunos3 if Alunos3 else float("nan")

            Ap1 = 1 / Tx1 if Tx1 not in (0, float("nan")) else float("nan")
            Ap2 = 1 / Tx2 if Tx2 not in (0, float("nan")) else float("nan")
            Ap3 = 1 / Tx3 if Tx3 not in (0, float("nan")) else float("nan")

            Total = Ap1 + Ap2 + Ap3
            Tempo = Total / 3
            Padronizado = 1 / Tempo if Tempo not in (0, float("nan")) else float("nan")

            IDEB = MediaTotal * Padronizado

            # Atualizando o contexto com os resultados
            contexto.update(dict(
                SinfM=SinfM, SinfP=SinfP, SsupM=SsupM, SsupP=SsupP,
                MediaExM=MediaExM, MediaExP=MediaExP,
                ProficM=ProficM, ProficP=ProficP, MediaTotal=MediaTotal,
                Tx1=Tx1, Tx2=Tx2, Tx3=Tx3,
                Ap1=Ap1, Ap2=Ap2, Ap3=Ap3,
                Total=Total, Tempo=Tempo, Padronizado=Padronizado, IDEB=IDEB,
                enviado=True
            ))
        except ValueError:
            flash("Preencha todos os campos corretamente (números).")
            return render_template('index.html') 

    return render_template('index.html', **contexto) 


if __name__ == '__main__':
    app.run(debug=True)
