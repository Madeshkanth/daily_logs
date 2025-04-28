import calculation as c

def calculate(num1,num2):
    addition = c.add(num1,num2)
    subtraction = c.sub(num1,num2)
    multiplication = c.mul(num1,num2)
    division = c.div(num1,num2)

    print(f'Addition: {addition}\nSubtraction: {subtraction}\nMultiplication: {multiplication}\nDivision: {division}')

calulate(1,2)



