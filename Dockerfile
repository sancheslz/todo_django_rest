# Define a imagem do projeto
FROM python:3.11-slim

# Define variáveis de ambinete (python)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG PROJECT_NAME
ARG PORT

# Define o nome do projeto
ENV PROJECT_NAME=$PROJECT_NAME
ENV PORT=$PORT

# Faz as instalações necessárias
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Define a pasta do projeto
WORKDIR /app/$PROJECT_NAME

# Copia todos os arquivos da pasta atual para o container
COPY . .

# Expõe a porta 8000
EXPOSE $PORT

# Define configurações de inicialização
ENTRYPOINT [ "./entrypoint.sh" ]
