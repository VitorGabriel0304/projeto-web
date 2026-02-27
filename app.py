from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return  '<h1>Ola python</h1>'


@app.route('/sobre')
def sobre ():
    return '''
<h1>pagina em Flask</h1>
<p>Desenvolvida por <b>Vitor</b) </p>
'''
@app.route('/sobre/fatec')
def sobre_fatec ():
    return '''
<h1>pagina em sobre a FATEC</h1>
<p>Desenvolvida na <b>FATEC</b) </p>
'''
@app.route ('/cor/<cor1>')
def exibe_cor(cor1):
    return f'<h1 style="color:{cor1}">A cor escolhida foi: {cor1}</h1>'



if __name__ == '__main__':
    app.run(debug=True)
