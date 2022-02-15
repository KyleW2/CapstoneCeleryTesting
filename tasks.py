from celery import Celery

BROKER_URL = "amqp://kyle:password@localhost:5672/vhost1"

app = Celery('tasks', broker = BROKER_URL)

@app.task
def multiply(x: int, y: int) -> int:
	return x * y
