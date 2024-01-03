# Create one class named “location” with members “name”, “code”.
# Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
# Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”. This method will return all “movement” objects which belong to the passed “product” as an argument.
# Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains “location” as key and actual stock of that product on that location as value.
# Create 4 different location objects.
# Create 5 different product objects.
# Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve.
# Display movements of each product using the “movement_by_product” method.
# Display product details with its stock at various locations using “stock_at_locations”.
# Display product list by location ( group by location).
class location:
    def __init__(self, name, code ):
        self.name = name
        self.code = code
class movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
    def movements_by_product(i):
        count = 0
        for x in range(len(mov)):

            if mov[x].product == products[i].name:
                print("From",mov[x].from_location, "to", mov[x].to_location, "Product:", mov[x].product, "Quantity:", mov[x].quantity)

                products[i].stock_at_locations[mov[x].from_location] += (-1)*(mov[x].quantity)
                #decresing the number of quantity of particular product at particular location

                products[i].stock_at_locations[mov[x].to_location] += (1)*(mov[x].quantity)
                # incresing the number of the quantity of particular product at particular location

                count += 1
            elif mov[x] != mov[-1] and count != 0:
                continue
            elif mov[x] == mov[-1] and count == 0:
                print("No Movement of this product")
            else:
                continue
class product:
    def __init__(self, name, code, price, stock_at_locations):
        self.name = name
        self.code = code
        self.price = price
        # category.no_of_products += 1
        self.stock_at_locations = stock_at_locations

    def dis_product_listby_grp(x):
        for list_x in range(len(products)):
            print(products[list_x].name, ":", products[list_x].stock_at_locations[x])
    def product_stock_detail():
        for i in products:
            print("Product Name:", i.name)
            print("Product Code:", i.code)
            print("Product Stock at different locations:", i.stock_at_locations)
            print('\n')


l1 = location("Ahmedabad", "GJ01")
l2 = location("Rajkot", "GJ03")
l3 = location("Junagadh", "GJ10")
l4 = location("Amreli", "GJ14")

locations = [l1,l2,l3,l4]

p1 = product("BMW","P1", 12500000,{l1.name: 19, l2.name: 0, l3.name: 0, l4.name: 0})
p2 = product("Audi","P2", 11500000,{l1.name: 11, l2.name: 0, l3.name: 0, l4.name: 0})
p3 = product("Mercedes", "P3", 11300000,{l1.name: 0, l2.name: 12, l3.name: 0, l4.name: 0})
p4 = product("Ford", "P4", 2500000,{l1.name: 0, l2.name: 15, l3.name: 0, l4.name: 0})
p5 = product("Tata", "P5", 2000000,{l1.name: 0, l2.name: 0, l3.name: 23, l4.name: 0})

products = [p1,p2,p3,p4,p5]

m1 = movement("Ahmedabad", "Rajkot",'BMW', 10)
m2 = movement("Rajkot", "Amreli",'Ford', 14)
m3 = movement("Junagadh", "Rajkot",'Tata', 11)
m4 = movement("Ahmedabad", "Amreli",'Audi', 9)
m5 = movement("Ahmedabad","Amreli","BMW", 5)
m6 = movement("Rajkot", "Amreli", "Mercedes", 7)

mov = [m1, m2, m3, m4, m5, m6]

print("\n")
print("=> Stock of the product at different location")
print("_____________________________________________________________________________________ \n ")
product.product_stock_detail()

print("=> Display the movements of the different products")
print("_____________________________________________________________________________________ \n ")
for i in range(len(products)):
    print(products[i].name, products[i].code)
    movement.movements_by_product(i)
    print("\n")

print("=> After the movement of the products the stock at different location")
print("_____________________________________________________________________________________ \n ")
product.product_stock_detail()

print("=> Display product list by location ( group by location).")
print("___________________________________________________________ \n ")
for loc in range(len(locations)):
    print("Location:", locations[loc].name)
    print("Numbers of products:")
    x = locations[loc].name
    product.dis_product_listby_grp(x)
    print("\n")