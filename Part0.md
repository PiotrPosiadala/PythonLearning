# Python

https://www.programiz.com/python-programming/keyword-list

## Słowa kluczowe

| `False`  |  `class`   | `finally` |    `is`    | `return` |
| :------: | :--------: | :-------: | :--------: | :------: |
|  `None`  | `continue` |   `for`   |  `lambda`  |  `try`   |
|  `True`  |   `def`    |  `from`   | `nonlocal` | `while`  |
|  `and`   |   `del`    | `global`  |   `not`    |  `with`  |
|   `as`   |   `elif`   |   `if`    |    `or`    | `yield`  |
| `assert` |   `else`   | `import`  |   `pass`   |          |
| `break`  |  `except`  |   `in`    |  `raise`   |          |

## Typy

### Set

```python
    a = {1,3,2,3,4,5,4,5,3,2}

    print("a=",a,"and is ", type(a))
```

> a= {1, 2, 3, 4, 5} and is  <class 'set'>

### Dictionary

Tworzy słownik - wywołanie d[1] oznacza tłumaczenie pierwszego miejsca w słowniku.

```python
d = {1:'value','key':2}
print(d, "is ", type(d))
print(d[1])
print(d['key'])
```

## Print

### Otwarcie pliku i zapisanie do niego za pomocą print'a

```python
sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()
```

### Print z odpowiednimi odstępami i zakończeniem

```python
print("Proszę podać liczbę")
a = input()
print("a=",a,"lubieplacki", sep='___',end='\n\n')
```

### Print tak jak w C

```python
x=2
y=3
print("Wartość x = {}, wartość y = {}, a ich suma to {}".format(x,y,x+y))
```



## Instrukcje

### if...elif...else

Nic nadzwyczajnego

### for

```python
numbers = [2,4,6,8,10]
sum = 0

for val in numbers:
    sum = sum + val
    print("sum is ", sum, "thanks ", val)
```

### range()

```python
# Output: range(0, 10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))
```

### range() + for

```python
nationalities = ["Czechy", "Francja", "islandia"]
for i in range(len(nationalities)):
    print("Bylem w ", nationalities[i])
```

## Funkcje

```python
def echo():
    """To jest funkcja echa"""
    print("Podaj imię")
    name=input()
    print("Podałeś imię: ", name)
```

Wypisanie tego komentarza na początku:

```python
print(echo.__doc__)
```

Return tak jak zawsze

### Asteriks

Pozwala na podanie dowolnej, większej ilości argumentów.

```python
def hello( *names):
    for name in names:
        print("Witaj ", name)

if __name__== '__main__':
    hello("Piotr", "Angela")
```

### Funkcje rekursywne (recursive)

```python
def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))
```

### Funkcje lambda

Używane pomocniczo na krótki czas.

```
triple = lambda x: x*3

a = 2
print(triple(a))
```

```python
# Program to filter out only the even items from a list	
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)
```



### Wbudowane funkcje Pythona

https://www.programiz.com/python-programming/methods/built-in



