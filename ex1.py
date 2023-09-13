class category:

    # a = "Satyam"
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def categories():

        for category in ct:
            print("Category Name:", category.name, "Category Code:", category.code, "No of Product",
                  category.no_of_products)


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


c1 = category("Electronics", "E1")
c2 = category("Clothes", "C1")
c3 = category("Automobiles", "A1")
c4 = category("Food", "F1")
ct = [c1, c2, c3, c4]

p1 = Product("Laptop", "P1", c1, 75000)
p2 = Product("Laptop", "P2", c2, 65000)
p3 = Product("Laptop", "P3", c4, 70000)
p4 = Product("Laptop", "P4", c2, 72000)
p5 = Product("Laptop", "P5", c1, 15000)
p6 = Product("Laptop", "P6", c3, 25000)
p7 = Product("Laptop", "P7", c2, 45000)
p8 = Product("Laptop", "P8", c3, 55000)
p9 = Product("Laptop", "P9", c4, 50000)
p10 = Product("Laptop", "P10", c4, 35000)
p11 = Product("Laptop", "P11", c4, 52000)
p12 = Product("laptop", "P12", c1, 25000)

product_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]


Product.sorting_in_low_to_high()

print("\n")
category.categories()
print("\n")

Product.search()






