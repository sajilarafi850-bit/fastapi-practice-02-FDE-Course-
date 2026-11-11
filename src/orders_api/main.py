from fastapi import FastAPI

app = FastAPI(title="Noor Foods Orders API")

ORDERS = {
    "A101": {
        "id": "A101",
        "customer": "Noor Foods",
        "total": 4500,
        "status": "pending",
    },
    "A102": {
        "id": "A102",
        "customer": "Bilal Traders",
        "total": 12800,
        "status": "delivered",
    },
    "A103": {
        "id": "A103",
        "customer": "Karachi Crafts",
        "total": 2300,
        "status": "pending",
    },
}


@app.get("/")
def read_root() -> dict[str, str]:
    return {"app": "Noor Foods Orders API", "docs": "/docs"}


@app.get("/orders")
def list_orders() -> list[dict]:
    return list(ORDERS.values())


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> dict:
    return ORDERS[order_id]


# problem 1


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


# problem 2
@app.get("/products")
def list_products() -> list[dict[str, str | int]]:
    return [
        {"name": "Biryani", "price": 450},
        {"name": "Nihari", "price": 600},
        {"name": "Chicken Karahi", "price": 1200},
    ]
