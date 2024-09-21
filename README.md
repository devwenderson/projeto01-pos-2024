# Grupo
- Wenderson da Silva
- Izac do Nascimento

# Instalação  
--- 

- Crie um ambiente virtual
```bash
py -m venv venv
```

- Abra o ambiente virtual

_powershell_
```bash
.\venv\Scripts\Activate.ps1
```

_bash_
```bash
source venv/Scripts/activate
```

- Instale as dependências
```bash
pip install -r requirements.txt
```

- Crie um arquivo _.env_ e coloque os dados abaixo
```bash
CLIENT_ID=<seu client_id>
CLIENT_SECRET=<seu client_secret>
```

- Rode o servidor
```bash
flask --app app.py --debug run
```
