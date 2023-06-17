from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    customersID = Column("CustomersID", Integer, primary_key=True)
    name = Column("Name", String)
    email = Column("Email", String)
    phone = Column("Phone", Integer)
    address = Column("Address", String)

    def __init__(self, customersID, name, email, phone, address):
        self.customersID = customersID
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"({self.customersID}) {self.name} {self.email} ({self.phone}) ({self.address})"


class Order(Base):
    __tablename__ = "orders"

    orderID = Column("OrderID", Integer, primary_key=True)
    customerID = Column("CustomerID", Integer, ForeignKey('customers.CustomerID'))
    product = Column("Product", String)
    quantity = Column("Quantity", Integer)
    orderDate = Column("OrderDate", Date)

    def __init__(self, orderID, customerID, product, quantity, orderDate):
        self.orderID = orderID
        self.customerID = customerID
        self.product = product
        self.quantity = quantity
        self.orderDate = orderDate

    def __repr__(self):
        return f"({self.orderID}) {self.customerID} {self.product} ({self.quantity}) ({self.orderDate})"


engine = create_engine("sqlite:///company.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

#    Customer(C-ID,  name,   email,                 phone,     address)
c1 = Customer(31234, "Anna", "annablue@github.com", 501234567, "958 Tremont St")
c2 = Customer(32423, "Bob", "bobblue@github.com", 502345671, "11040 Minnesota 55")
c3 = Customer(45654, "Angela", "angelacold@github.com", 503456712, "25123 SE Stark St")
c4 = Customer(12312, "Mike", "mikesmith@github.com", 504567123, "5415 Pinemont Dr")

session.add(c1)
session.add(c2)
session.add(c3)
session.add(c4)
session.commit()

#    Order(O-ID,  C-ID,  product, qty.,  order date)
o1 = Order(47852, 31234, "nails", 12500, OrderDate=(datetime.strptime('2023-06-25', '%Y-%m-%d').date()))
o2 = Order(65781, 32423, "hammer", 120, OrderDate=(datetime.strptime('2023-07-01', '%Y-%m-%d').date()))
o3 = Order(75389, 45654, "plier", 170, OrderDate=(datetime.strptime('2023-06-29', '%Y-%m-%d').date()))
o4 = Order(14924, 12312, "wrench", 150, OrderDate=(datetime.strptime('2023-06-20', '%Y-%m-%d').date()))
session.commit()
