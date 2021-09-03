def add_up (num1, num2): #paramaters (num1, num2) this is a new function
    return num1 + num2 

(add_up (7, 3))

print(add_up (123, 480))

balance = 1000
pin = 1234

def atm_function(pin_entered, amount):
    global balance 
    if pin_entered == pin:
        print ("Access granted")
        if amount <= balance:
            print(f"You may withdraw that amount {amount}")
            balance -= amount 
            print ("Your new balance is {}. Thankyou for using this bank".format(balance))
    elif amount > balance:
        print("You don't have enough")
    else:
        print ("That was incorrect")

atm_function(1234, 333)





def multiply_by_nine_fifths(celcius):
    return celcius * (9/5)

def get_fahrenheit(celcius):
    return multiply_by_nine_fifths(celcius) + 32 #calls function

# print ("The temperature is {}° F".format(get_fahrenheit(9)))
print(get_fahrenheit(20))

