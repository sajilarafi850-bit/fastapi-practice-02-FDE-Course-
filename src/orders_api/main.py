"""from fastapi import FastAPI

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
# problem 3

@app.get("health")
def health_check():
    return {"status": "ok"}"""
# AssertionError: Path must start with '/

from enum import StrEnum

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Noor Foods Orders API")


class OrderStatus(StrEnum):
    PENDING = "pending"
    DELIVERED = "delivered"


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
def list_orders(
    customer: str | None = None,
    status: OrderStatus | None = None,
    limit: int = 10,
) -> list[dict]:
    orders = []

    for order in ORDERS.values():
        if customer is not None and order["customer"].lower() != customer.lower():
            continue

        if status is not None and order["status"] != status:
            continue

        orders.append(order)

    return orders[:limit]


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> dict:
    if order_id not in ORDERS:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")

    return ORDERS[order_id]


@app.get("/orders")
def list_orders(
    status: OrderStatus | None = None,
    min_total: int | None = None,
    limit: int = 10,
) -> list[dict]:

    orders = []

    for order in ORDERS.values():
        if status is not None and order["status"] != status:
            continue

        if min_total is not None and order["total"] < min_total:
            continue

        orders.append(order)

    return orders[:limit]


@app.get("/customers/{name}/orders")
def get_customer_orders(name: str) -> list[dict]:

    orders = []

    for order in ORDERS.values():
        if order["customer"].lower() == name.lower():
            orders.append(order)

    if not orders:
        raise HTTPException(
            status_code=404, detail=f"No orders found for customer {name}"
        )

    return orders
