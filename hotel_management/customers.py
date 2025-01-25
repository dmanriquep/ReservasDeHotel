class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        print(f"Cliente {customer.name} agregado.")

    def get_customer(self, customer_id):
        return self.customers.get(customer_id, "Cliente no encontrado")