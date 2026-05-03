import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_add():
    response = client.post("/op/add", json={"op1": 5, "op2": 3, "mod": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 1, "mod": 7}

def test_caesar_api():
    # Encrypt
    response = client.post("/crypto/caesar/encrypt", json={"text": "HELLO", "key": 3})
    assert response.status_code == 200
    assert response.json() == {"result": "KHOOR"}
    
    # Decrypt
    response = client.post("/crypto/caesar/decrypt", json={"text": "KHOOR", "key": 3})
    assert response.status_code == 200
    assert response.json() == {"result": "HELLO"}

def test_affine_api():
    # Encrypt
    response = client.post("/crypto/affine/encrypt", json={"text": "ABC", "a": 5, "b": 8})
    assert response.status_code == 200
    assert response.json() == {"result": "INS"}
    
    # Decrypt
    response = client.post("/crypto/affine/decrypt", json={"text": "INS", "a": 5, "b": 8})
    assert response.status_code == 200
    assert response.json() == {"result": "ABC"}
    
    # Invalid Key 'a' (not coprime)
    response = client.post("/crypto/affine/encrypt", json={"text": "ABC", "a": 2, "b": 3})
    assert response.status_code == 400
    assert "ValidationError" in response.json()["error"]

def test_vigenere_api():
    # Encrypt
    response = client.post("/crypto/vigenere/encrypt", json={"text": "HELLO", "keyword": "KEY"})
    assert response.status_code == 200
    assert response.json() == {"result": "RIJVS"}
    
    # Decrypt
    response = client.post("/crypto/vigenere/decrypt", json={"text": "RIJVS", "keyword": "KEY"})
    assert response.status_code == 200
    assert response.json() == {"result": "HELLO"}

def test_modint_exception_api():
    # Division by zero or non-invertible
    response = client.post("/op/div", json={"op1": 5, "op2": 2, "mod": 4})
    assert response.status_code == 400
    assert "InvalidInverseError" in response.json()["error"]

def test_crt_api():
    response = client.post("/op/crt", json={"remainders": [2, 3, 2], "moduli": [3, 5, 7]})
    assert response.status_code == 200
    assert response.json() == {"result": 23, "modulus": 105}
