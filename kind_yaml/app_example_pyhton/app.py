from flask import Flask

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração do endpoint /pydatadog
@app.route('/pydatadog', methods=['GET'])
def pydatadog():
    app.logger.info("Hello, World!")  # Loga "Hello, World!" no console
    return {"message": "Log registrado com sucesso!"}, 200

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)  # Porta ajustada para 8080