car_name = "Volvo" #global variable

def my_function():
    car_name = "Toyota" #local variable
    global model
    model = "Corolla" #local variable
    print(car_name)

my_function()

print(model)