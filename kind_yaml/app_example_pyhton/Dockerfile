# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o container
COPY app.py /app

# Instala as dependências necessárias
RUN pip install flask

# Expõe a porta 8080 para o Kubernetes acessar
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "app.py"]