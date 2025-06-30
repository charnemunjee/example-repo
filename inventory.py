
#========The beginning of the class==========
class Shoe:
    """ This code creates the shoe class

    Attributes:
        country (string): The country where the shoe was manufactured
        code (string): The code of the shoe
        product (string): The name of the shoe
        cost (float): The cost of a pair of shoes
        quantity (int): The number of pairs of shoes in stock

    Methods:
        get_cost: returns the cost of the item depending on the code input
        get_quantity: returns the number of pairs of shoes in stock depending on the code input
    """
    def __init__(self, country, code, product, cost, quantity):
        """ Initializes the shoe object

        Attributes:
            country (string): The country where the shoe was manufactured
            code (string): The code of the shoe
            product (string): The name of the shoe
            cost (float): The cost of a pair of shoes
            quantity (int): The number of pairs of shoes in stock
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self, code_input):
        """ Returns the cost for a specified shoe code"""
        if self.code == code_input:
            return self.cost

    def get_quantity(self, code_input):
        """ Returns the quantity of a specified shoe code"""
        if self.code == code_input:
            return self.quantity

    def __str__(self):
        """ Returns a string with the shoe name, shoe cost, shoe code and quantity of shoes"""
        return f"Product: {self.product}, Cost: {str(self.cost)}, Code: {self.code}, Quantity: {str(self.quantity)}, Country: {self.country}"


#=============Shoe list===========

# Initializes the shoe_list to store a list of shoe objects
shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():
    """
    This function does the following:
        Opens the file inventory.txt
        Reads the data from this file and loops through each row to create a shoe object
        Appends the object into the shoe_list.
    """

    # Initializes the shoe_database to temporarily store
    # a nested list where each item in the list is a
    # list containing information about a shoe
    shoe_database = []
    try:
        # Opens the inventory text file, creates a list from each line in the file
        # Each list is stored in the shoe database
        # The first row in the text file is removed from the shoe_database
        with open("inventory.txt", "r") as file:
            for line in file:
                shoe_database.append(line.replace("\n", "").split(","))
            shoe_database.pop(0)

    # If file does not exist, the code outputs an error message
    except FileNotFoundError:
        print("Error: The file was not found")

    # Loops through the shoe_database list,
    # Specifies the index of items in the list that represents each attribute for the shoe object
    # Create objects and stores it in shoe_list
    for inventory in range(len(shoe_database)):
        object_name = shoe_database[inventory][2]
        object_country = shoe_database[inventory][0]
        object_code = shoe_database[inventory][1]
        object_product = shoe_database[inventory][2]
        object_cost = float(shoe_database[inventory][3])
        object_quantity = int(shoe_database[inventory][4])

        object_name = Shoe(object_country, object_code, object_product, object_cost, object_quantity)

        shoe_list.append(object_name)


def capture_shoes():
    """This function allows the user to enter data about a shoe
    and create a shoe object that is added to the shoe_list"""

    # This code asks the user to enter the attribute of the new objects
    object_name = input("Please enter the product name")
    object_product = object_name
    object_country = input("Please enter the country")
    object_code = input("Please enter the code")
    object_cost = float(input("Please enter the product cost"))
    object_quantity = int(input("Please enter the quantity of stock"))

    # Check if the shoe already exists in the shoe_list. If the shoe exists, print an error message
    for shoe in range(len(shoe_list)):
        # if the shoe name already exists, print out an error message
        if shoe_list[shoe].product == object_product:
            print(f"The object already exists with code: {shoe_list[shoe].code}")
        # if the shoe code already exists, print out an error message
        elif shoe_list[shoe].code == object_code:
            print(f"This code already exists. The shoe name is {shoe_list[shoe].product}")
        # if the shoe exists, create the object and add it to the database
        else:
            object_name = Shoe(object_country, object_code, object_product, object_cost, object_quantity)

    shoe_list.append(object_name)


def view_all():
    """
    This function returns a list of all the shoes,
    their names, code, cost and quantity
    """
    # Loop through the list of shoe objects in the database and print
    # the information
    for shoe in range(len(shoe_list)):
        print(shoe_list[shoe])


def re_stock():
    """
    This function finds and prints the item with the lowest stock then asks the
    user if they would like to order more stock. If yes, it asks the
    user for the quantity of stock it needs to re-order
    """

    stock_minimum = 0
    shoe_product_minimum = ""
    shoe = 0

    # This while loop does the following:
    #   Loops through the list of shoe objects to find the shoe with the lowest quantity attribute
    #   Saves the smallest quantity found in "stock_minimum"
    #   Saves the name of the product with lowest quantity as "shoe_product_minimum"
    #   Saves the index of the product with lowest quantity in variable "shoe"
    while shoe < len(shoe_list):
        if shoe == 0:
            stock_minimum = shoe_list[0].quantity
            shoe_product_minimum = shoe_list[0].product
        elif shoe_list[shoe].quantity < stock_minimum:
            stock_minimum = shoe_list[shoe].quantity
            shoe_product_minimum = shoe_list[shoe].product
            shoe_min_position = shoe
        else:
            stock_minimum = stock_minimum
            shoe_product_minimum = shoe_product_minimum

        shoe += 1

    # prints the details of the shoe with the lowest quantity
    print(f"Shoe with lowest stock: {shoe_product_minimum}")
    print(f"Stock: {stock_minimum}")

    # Ask the user if they would like to update stock and by how much.
    # If yes, then change the quantity attribute to updated stock levels
    update_stock = input(f"Do you want to order more stock for this shoe?(Y/N)").capitalize()
    if update_stock == "Y":
        order_size = int(input("How many shoes would you like to order?"))
        shoe_list[shoe_min_position].quantity += order_size
        print(f"The stock of {shoe_product_minimum} has been updated to {shoe_list[shoe_min_position].quantity}")
    else:
        print(f"No problem. The stock of {shoe_product_minimum} will remain unchanged")


def search_shoe():

    """
    This function asks the user to input the code of the shoe they
    want to view
    and loops through the shoe objects in shoe_list until the shoe code equals
    the user input and prints the shoe information
    """

    # Asks the user to input the shoe code they want to view
    shoe_code_input = input("Please enter the shoe code you would like to find: ")

    # Loops through the objects in shoe_list until shoe code equals the user input
    # prints the information on the shoe
    for shoe in range(len(shoe_list)):
        if shoe_list[shoe].code == shoe_code_input:
            print(shoe_list[shoe])


def value_per_item():
    """
    This function calculates the total value of each shoe object
    as cost of shoe * quantity of shoe
    and prints the shoe name and total value
    """

    print("")
    print("Report on the value of all shoes\n")
    for shoe in range(len(shoe_list)):
        value = shoe_list[shoe].quantity * shoe_list[shoe].cost
        print(f"Shoe: {shoe_list[shoe].product} | Value: {value} ")


def highest_qty():
    """
    This function loops through the objects in the shoe_list.
    Finds the shoe with the highest quantity attribute
    Prints out the shoe name and stock value and that this shoe
    should be on sale

    """
    stock_maximum = 0
    shoe_product_maximum = ""
    shoe = 0

    # loop through shoe objects in shoe_list to find the shoe with the highest quantity attribute
    while shoe < len(shoe_list):
        if shoe_list[shoe].quantity > stock_maximum:
            stock_maximum = shoe_list[shoe].quantity
            shoe_product_maximum = shoe_list[shoe].product
            shoe_max_position = shoe
        else:
            stock_maximum = stock_maximum
            shoe_product_maximum = shoe_product_maximum
        shoe += 1

    # prints the name of the shoe with the highest quantity attribute and its quantity
    print(f"The product with the most stock is: {shoe_product_maximum} with {stock_maximum} shoes")
    print("These shoes are on sale")


#==========Main Menu=============

# main menu for operating the code

# warehouse_management variable used to decide when to end the program
warehouse_management = True

# print welcome statement
print("Welcome to the Nike warehouse management system")
# read in shoe data from "inventory.txt" file
read_shoes_data()

# start while loop and ask user what they would like to do
while warehouse_management:

    print("\nPlease chose from numbers 1-7 below:")

    instruction = input("What would you like to do?\n"
                        "1:   View all stock\n"
                        "2:   Restock and existing show\n"
                        "3:   Search for a shoe\n"
                        "4:   Calculate and print out the value of all shoes\n"
                        "5:   Find the shoe on sale\n"
                        "6:   Order a new shoe\n"
                        "7    Exit\n")

    # Execute instruction by calling the necessary function based on user input
    if instruction == "1":
        view_all()
    elif instruction == "2":
        re_stock()
    elif instruction == "3":
        search_shoe()
    elif instruction == "4":
        value_per_item()
    elif instruction == "5":
        highest_qty()
    elif instruction == "6":
        capture_shoes()
    elif instruction == "7":
        print("Shutting down...")
        warehouse_management = False
    else:
        print("\nInvalid input")

