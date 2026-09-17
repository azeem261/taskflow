import json


def test_create_task_publishes_event_and_appears_in_list(client, fake_redis):
    pubsub = fake_redis.pubsub()
    pubsub.subscribe("task-events")
    pubsub.get_message(timeout=1)  # discard the subscribe confirmation

    res = client.post("/tasks", json={"title": "Write docs", "description": "Explain the setup"})
    assert res.status_code == 201
    body = res.json()
    assert body["title"] == "Write docs"
    assert body["owner"] == "alice@example.com"
    assert body["status"] == "todo"

    message = pubsub.get_message(timeout=1)
    payload = json.loads(message["data"])
    assert payload["event"] == "task.created"
    assert payload["task"]["title"] == "Write docs"

    list_res = client.get("/tasks")
    assert list_res.status_code == 200
    assert len(list_res.json()) == 1


def test_get_missing_task_returns_404(client):
    res = client.get("/tasks/999")
    assert res.status_code == 404


def test_update_task_publishes_event(client, fake_redis):
    create_res = client.post("/tasks", json={"title": "Ship it", "description": ""})
    task_id = create_res.json()["id"]

    pubsub = fake_redis.pubsub()
    pubsub.subscribe("task-events")
    pubsub.get_message(timeout=1)

    update_res = client.put(f"/tasks/{task_id}", json={"status": "done"})
    assert update_res.status_code == 200
    assert update_res.json()["status"] == "done"

    message = pubsub.get_message(timeout=1)
    payload = json.loads(message["data"])
    assert payload["event"] == "task.updated"
    assert payload["task"]["status"] == "done"


def test_delete_task(client):
    create_res = client.post("/tasks", json={"title": "Temp", "description": ""})
    task_id = create_res.json()["id"]

    delete_res = client.delete(f"/tasks/{task_id}")
    assert delete_res.status_code == 204

    get_res = client.get(f"/tasks/{task_id}")
    assert get_res.status_code == 404
