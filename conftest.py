import pytest
from utils.model_client import ModelClient
from utils.generate_metrics_report import Report
from utils.generate_performance_report import PerformanceTestReport
import base64

def pytest_addoption(parser):
    parser.addoption("--model", default="qwen2.5-vl")

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
def random_b64_string():
    return "VGhpcyBpcyBhIHJhbmRvbSBiNjQgc3RyaW5nIHRoYXQgZG9lc24ndCBjb250YWluIGFueSBpbWFnZSBkYXRhLg=="

@pytest.fixture
def edge_case_image_in_b64_ripped_receipt():
    with open('images/edge_case_image_receipt_ripped.jpeg', 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    return image_b64

@pytest.fixture
def edge_case_image_in_b64_image_from_side():
    with open('images/edge_case_image_from_side.jpeg', 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    return image_b64

@pytest.fixture
def edge_case_image_in_b64_blurry_receipt():
    with open('images/edge_case_image_blurry.jpeg', 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    return image_b64

@pytest.fixture
def edge_case_image_in_b64_minus():
    with open('images/edge_case_image_minus.jpeg', 'rb') as f:
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

@pytest.fixture(scope="session", autouse=True)
def performance_report(model):
    performance_report = PerformanceTestReport(model)
    yield performance_report
    performance_report.save_report()


