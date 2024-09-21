from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from authlib.integrations.flask_client import OAuth
from main import oauthRegister, User
from datetime import date
import jinja2

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)
oauthRegister(oauth, 
              name = "suap", 
              api_base_url="https://suap.ifrn.edu.br/api/", 
              request_token_url=None, 
              access_token_method="POST", 
              access_token_url="https://suap.ifrn.edu.br/o/token/", 
              authorize_url="https://suap.ifrn.edu.br/o/authorize/", token="suap_token")

# Manipulador de erro para UndefinedError
@app.errorhandler(jinja2.exceptions.UndefinedError)
def handle_jinja2_error(e):
    # Aqui você pode enviar a exceção para log ou para um sistema de monitoramento
    return render_template('500.html', error=str(e)), 500

@app.route('/')
def index():
    if 'suap_token' in session:
        user = User(oauth)
        user_data = user.get_user_dados()
        print(user_data.json())
        data = {"user_data": user_data.json()}
        return render_template('user.html', data=data)
    else:
        return render_template('index.html')
    
@app.route("/boletim", methods=["GET"])
def boletim():
    user = User(oauth)

    user_data = user.get_user_dados()
    anos_letivos = user.get_user_anos_letivos()
    data = {
        "user_data": user_data.json(),
        "anos_letivos": anos_letivos.json(),
    }
    if (request.args.get('ano_letivo')):
        try:
            ano_letivo, periodo_letivo = str(request.args.get('ano_letivo')).split(".")  
            boletim = user.get_user_boletim(ano_letivo, periodo_letivo)
            data["boletim"] = boletim.json()                                            
            data["ano_selecionado"] = str(request.args.get('ano_letivo'))
        
        except jinja2.exceptions.UndefinedError as e:
            handle_jinja2_error(e)
        
    return render_template("boletim.html", data=data)

   

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)


@app.route('/logout')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))


@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
    
    