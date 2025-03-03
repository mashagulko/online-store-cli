# orders/orders.py

orders_list = []  # Список заказов

def create_order(product_name, quantity):
    """Создаёт новый заказ"""
    orders_list.append({"product": product_name, "quantity": quantity})

def list_orders():
    """Возвращает список заказов"""
    return orders_list
