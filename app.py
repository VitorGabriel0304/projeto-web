from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return  render_template('index.html')


@app.route('/sobre')
def sobre ():
    return  render_template ('sobre.html')

@app.route('/boostrap')
def ver_algo ():
    return  render_template ('boostrap.html')


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




