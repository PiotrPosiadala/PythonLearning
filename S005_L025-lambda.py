#Lambda - może przyjąć dowolną ilość argumentów 

def double(x):
    return x*2

x = 10
x = double(x)
print(x)

x = 10
f = lambda x: x*2       #po dwukropku tylko jedno wyrazenie
print(f(x))


#---#
def power(x,y):
    return x**y

x = 5
y = 3
print(power(x,y))

f = lambda x,y: x**y
print(f(x,y))
#---#

list_numbers = [1,2,3,4,11,15,20,21]

def is_odd(x):
    return x % 2 != 0

print(is_odd(7), is_odd(4))

#---#

#funkcja filter wykona dana funkcje dla kazdego elementu na lisice
# dzieki lambda dostajemy cos jak wyrazenie funkcyjne, funkcja jest anonimowa, nie ma zadnej nazwy
filtered_list = list(filter (is_odd, list_numbers))
print(filtered_list)

filtered_list = list(filter(lambda x: x % 2 != 0, list_numbers))
print(filtered_list)
#---#


# skupienie kilku liniek kodu w jednej
print(list(filter(lambda x: x % 2 != 0, list_numbers)))

# generowanie sobie funkcji
def generate_multiply_function(n):
    return lambda x: n * x

mul_2 = generate_multiply_function(2)
mul_3 = generate_multiply_function(3)

print(mul_2(13), mul_3(8))

