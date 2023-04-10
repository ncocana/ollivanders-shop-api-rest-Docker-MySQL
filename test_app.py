import json
import pytest
from app import app
from database import db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# TEST "GET" METHOD.


@pytest.mark.test_endpoints_get
def test_get_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data is not None


@pytest.mark.test_endpoints_get
def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert response.data is not None


@pytest.mark.test_endpoints_get
def test_get_inventory_create(client):
    response = client.get("/inventory/create")
    assert response.status_code == 200
    assert response.data is not None


@pytest.mark.test_endpoints_get
def test_get_inventory_delete(client):
    response = client.get("/inventory/delete")
    assert response.status_code == 200
    assert response.data is not None


@pytest.mark.test_endpoints_get
def test_get_inventory_success(client):
    response = client.get("/inventory/success")
    assert response.status_code == 200
    assert response.data is not None
    assert b"Inventory updated" in response.data


@pytest.mark.test_endpoints_get
def test_get_item_with_valid_id(client):
    response = client.get("/inventory/get?id=7")
    assert response.status_code == 200
    assert response.data is not None
    item = db.get_item_by_id(7)
    assert json.loads(response.data) == dict(item)


@pytest.mark.test_endpoints_get
def test_get_item_with_missing_id(client):
    response = client.get("/inventory/get")
    assert response.status_code == 400
    assert json.loads(response.data) == {"error": "ID parameter missing"}


@pytest.mark.test_endpoints_get
def test_get_item_with_invalid_id(client):
    response = client.get("/inventory/get?id=invalid_id")
    assert response.status_code == 400
    assert json.loads(response.data) == {"error": "Invalid ID parameter"}


@pytest.mark.test_endpoints_get
def test_get_item_not_found(client):
    response = client.get("/inventory/get?id=100")
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "Item not found"}


# TEST "POST" METHOD.


@pytest.mark.test_endpoints_post
def test_post_inventory_no_param(client):
    response = client.post("/inventory/create")
    assert response.status_code == 200
    assert response.data is not None
    assert b"Invalidad data in the form" in response.data


@pytest.mark.test_endpoints_post
def test_post_inventory_with_wrong_param(client):
    item = {
        "name": "Test item",
        "sell_in": "String",
        "quality": "String",
        "class_object": "ConjuredItem",
    }
    response = client.post("/inventory/create", data=item)
    assert response.status_code == 200
    assert response.data is not None
    assert b"Invalidad data in the form" in response.data


@pytest.mark.test_endpoints_post
def test_post_inventory_with_param(client):
    item = {
        "name": "Test item",
        "sell_in": 10,
        "quality": 5,
        "class_object": "ConjuredItem",
    }
    response = client.post("/inventory/create", data=item)
    assert response.status_code == 200
    assert response.data is not None
    assert b"Inventory updated" in response.data

    INVENTORY = db.get_all_inventory()
    name_item_list = [item["name"] for item in INVENTORY]

    assert item["name"] in name_item_list


# TEST "PUT" METHOD.


@pytest.mark.test_endpoints_put
def test_put_inventory(client):
    response = client.put("/inventory")
    assert response.status_code == 200
    assert response.data is not None
    assert json.loads(response.data) == {"success": True}


# TEST "DELETE" METHOD.


@pytest.mark.test_endpoints_delete
def test_delete_inventory_item(client):
    item = db.get_item_by_name("Test item")
    if item is not None:
        item_id = {"id": item["id"]}
        response = client.delete("/inventory/delete", data=item_id)
        assert response.status_code == 200
        assert response.data is not None

        INVENTORY = db.get_all_inventory()
        id_item_list = [item["id"] for item in INVENTORY]

        assert item["id"] not in id_item_list
