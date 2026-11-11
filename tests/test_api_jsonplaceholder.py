import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def test_get_post_ok():
    """GET /posts/1 devuelve 200 y un JSON con los campos esperados."""
    response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    for campo in ("userId", "id", "title", "body"):
        assert campo in data


def test_get_post_inexistente():
    """GET a un post que no existe devuelve 404 (escenario de error)."""
    response = requests.get(f"{BASE_URL}/posts/9999", timeout=TIMEOUT)
    assert response.status_code == 404


def test_create_post():
    """POST /posts devuelve 201 y refleja los datos enviados."""
    payload = {"title": "Mi post", "body": "Contenido de prueba", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_delete_post():
    """DELETE /posts/1 devuelve 200."""
    response = requests.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code == 200


def test_encadenado_usuario_y_sus_posts():
    """Obtiene un usuario y verifica que sus posts tengan ese userId."""
    user = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)
    assert user.status_code == 200
    user_id = user.json()["id"]

    posts = requests.get(f"{BASE_URL}/posts", params={"userId": user_id}, timeout=TIMEOUT)
    assert posts.status_code == 200
    lista = posts.json()
    assert len(lista) > 0
    assert all(p["userId"] == user_id for p in lista)
