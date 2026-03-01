FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

COPY --chmod=+x run.sh .

ENV DJANGO_SETTINGS_MODULE=project.settings_prod
ENV PYTHONUNBUFFERED=1
ENV APP_PORT=8000

ENTRYPOINT ["sh", "run.sh"]

EXPOSE ${APP_PORT}

VOLUME [ "/app/.static", "/app/.media", "/app/db.sqlite3" ]
