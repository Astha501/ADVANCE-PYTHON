class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class CRM:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email):
        c = Customer(name, email)
        self.customers.append(c)

    def show_customers(self):
        for c in self.customers:
            print(c.name, "-", c.email)

crm = CRM()

crm.add_customer("Riya", "riya@gmail.com")
crm.add_customer("Amit", "amit@gmail.com")

crm.show_customers()