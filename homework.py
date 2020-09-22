class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year


# objects of the class Movie
titanic = Movie('Титаник','реж. Джеймс Кэмерон','1997')
star_wars = Movie('Звездные войны','реж. Джордж Лукас','1977')
fight_club = Movie('Бойцовский клуб','реж. Дэвид Финчер','1999')

# don't delete this code
# it is here to check your results
# print(titanic.title)
# print(star_wars.year)
# print(fight_club.director)

class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0]+last_name+birth_year

# input_name = input()
# # input_l_name = input()
# # input_birth_year = input()
# # student1 = Student(input_name ,input_l_name ,input_birth_year)
# # print(student1.id)

class Person:
    def __init__(self, name):
        self.name = name

        # create the method greet here

    def greet(self):
        print(f'Hello, I am {self.name}!')


person = Person(input())
person.greet()


