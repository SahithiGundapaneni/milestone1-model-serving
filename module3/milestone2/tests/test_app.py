import pytest
from app.app import predict

def test_predict_success():
    out = predict({"text": "hello"})
    assert out["label"] == "OK"
    assert out["length"] == 5

def test_missing_text():
    with pytest.raises(ValueError):
        predict({"nope": "x"})

def test_bad_text():
    with pytest.raises(ValueError):
        predict({"text": ""})

def test_bad_payload_type():
    with pytest.raises(TypeError):
        predict("not a dict")
