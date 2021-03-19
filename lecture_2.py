# 1


class Book:
    def __init__(self, name, author, page_length):
        self.__name = name
        self.__author = author
        self.__page_length = page_length

    def info(self):
        print("-------")
        print("Book:", self.__name)
        print("Author:", self.__author)
        print("Pages:", self.__page_length)
        print("-------")


b1 = Book("booktitle", "john", 126)
b1.info()

b2 = Book("booktitle2", "james", 456)
b2.info()

# 2
print("-------")


class ExtendedList(list):
    def min(self):
        print(min(self))

    def max(self):
        print(max(self))


l = ExtendedList([1, 2, 3, 4])
l.min()
l.max()

# 3
print("-------")


class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        print("-------")
        print("Name:", self._name)
        print("Age:", self._age)
        print("-------")


class Dog(Animal):
    def __init__(self, breed, color, **kwargs):
        super().__init__(**kwargs)
        self._breed = breed
        self._color = color

    def info(self):
        print("-------")
        print("Name:", self._name)
        print("Age:", self._age)
        print("Breed:", self._breed)
        print("Color:", self._color)
        print("-------")


dog1 = Dog(name="Goofy", age=4, breed="Lablador", color="Gold")
dog1.info()

dog2 = Dog(name="Mimi", age=3, breed="Chihuahua", color="Brown")
dog2.info()

# 4
print("-------")


class CallMixin:
    def call(self):
        print("Dialing...", self._phone)


class Person:
    def __init__(self, fname, lname, phone):
        self.__fname = fname
        self.__lname = lname
        self._phone = phone

    def info(self):
        print("-------")
        print("Name:", self.__fname, self.__lname)
        print("Phone:", self._phone)
        print("-------")


class CallPerson(CallMixin, Person):
    pass


callp = CallPerson("Luka", "Urushadze", "555 123 456")
callp.info()
callp.call()