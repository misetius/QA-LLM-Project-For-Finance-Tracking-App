import pytest
from utils.wrapper import ModelClient
from utils.generate_metrics_report import Report
import base64

def pytest_addoption(parser):
    parser.addoption("--model", default="qwen2.5vl")

@pytest.fixture(scope="session", autouse=True)
def model(request):
    return request.config.getoption("--model")

@pytest.fixture
def clear_image_in_b64():
    with open('images/clear_image.jpeg', 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    return image_b64

@pytest.fixture
def random_image_in_b64():
    with open('images/random_dog_image.jpg', 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    return image_b64

@pytest.fixture
def model_client(model):
    return ModelClient(model)

@pytest.fixture(scope="session", autouse=True)
def report(model):
    metrics_report = Report(model)
    yield metrics_report
    metrics_report.save_report()    

