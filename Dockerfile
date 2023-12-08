# Definir a imagem base
FROM python:3

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários para o contêiner Docker
COPY . .

# Instalar as dependências necessárias
RUN pip install requests pandas python-bcb

# Definir o comando para executar o aplicativo
CMD ["python", "main.py"]