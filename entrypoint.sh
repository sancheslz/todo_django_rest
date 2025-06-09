#! /bin/bash

# Interrompe o script em caso de erros
set -e

PROJECT_NAME=${PROJECT_NAME:-core}
PORT=${PORT:-8000}


if [ ! -f requirements.txt ]; then
    echo "O arquivo 'requirements.txt' não foi encontrado."
    echo "Seguindo configurações padrão"
    echo "1. Criando o arquivo requirements.txt"
    cat << EOF > requirements.txt
django
djangorestframework
django-cors-headers
pytest
pytest-django
factory_boy
faker
EOF
else
    echo "1. Arquivo requirements.txt encontrado"
fi

echo "2. Instalando dependências"
pip install -r requirements.txt

if [ ! -f "manage.py" ]; then
    django-admin startproject "$PROJECT_NAME" .
    ls -l
fi


echo "Verificando argumentos... "
if [ -z "$1" ]; then
    echo -e "3. Carregando servidor"
    exec python manage.py runserver 0.0.0.0:$PORT
else
    echo "3. Execundo o comando $@"
    exec "$@"
fi
