def swap(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp
    return item1, item2

def swapSimple(item1, item2):
    return item2, item1

def invoke_swap():
    number1 = 10
    number2 = 20
    print(f"Before swapping: value of number1= {number1} and number2={number2}")

    number1, number2 = swapSimple(number1, number2)
    print(f"After swapping: value of number1= {number1} and number2={number2}")

invoke_swap()