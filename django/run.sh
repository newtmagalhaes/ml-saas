# coleta arquivos estáticos para o NGinx
python manage.py collectstatic --no-input

# aplica migrações
python manage.py migrate

# inicia aplicação
gunicorn project.wsgi
