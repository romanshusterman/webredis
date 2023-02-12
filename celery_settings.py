import os
CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = os.environ.get('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['json']
