# Utilize uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências do sistema necessárias para compilar mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo requirements.txt para a imagem
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para a imagem
COPY . .

# Defina o comando de inicialização
CMD ["gunicorn", "--bind", "0.0.0.0:3306", "proj_workshop_fabrica.wsgi:application"]
