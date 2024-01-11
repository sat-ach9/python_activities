import re
from datetime import datetime
from datetime import date


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

P1 = Product("soda", 100)
P2 = Product("brad", 40)
P3 = Product("Shirts", 200)
P4 = Product("Jenes", 300)
# P = Product("soda", 100)


class types:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Customer:
    def __init__(self, name, email, phone, street, city, state, country, types, company=None):
        self.name = Customer.valid_for_strings(name)
        self.email = Customer.valid_email(email)
        self.phone = Customer.valid_phone(phone)
        self.street = street
        self.city = Customer.valid_for_strings(city)
        self.state = Customer.valid_for_strings(state)
        self.country = Customer.valid_for_strings(country)
        self.company = company
        self.type = Customer.valid_for_type(types)


    def customer_info(ct):
        print("Name:", ct.name, "Email:", ct.email, "Phone:", ct.phone, "Street:", ct.street, "City:", ct.city, "State:", ct.state, "Country:",
              ct.country, "Company:", ct.company, "Type:", ct.type.name)
        print("\n")
    def valid_email(x):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if (re.fullmatch(regex, x)):
            return x
        else:
            return "Invalid Email"

    def valid_phone(phone):
        a =str(phone)
        regex = r'\b[6-9][0-9]{9}\b'

        if (re.fullmatch(regex, a)):
            return a
        else:
            return "Invalid Phone"

    def valid_for_strings(x):
        res = any(chr.isdigit() for chr in x)

        if res == True:
            return "string has a digit in it"
        else:
            return x
    def valid_for_type(y):
        ty = ["company", "contact", "billing", "shipping"]

        if y in ty:
            return y
        else:
            return  "Invalid type\ntype must be one of the these (company, contact, billing, shipping) "



    def company_relation(self):
        if self.company is None:
            return self.name
        else:
            return f'{self.company.company_relation()}'



    def display_customer_with_order():
        for customer in cust:
            print(f'\nCompany Name:{customer.name} \nEmail:{customer.email} \nPhone:{customer.phone} \nAddress:{customer.street},{customer.city},{customer.state},{customer.country} '
                  f'\nSub company of:{customer.company_relation()} \nTypes of Company:{customer.type}')



            # for o_lst in order_list:
            count = 0
            for o_lst in order_list:

                if o_lst.company == customer.name:
                    print("")
                    print(f"______List of the Orders of \"{o_lst.company}\"______________________")
                    print("Order number:", o_lst.number, ",", "Company name:", ",", o_lst.company, ",", "Total Amount:",
                          o_lst.total_amount)

                    count += 1
                    # print(count)
                elif count == 0 and o_lst != order_list[-1]:
                    continue
                elif count == 0 and o_lst == order_list[-1]:
                    print("no order")
                # elif count != 0 and o_lst == order_list[-1]:
                #     continue
                else:
                    continue


class Order:
    def __init__(self, number, date, company, billing,
                 shipping):
        self.number = number
        # self.date = Order.valid_date(date_value)
        self.date = Order.date_valid(date)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.total_amount = 0

        self.order_lines = []

    #"date" must be today or the future. Does not allow past date.

    def date_valid(date1):
        convert1 = datetime.strptime(date1, '%d-%m-%Y').date()

        d1 = date.today()
        if convert1 < d1:
            return "date invalid"
        else:
            return date1

    def display_info(self):
        print("Order number:", self.number, "Date:", self.date, "Company name:", self.company, "Billing Company", self.billing, "Shipping Company", self.shipping, "Total Amount:", self.total_amount)
        for i in self.order_lines:
            print("Product:", i.product, "Quantity:", i.quantity, "Price:", i.price)


    def display_all_orders():

        for o_lst in order_list:
            print("Order number:", o_lst.number, "Company name:", o_lst.company, "Total Amount:", o_lst.total_amount)
            for i in o_lst.order_lines:
                print(i)

            print("\n")

    def search():
        search = input("Enter product code (type in this manner - ORD__ or ord__):\n")
        x = search.upper()
        for order in order_list:
            if order.number.upper() == x:
                order.display_info()
    def sorting_in_date():

        for i in range(0, len(order_list)):
            for j in range(i+1, len(order_list)):
                if datetime.strptime(order_list[i].date, '%d-%m-%Y').date() >= datetime.strptime(order_list[j].date, '%d-%m-%Y').date():
                    temp = order_list[i]
                    order_list[i] = order_list[j]
                    order_list[j] = temp

        print("\n")
        print("Sorting of the order (Date vise) ")

        for i in order_list:
            i.display_info()
            print("\n")

    def current_month_orders():
        print("CURRENT MONTHS ORDERS")
        for i in order_list:
            if datetime.strptime(i.date, '%d-%m-%Y').month == datetime.now().month:
                i.display_info()


    def orders_for_specific_product():
        search = input("Enter the product name for see all orders for it:\n")
        product_name = search.upper()
        for o in order_list:
            for x in o.order_lines:
                if x.product.upper() == product_name:
                    print(f"\nOrder number:{x.order.number},\nCompany name:{x.order.company},\nQuantity:{x.quantity},Price:{x.price}")

