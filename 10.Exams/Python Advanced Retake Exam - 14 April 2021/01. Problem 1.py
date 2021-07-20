from collections import deque

orders = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]

orders = deque([x for x in orders if 0 < x <= 10])
pizza_counter = 0

while orders and employees:
    current_order = orders.popleft()
    current_employee = employees.pop()
    if current_order <= current_employee:
        pizza_counter += current_order
    else:
        current_order -= current_employee
        orders.appendleft(current_order)
        pizza_counter += current_employee

if not orders:
    print(
        f"All orders are successfully completed!\n"
        f"Total pizzas made: {pizza_counter}\n"
        f"Employees: {', '.join([str(x) for x in employees])}")
elif not employees and len(orders) > 0:
    print(
        f"Not all orders are completed.\n"
        f"Orders left: {', '.join([str(x) for x in orders])}"
    )
