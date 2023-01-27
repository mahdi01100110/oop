import os
import re
import sys
import logging
from auth import User
from helper.enums import ExitCommand
from helper.exceptions import (
    PasswordLengthError,
    WrongUsernameException,
    TypePasswordException,
    TypeUsernameException
)
from unscramble_game import game
logging.basicConfig(
filename='shopping_list_log.log',
level=logging.INFO,
filemode='a',
format='%(name)s - %(message)s - %(process)s - %(asctime)s',datefmt='%H:%M:%S'
)

shopping_list: list = list()
shopping_list_item_counter: list = list()
stock: dict = dict()
counter: int = 0


class DataBase:
    """ this class is related to DataBase and wants a file name to read """
    def __init__(self, FileName: str):
        self.FileName = FileName

    def Database_reader(self):
        """ this method reads a file and return as list of elements of file """
        try:
            with open(self.FileName, encoding='utf-8') as reader:
                return reader.readlines()
        except IOError as file_error:
            logging.error(file_error, exc_info=True)


class Products:
    """ this class wants a list of product to split name and number and categorize theme : (supermarket,vegetables,fruit's)"""

    def __init__(self, products_list: list):
        self.products_list = products_list

    def purify_products_name(self):
        """ this method remove numbers in a list and return the list"""
        regex_of_numbers = r'[0-9]'
        just_name: list = list()
        for items_of_list in self.products_list:
            items_of_list = re.sub(regex_of_numbers, '', items_of_list)
            items_of_list = items_of_list.replace("by", "")
            items_of_list = items_of_list.replace("kg", "")
            items_of_list = items_of_list.replace("each", "")
            just_name.append(items_of_list.strip())
        return just_name

    def purify_products_prices(self):
        """ this method eliminate names and just returns a list that contain prices of products """
        regex_of_numbers = r'[a-z]'
        just_num: list = list()
        for items_of_list in self.products_list:
            items_of_list = re.sub(regex_of_numbers, '', items_of_list)
            items_of_list = items_of_list.replace("by", "")
            items_of_list = items_of_list.replace("kg", "")
            items_of_list = items_of_list.replace("each", "")
            just_num.append(items_of_list.strip())
        return just_num

    def categorize_products(self, category_choice: str):
        """

        Parameters
        ----------
        category_choice : this argument is the category chosen by user
            

        Returns the category that our user chose
        -------

        """
        if category_choice == "vegetables":
            for vegetables in self.purify_products_name():
                print(f"-> {vegetables}")

        elif category_choice == "fruits":
            for fruits in self.purify_products_name():
                print(f"-> {fruits}")

        elif category_choice == "supermarket":
            for supermarket in self.purify_products_name():
                print(f"-> {supermarket}")

    def generate_products_as_dict(self):
        """ this method use purified products name and prices to generate a dictionary of products name and prices """
        counter: int = 0
        for num in range(len(self.products_list)):
            stock[self.purify_products_name()[counter]]  =  self.purify_products_prices()[counter]
            counter += 1
        counter = 0
        return stock


vegetables_data: list = DataBase("vegetables.txt").Database_reader()
supermarket_data: list = DataBase("supermarket.txt").Database_reader()
fruits_data: list = DataBase("fruit's.txt").Database_reader()

vegetables = Products(vegetables_data)
vegetables_name = vegetables.purify_products_name()
vegetables_prices = vegetables.purify_products_prices()

fruits = Products(fruits_data)
fruits_name = fruits.purify_products_name()
fruits_prices = fruits.purify_products_prices()

supermarket = Products(supermarket_data)
supermarket_product_name = supermarket.purify_products_name()
supermarket_product_name = supermarket.purify_products_prices()

fruits.generate_products_as_dict()
vegetables.generate_products_as_dict()
supermarket.generate_products_as_dict()


