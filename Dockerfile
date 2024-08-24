# Usando uma imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo de requisitos
COPY requirements.txt .

# Instalando as dependências
RUN pip install -r requirements.txt

# Copiando o código do projeto
COPY . .

# Expondo a porta do servidor
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
