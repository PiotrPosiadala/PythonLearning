text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)

word = "words"
print(f(word))

#mozna uzywac filter oraz map - zalezy czy zwraca true czy dla kazdego elementu mamy cos obliczyc
print(list(map(f, text_list)))
print(list(map(lambda x: len(x), text_list)))
