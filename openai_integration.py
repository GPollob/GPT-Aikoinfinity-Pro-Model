import pytest
from openai_integration.openai_api import get_openai_response

def test_openai_response():
    prompt = "What is the impact of AI on society?"
    response = get_openai_response(prompt)
    assert response is not None
    assert isinstance(response, str)
