# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash_add(pet_shop, sum_to_add):
    sum_to_add + pet_shop["admin"]["total_cash"]
    cash_total = cash_total + sum_to_add
    return cash_total

def add_or_remove_cash(pet_shop, sum_to_sub):
    return add_or_remove_cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number):
    sold = pet_shop["admin"]["pets_sold"] + number
    return sold

def get_stock_count(pet_shop):
    count = 0
    for stock in pet_shop["pets"]:
        count += 1
    
    return(count) 

def get_pets_by_breed(pet_shop, breed):
    for pet in pet_shop:
        for name in pet:
            p
            pets += 1
    return pets
        
def test_pets_by_breed(pet_shop, breed):
    for pet in pet_shop:
        if pet == breed:
            return 

def find_pet_by_name(pet_shop, pet_name):
    found_pet = None
    for pet in pet_shop:
        if pet["name"] == pet_name:
            found_pet = pet
    
    return found_pet

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop:
        if pet["name"] == pet_name:
            return pet
        else:
            return "Not found"


def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop:
        if pet["name"] == pet_name:
            del pet_shop["name"]

def add_pet_to_stock(pet_shop, new_pet):
    count = 0
    new_pet = 0
    for stock in pet_shop["pets"]:
        count += 1
        return pet_shop.append(new_pet)

def get_customer_cash(pet_shop, number):
    for customer in pet_shop:
        if customer['cash'] == number:
            return customer


        

   