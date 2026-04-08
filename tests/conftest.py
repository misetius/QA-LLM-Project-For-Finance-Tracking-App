import pytest
from utils.wrapper import ModelClient
import base64

def pytest_addoption(parser):
    parser.addoption("--model", default="qwen2.5vl")

@pytest.fixture
def model(request):
    return request.config.getoption("--model")

@pytest.fixture
def clear_image_in_b64():
    with open('images/clear_image.jpeg', 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    return image_b64

@pytest.fixture
def model_client(model):
    return ModelClient(model)