import pytest

import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(directory)

sys.path.append(parent)

from tasks import multiply

@pytest.fixture(scope = "session")
def celery_config():
	return {
		"broker_url": "amqp://kyle:password@localhost:5672/vhost1"
	}

def test_multiply(celery_worker):
	multiply.delay(2, 2)
