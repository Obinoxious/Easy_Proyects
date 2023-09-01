
    
def main():
    while True:
        Expression= input("What do you want to calculate? ")
        values = get_equation(Expression)
        result = calculation(values)
        print("The result is: ", result)

def calculation(values):
    A=int(values[0])
    B=values[1]
    C=int(values[2])

    if B == "*":
        return A*C
    elif B == "+":
        return A+C
    elif B == "-":
        return A-C
    elif B == "/":
        if C == 0:
            return "Indivisible by 0"
        else:
            return A/C
    else:
        print(" Please calculate only adition substraction multiplication or division.")

def read_ecuation(operation):
    numbers=[]
    operators=[]
    if operation[0].isdigit and operation[0]!= "*" and operation[0] != "+" and operation[0] !="-" and operation[0] !="/":
        if operation[1].isdigit and operation[1]!= "*" and operation[1] != "+" and operation[1] !="-" and operation[1] !="/":
            if operation[2].isdigit and operation[2]!= "*" and operation[2] != "+" and operation[2] !="-" and operation[2] !="/":
                if operation[3].isdigit and operation[3]!= "*" and operation[3] != "+" and operation[3] !="-" and operation[3] !="/":
                    if operation[4].isdigit and operation[4]!= "*" and operation[4] != "+" and operation[4] !="-" and operation[4] !="/":
                        if operation[5].isdigit and operation[5]!= "*" and operation[5] != "+" and operation[5] !="-" and operation[5] !="/":
                            if operation[6].isdigit and operation[6]!= "*" and operation[6] != "+" and operation[6] !="-" and operation[6] !="/":
                                    number=operation[0] + operation[1] + operation[2] + operation[3] + operation[4] + operation[5] + operation[6]
                                    numbers.append(number)
                                    return numbers
                            else:
                                    number=operation[0] + operation[1] + operation[2] + operation[3] + operation[4] + operation[5]
                                    numbers.append(number) 
                                    return numbers                     
                        else:
                                number=operation[0] + operation[1] + operation[2] + operation[3] + operation[4]
                                numbers.append(number)
                                return numbers
                    else:
                            number=operation[0] + operation[1] + operation[2] + operation[3]
                            numbers.append(number)
                            return numbers
                else:
                        number=operation[0] + operation[1] + operation[2]
                        numbers.append(number)
                        return numbers
            else:
                    number=operation[0] + operation[1]
                    numbers.append(number)
                    return numbers
        else:
                number=operation[0]
                numbers.append(number)
                return numbers
    else:
            numbers.append(operation[0])
            return numbers

def get_equation(Expression):
    numbers = []
    i=0
    operation = []
    for symbol in Expression:
        operation.append(symbol)
    for _ in range(len(operation)):
        character = read_ecuation(operation)
        numbers.append(character[0])
        z = int(len(character[0]))
        i=0
        while i < z:
            operation.remove(operation[0])
            operation.append("*")  
            i=i+1
    return numbers



if __name__ == "__main__":
    main()