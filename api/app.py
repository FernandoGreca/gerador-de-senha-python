from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        quant = int(request.form['name'])
        return gerar(quant)
    except ValueError:
        erro = "INFORME UM VALOR VALIDO!!"
        return render_template("index.html", erro=erro)
    
def gerar(quant):
    vet = [0 for x in range(quant)]

    caracteres_evitar = [34, 39, 40, 44, 46, 41, 47, 58, 91, 92, 93, 94, 96]

    for i in range(quant):
        vet[i] = random.randint(33, 122)
        while vet[i] in caracteres_evitar:
            vet[i] = random.randint(33, 122)
        vet[i] = chr(vet[i])

    vet = "".join(vet)
    
    return render_template("index.html", msg=vet)

if __name__ == '__main__':
    app.run(debug=True)






