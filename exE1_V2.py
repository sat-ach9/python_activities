# Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
# Add a new member function to generate “display_name”.
# “display_name” has the text value as below.
#        1.Vehicle category without parent then “Vehicle”
#        2.Car category with “Vehicle” as a parent then “Vehicle > Car”
#        3.Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
# Create 5 category objects with parent and child relation.
# Create 3 product objects in each category.
# Display the Category with its Code, Display Name, and all product details inside that category.
# Display product list by category (group by category, order by category name).

class Category:

    # a = "Satyam"
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.no_of_products = 0
        # self.display_name = display_name()

        # self.product_list = []

    def display_name(self):
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.display_name()} > {self.name}"

    def categories():

        for i in range(0, len(ct)):
            for j in range(i+1, len(ct)):
                if ct[i].name > ct[j].name:
                    temp=ct[i]
                    ct[i]=ct[j]
                    ct[j]=temp

        for categories_with_products in ct:
            print("Categ-name:",categories_with_products.name,"\n"
                  "Categ-code:",categories_with_products.code,"\n"
                  "Display Name of the Category:", categories_with_products.display_name(),"\n"
                  "No of Products:",categories_with_products.no_of_products
                  )
            for products in product_list:
                if products.category.name == categories_with_products.name:
                    print("Product Name:", products.name, "Product Code:", products.code, "Display Name of Category:",
                          categories_with_products.display_name(), "Product Price:", products.price)

            print("\n")




class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        # category.no_of_products()
        category.no_of_products += 1


    def display_cat(self):
        print(self.category)

    def sorted_list(self):
        print(self.price)

    def display_info(self):
        print(self.name, self.code, self.category.name, self.price)

    def sorting_in_low_to_high():

        for product in product_list:
            product.display_info()

        for i in range(0, len(product_list)):

            for j in range(i + 1, len(product_list)):
                if product_list[i].price >= product_list[j].price:
                    temp = product_list[i]
                    product_list[i] = product_list[j]
                    product_list[j] = temp

        print("\n")
        print("Sorted Product List")
        print("\n")

        # print(product_list)
        for product in product_list:
            product.display_info()



    def search():

        search = input("Enter product code:\n")
        for product in product_list:
            if product.code == search:
                product.display_info()

print("\n")

c1 = Category("Vehicle", "veh")
c2 = Category("Car","car",c1)
c3 = Category("Petrol","pet",c2)
c4 = Category("Electronic","E1")
c5 = Category("Freeze","A1",c4)
c6 = Category("Food","F1")

ct = [c1,c2,c3,c4,c5,c6]

p1 = Product("Bike","P1", c1, 75000)
p2 = Product("Car","P2", c1, 350000)
p3 = Product("Truck","P3", c1, 850000)

p4 = Product("BMW","P4", c2, 1250000)
p5 = Product("Audi","P5", c2, 1150000)
p6 = Product("Mercedes", "P6", c2, 1130000)

p7 = Product("Regular","P7", c3, 100)
p8 = Product("Shell","P8", c3, 108)
p9 = Product("Premium","P9", c3, 114)


p10 = Product("Device", "P10", c4, 75000)
p11 = Product("TV", "P11", c4, 65000)
p12 = Product("Others", "P12", c4, 70000)

p13 = Product("LG", "P13", c5, 72000)
p14 = Product("Samsung", "P14", c5, 55000)
p15 = Product("Haier", "P15", c5, 25000)

product_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12,p13, p14, p15]


# c5.add_product.(Product("bike","P13","")

Product.sorting_in_low_to_high()

print("\n")
Category.categories()

Product.search()