class Cart:
    """ this is a shopping cart class to do stuff like add,edit,remove,display item in the shopping cart """

    def __init__(self, shopping_list: list, shopping_list_item_counter: list):
        self.shopping_list = shopping_list
        self.shopping_list_item_counter = shopping_list_item_counter

    def display_items(self):
        """ this method display the shopping list """
        number = 1
        print("item's :")
        print("\n")
        for itemFinder in shopping_list:
            print(f"> {number}. {itemFinder}")
            number += 1
        print("\n")

    def count_items(self):
        """ this method count the items in the list """
        print(f"length of your list: {len(self.shopping_list)}")

    def add_item(self, item_to_add: str, repetitive: bool):
        """

        Parameters
        ----------
        item_to_add: str : this is a item user wanna add it to the list
            
        repetitive: bool : we wanna check if it's repetitive dont add item to list, instead add it to item counter list
            

        Returns 
        -------

        """
        if repetitive is False:
            shopping_list.append(item_to_add)
        else:
            shopping_list_item_counter.append(item_to_add)

    def drop_item(self, item_to_drop: str):
        """

        Parameters
        ----------
        item_to_drop : this is a item user wanna remove it from list 
            

        Returns
        -------

        """
        if item_to_drop not in shopping_list:
            print("Item doesn't exit")
        else :
            shopping_list.remove(item_to_drop)

    def find_element(self, item_to_find: str):
        """

        Parameters
        ----------
        item_to_find : this is a item user wanna find it 
            

        Returns
        -------

        """
        if item_to_find in shopping_list:
            print("\n + item has been found +")
            print(f"number of element is > {shopping_list.index(item_to_find) + 1} <")
        else:
            print(" -item doesn't exist- ")

    def edit_item(self, item_to_edit: str,new_value: str):
        """

        Parameters
        ----------
        item_to_edit: str : this is a item user wanna edit
            

        Returns
        -------

        """
        if item_to_edit in shopping_list:
            index_of_item = shopping_list.index(item_to_edit)
            shopping_list[index_of_item] = new_value
        else:
            print("item doesn't exist")

    def change_priority(self, item_to_change_its_place: str, index_of_item: int):
        """

        Parameters
        ----------
        item_to_change_its_place: str : it's a item user wanna change its place
            
        index_of_item: int : this argument tells the program where user want to place the item
            

        Returns
        -------

        """
        if item_to_change_its_place in shopping_list:
            shopping_list.remove(item_to_change_its_place)
            index_of_item -= 1
            try:
                shopping_list.insert(index_of_item, item_to_change_its_place)
            except ValueError as ve:
                logging.error("the value is not correct !")
        else:
            print("item doesn't exist")

    def sales_invoice(self):
        """ this method print the sale invoice of our shopping list"""
        total_price: int = 0
        for item in shopping_list:
            count_of_item = shopping_list_item_counter.count(item)
            print(f"| {item} | price : {stock.get(item)} | count : {count_of_item} |")
            total_price += count_of_item * int(stock[item])
        print(f"total price is : {total_price}")


class Menu:
    """ this class just shows us the menu of the program """

    def __init__(self, shop_products: str):
        self.shop_products = shop_products

    def __str__(self):
        print(f"___ we sell  {self.shop_products} here ___")
        print("Menu :")
        print("0] show your list and exit the program")
        print("1] see your shopping cart ")
        print("2] see  your count of item in shopping list ")
        print("3] remove an item from your list ")
        print("4] search for your item and show it's place ")
        print("5] edit your item ")
        print("6] prioritize your item's ")
        print("7] show product's by category ")
        print("8] add item to your shopping list ")
        print("9] game ")
        print("10]show menu")
        print("11]sign in")


