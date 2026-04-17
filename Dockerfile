# Imagem base leve e estável
FROM python:3.12-slim

# Evita criação de arquivos .pyc e força flush de logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema necessárias para pandas, numpy e requests
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório da aplicação
WORKDIR /app

# Copia requirements primeiro (melhor cache)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Cria diretórios de dados (caso não existam)
RUN mkdir -p data/raw data/processed data/output

# Comando padrão (pode ser sobrescrito)
CMD ["python", "-c", "print('Container pronto!')"]
