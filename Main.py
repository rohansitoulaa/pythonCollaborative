import Addition
import div
import multiplication
import Subtration
def Main():
    operator = input("Enter operator (+, -, *, /): ")
    match operator:
        case "+":
            add = Addition.Addition()
            print("The added value is", add)
        case "-":
            sub = Subtration.Sub()
            print("The sub is ", sub)
        case "*":
            mul = multiplication.Multiply()
            print("The multiplication is ", mul)
        case "/":
            divison = div.divide()
            print("The divison is ", divison)
        case _:
            return "Invalid operator"
Main()