class OrderLine:

    def __init__(self, Order, Product, product, quantity, price, subtotal=None):

        self.order = Order
        self.Product = Product
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = OrderLine.totalSum(quantity, price)
        # self.__init_subclass__()

        Order.total_amount += self.subtotal

    def totalSum(quantity, price):
        x = quantity*price
        return x

t1 = types("company", "Company")
t2 = types("contact", "Contact")
t3 = types("billing", "Billing")
t4 = types("shipping", "Shipping")

Company = Customer("satyam enterprise", "abc123@gmail.com", 9654785214, "abs street", "xyz", "Gujarat", "India", "company", None)
billing = Customer("a", "satyam13@gmail.com", 9644385214, "3 manhar street", "Ahmedabad", "Gujarat", "India", "billing", Company)
shipping = Customer("b", "harsh1dholakiya@gmail.com", 9651235214, "Nana maua", "Surat", "Gujarat", "India", "shipping", Company )

cust = [Company, billing, shipping]

# c1 = Customer("Jeet", "jeet@gmail.com", 9664609945, "3 manhar plot", "Rajkot", "Gujarat", "India", "1into2 digital", t1)
# c2 = Customer("Harsh", "harshdholakiya@gmail.com",9658417524,"4 manhar plot","Rajkot","Gujarat","India", "1into2 digital", t2)
# c3 = Customer("karan", "karanlathiya1@gmail.com", 9641587254, "19 manhar plot", "Rajkot", "Gujarat", "India", "Zuru", t4)
# c4 = Customer("Tushar", "tusharmandani234@gmail.com", 9874123658, "ghel chowk", "Amreli", "Gujarat", "India", "Tatvasoft", t3)
# cust = [c1, c2, c3, c4]

o1 = Order("ORD01", "02-02-2024", "satyam enterprise", billing.name, shipping.name)
o2 = Order("ORD02", "14-01-2024", "Harsh enterprise", billing.name, shipping.name)

order_list = [o1, o2]


o_line1 = OrderLine(o1, P1, P1.name, 10, P1.price)
o_line2 = OrderLine(o1, P2, P2.name, 10, P2.price)
o_line3 = OrderLine(o2, P3,  P3.name, 20, P3.price)
o_line4 = OrderLine(o2, P4, P4.name, 20, P4.price)
o_line5 = OrderLine(o2, P1, P1.name, 10, P1.price)
# o3 = Order()
# o4 = Order()
order_lines_list = [o_line1, o_line2, o_line3, o_line4, o_line5]



for order_ws in order_list:
    for order_ls_lt in order_lines_list:
        if order_ws.company == order_ls_lt.order.company:
            order_ws.order_lines.append(order_ls_lt)


# _______________________________________________________________________________________________
# Customer.display_customer_with_order()
Order.sorting_in_date()
print("________________________________________________________________________________________")
Order.current_month_orders()
print("\n")
print("________________________________________________________________________________________")
Order.search()
print("\n")
print("________________________________________________________________________________________")
Order.orders_for_specific_product()

# _________________________________________________________________________________________
