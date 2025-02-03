"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        pass
    
    def add_ingredient(self, ingredient):
        pass


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        pass

    def go_up(self):
        pass

    def go_down(self):
        pass

    def get_current_floor(self):
        pass


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass


"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self):
        pass


"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        pass

    def birthday(self):
        pass


"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        pass


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        pass

    @staticmethod
    def subtract(x, y):
        pass

    @staticmethod
    def multiply(x, y):
        pass

    @staticmethod
    def divide(x, y):
        pass


"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        pass


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student:
    def __init__(self, name):
        pass

class Course:
    def __init__(self):
        pass

    def enroll(self, student):
        pass

    def print_students(self):
        pass


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        pass

    def add_passenger(self, passenger):
        pass

    def change_destination(self, new_destination):
        pass

    def delay(self, delay_time):
        pass


"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        pass

class Library:
    def __init__(self):
        pass

    def add_book(self, book):
        pass

    def find_by_title(self, title):
        pass


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        pass

    def add(self, other):
        pass

    def subtract(self, other):
        pass

    def multiply(self, other):
        pass


"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def is_square(self):
        pass


"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        pass

    def area(self):
        pass

    def circumference(self):
        pass


"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class AbstractShape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(AbstractShape):
    def __init__(self, radius):
        pass

class Rectangle(AbstractShape):
    def __init__(self, height, width):
        pass

class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        pass

"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""
class MusicPlayer:
    def __init__(self):
        pass

    def add_song(self, song):
        pass

    def play_song(self):
        pass

    def next_song(self):
        pass

    def shuffle(self):
        pass


"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        pass

    def add_stock(self, quantity):
        pass

    def sell(self, quantity):
        pass

    def check_stock(self):
        pass


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        pass

    def change_rating(self, rating):
        pass

    def change_genre(self, genre):
        pass

    def display_details(self):
        pass


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Person:
    def __init__(self, name, age):
        pass

class Teacher(Person):
    pass

class Student(Person):
    pass

class School:
    def __init__(self):
        pass

    def add_teacher(self, teacher):
        pass

    def add_student(self, student):
        pass

    def print_all(self):
        pass

"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
class Card:
    def __init__(self, suit, rank):
        pass

class Deck:
    def __init__(self):
        pass

    def shuffle(self):
        pass

    def deal(self):
        pass

    def count(self):
        pass
