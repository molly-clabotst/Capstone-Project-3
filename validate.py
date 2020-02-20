import re

# VALIDATE
def validate_name(name):
    while True:
        chars = name.replace(" ", "")
        if len(chars)<2:
            name = input('Please enter a valid name. ')
        else:
            break

    return name

def validate_Email(email):
    while True:
        # Regex basics https://www.tutorialspoint.com/python/python_reg_expressions.htm
        # Regex email https://www.tutorialspoint.com/Extracting-email-addresses-using-regular-expressions-in-Python
        searchObject = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email)

        if searchObject:
            return email
        else:
            email = input('Please enter a valid email. E.X. email@email.com ')

def validate_Art(name='string', price='0.00', available='no'):
    name= validate_Art_empty(name)
    price = validate_Art_price_float(price)
    available = validate_Art_available_chars(available)

    return name, price, available


def validate_Art_empty(name):
    while True:
        charsName =name.replace(" ","")
        if len(charsName)<1:
            name = input('Please enter a valid name. ')
        else:
            break

    return name

def validate_Art_price_float(price):
    while True:
        # Regex for currency https://stackoverflow.com/questions/4862827/how-does-one-find-the-currency-value-in-a-string#4862874
        searchObject =  re.search(r'([£$€])(\d+(?:\.\d{2})?)', price)
        if searchObject:
            return price
        else:
            price = input('Please enter a valid decimal with no spaces, E.X. $2.00. ')

def validate_Art_available_chars(available):
    while True:
        if available.upper()!="YES" and available.upper()!="NO":
            available = input('Please enter a valid availability response. E.X. yes, no. ')
        else:
            return available