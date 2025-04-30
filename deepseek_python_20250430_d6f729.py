from flask import Flask  # <-- ATENÇÃO: "Flask" com F maiúsculo!

app = Flask(__name__)

@app.route('/')  # <-- Corrigido: era "drop.route"
def home():
    return "Sistema de Vendas Online!"  # <-- Corrigido: era "Wendas"

if __name__ == '__main__':
    app.run()