#Vamos criar um dicionário com duas chaces e tentar retornar seus dados pela rota
dicionario = {
    "nome": "Otavio",
    "nascimento":1991
}


#importar flask
from flask import Flask
#Criar a aplicação flask
app = Flask(__name__)

# a rota abaixo retorna uma função que retorna um dicionario
@app.route("/teste")
def mostra_dicionario():
    return dicionario

@app.route("/")
def dados_usuario():
    return f"<b>O usuário {dicionario['nome']} nasceu em {dicionario['nascimento']}</b>"

#Colocar a aplicação para Rodar
app.run(debug=True)