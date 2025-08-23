def test_get_users(api_client):
    resp = api_client.get("api/users?page=2")   # removed leading /
    assert resp.status == 200
    print("\nGET Response:", resp.json())

def test_create_user(api_client):
    payload = {"name": "morpheus", "job": "leader"}
    resp = api_client.post("api/users", payload)   # no leading /
    assert resp.status == 201
    print("\nPOST Response:", resp.json())

def test_update_user_put(api_client):
    payload = {"name": "morpheus", "job": "zion resident"}
    resp = api_client.put("api/users/2", payload)  # no leading /
    assert resp.status == 200
    print("\nPUT Response:", resp.json())

def test_update_user_patch(api_client):
    payload = {"job": "zion commander"}
    resp = api_client.patch("api/users/2", payload)  # no leading /
    assert resp.status == 200
    print("\nPATCH Response:", resp.json())

def test_delete_user(api_client):
    resp = api_client.delete("api/users/2")   # no leading /
    assert resp.status == 204
    print("\nDELETE Status:", resp.status)
