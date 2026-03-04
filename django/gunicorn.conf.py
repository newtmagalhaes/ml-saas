import multiprocessing
from os import getenv

# Logs
accesslog = '-'
access_log_format = r"%(h)s %(u)s %(t)s %(p)s '%(f)s' %(r)s %(s)s %(T)ss %(b)sB %(a)s"

# Server config
bind = "0.0.0.0:" + getenv("APP_PORT", "8000")
timeout = getenv("GUNICORN_TIMEOUT", "30")
# graceful_timeout = 30
# keepalive = 5
# worker_class = getenv("GUNICORN_WORKER_CLASS", "gevent")
workers = getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1)
max_requests = 500
max_requests_jitter = 50

# if worker_class == 'gevent':
#     environ.setdefault("USING_GUNICORN", "true")
