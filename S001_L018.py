def double(x):
    return 2 *x
    
def root(x):
    return x**2
    
def negative(x):
    return -x
    
def div2(x):
    return x/2


number = 8
transformations = [double, root, div2, negative]
transformations2 = [root, root, div2, double]
tmp_return_value = number

print("*"*30)

for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print("Value after {} is {}".format(transformation.__name__ ,tmp_return_value))

print("*"*30)

tmp_return_value = number

for transformation in transformations2:
    tmp_return_value = transformation(tmp_return_value)
    print("Value after {} is {}".format(transformation.__name__ ,tmp_return_value))

print("*"*30)