class Help:
    """ this is for display """
    def __init__(self, program_name: str, program_version: str, program_authors: str):
        self.program_name = program_name
        self.program_version = program_version
        self.program_authors = program_authors

    def __str__(self):
        print(">> enter quit to exit the program and see your list << \n")
        print(">> You can use edit, show, find and remove keyword's << \n")

    def clear_screen(self):
        """ this method clear the terminal """
        assert ('win32' in sys.platform), "This code runs on window only."
        return os.system('cls')
    
    def show_program_info(self):
        """ this program print program name,version,author """
        print(f"--{self.program_name}--")
        print(f"Author : {self.program_authors}")
        print(f"Version : {self.program_version}")


menu = Menu("vegetables/fruits/supermarket products")
menu.__str__()
mehdi_cart = Cart(shopping_list, shopping_list_item_counter)
mehdi = User()
shop_help = Help("shopping list", "1.0.0", "Mahdi Abdollahi")

while True:

    user_choice: str = input(" \n enter your choice from menu: ").lower().strip()
    logging.info(f"User run {user_choice}")
    shop_help.clear_screen()
    if user_choice == "0":
        shop_help.clear_screen()
        mehdi_cart.display_items()
        print('^ This is your final list ^')
        print("sale invoice : ")
        mehdi_cart.sales_invoice()
        print("** Thanks for shopping here **")
        break
    elif user_choice == '1':
        mehdi_cart.display_items()
    elif user_choice == '2':
        mehdi_cart.count_items()
    elif user_choice == 'help':
        shop_help.show_help()
    elif user_choice == '3':
        item_to_remove = input('please enter the item you want to remove : ')
        mehdi_cart.drop_item(item_to_remove)
        mehdi_cart.display_items()
        print("item removed")
    elif user_choice == '4':
        item_to_find = input('enter your element to start searching: ')
        mehdi_cart.find_element(item_to_find)
    elif user_choice == '5':
        mehdi_cart.display_items()
        item_to_edit = input("which item do you wanna edit :").strip().lower()
        new_value = input("enter the new value :")
        mehdi_cart.edit_item(item_to_edit,new_value)
    elif user_choice == '6':
        mehdi_cart.display_items()
        print("> change your item's place's <")
        item_to_change_place = input("enter your item : ")
        try:
            where_to_place = int(input("where ?"))
        except ValueError as ve:
            print("value is not correct !")
            logging.error(ve)
        mehdi_cart.change_priority(item_to_change_place, where_to_place)
        mehdi_cart.display_items()
    elif user_choice == "7":
        category_choice = input("which category ? vegetables,fruits or supermarket  : ").casefold().strip()
        if category_choice == "vegetables":
            vegetables.categorize_products(category_choice)
        elif category_choice == "fruits":
            fruits.categorize_products(category_choice)
        elif category_choice == "supermarket":
            supermarket.categorize_products(category_choice)
        else:
            print("Your category has not been found ‼ ‼ ‼ ‼")
    elif user_choice == '8':
        esc = False
        print("\n you can press exit,ex to exit the adding section ")
        while True:
            item_existence = False
            item_to_add = input("write your item to add : ").strip().casefold()
            for command in ExitCommand:
                if item_to_add == command.value:
                    esc = True
            if esc is True:
                break
            for item in stock:
                if item.strip() == item_to_add:

                    if item_to_add in shopping_list:
                        mehdi_cart.add_item(item_to_add, True)
                        item_existence = True
                    else:
                        mehdi_cart.add_item(item_to_add, False)
                        mehdi_cart.add_item(item_to_add, True)
                        print(f"> {item_to_add} < added to list")
                        print(f"You have {len(shopping_list)} item's in list")
                        item_existence = True
            if item_existence is False:
                print("item doesn't exist in the stock !")
    elif user_choice == '9':
        game()
    elif user_choice == '10':
        menu.__str__()
    elif user_choice == '11':        
        try:
            username = input('Username: ')
            password = input('password: ')
            mehdi.register(username, password)
            print("You are registered successfully.")
        except PasswordLengthError as e:
            logging.error(e)
    else:
        print("Your choice should be something between 0 and 11")
        logging.debug("user entered the wrong order")






