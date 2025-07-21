from fastapi import FastAPI, HTTPException

app = FastAPI()

data_store = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Canary Deployment Demo"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = data_store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": item}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: str):
    data_store[item_id] = item
    return {"message": "Item created", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in data_store:
        del data_store[item_id]
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
