import time
import math

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
    ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)


for formula in formulas_list:
    result_list = []
    print("Formula = {}".format(formula))
    start = time.time()

    for x in argument_list:
        result_list.append(eval(formula))
    
    print("Result list =  {} ... {} ".format(result_list[0],result_list[-1]))
    
    stop = time.time()
    duration = stop - start
    print("Duration: ", duration)

print("-"*30)

for formula in formulas_list:
    result_list = []
    print("Formula = {}".format(formula))
    start = time.time()

    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        result_list.append(eval(compiled_formula))
    
    print("Result list =  {} ... {} ".format(result_list[0],result_list[-1]))
    
    stop = time.time()
    duration = stop - start
    print("Duration: ", duration)