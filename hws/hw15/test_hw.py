import unittest

import hw

class TestExercise(unittest.TestCase):
    
    # Test for Exercise 1: Pizza
    def test_add_ingredient(self):
        pizza = hw.Pizza()
        pizza.add_ingredient("cheese")
        self.assertIn("cheese", pizza.ingredients)
        with self.assertRaises(ValueError):
            pizza.add_ingredient("cheese")

    # Test for Exercise 2: Elevator
    def test_elevator_movement(self):
        elevator = hw.Elevator()
        elevator.go_up()
        self.assertEqual(elevator.get_current_floor(), 1)
        elevator.go_down()
        self.assertEqual(elevator.get_current_floor(), 0)
        elevator.go_down()
        self.assertEqual(elevator.get_current_floor(), 0)

    # Test for Exercise 3: Stack
    def test_stack_operations(self):
        stack = hw.Stack()
        self.assertTrue(stack.is_empty())
        stack.push("item")
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), "item")
        with self.assertRaises(IndexError):
            stack.pop()

    # Test for Exercise 4: BankAccount
    def test_bank_account_operations(self):
        bank_account = hw.BankAccount(500)
        self.assertEqual(bank_account.check_balance(), 500)
        bank_account.deposit(200)
        self.assertEqual(bank_account.check_balance(), 700)
        bank_account.withdraw(300)
        self.assertEqual(bank_account.check_balance(), 400)
        with self.assertRaises(ValueError):
            bank_account.withdraw(500)

        # Test for Exercise 5: Person
    def test_birthday(self):
        person = hw.Person("Alice", 30)
        self.assertEqual(person.age, 30)
        person.birthday()
        self.assertEqual(person.age, 31)
        with self.assertRaises(ValueError):
            hw.Person("Bob", -1)

    # Test for Exercise 6: Animal, Dog, Cat
    def test_animal_sounds(self):
        dog = hw.Dog()
        self.assertEqual(dog.sound(), "Woof")
        cat = hw.Cat()
        self.assertEqual(cat.sound(), "Meow")

    # Test for Exercise 7: Calculator
    def test_calculator_operations(self):
        self.assertEqual(hw.Calculator.add(2, 3), 5)
        self.assertEqual(hw.Calculator.subtract(2, 3), -1)
        self.assertEqual(hw.Calculator.multiply(2, 3), 6)
        self.assertEqual(hw.Calculator.divide(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            hw.Calculator.divide(6, 0)

    # Test for Exercise 8: Car
    def test_car(self):
        car = hw.Car(60, 10000)
        self.assertEqual(car.speed, 60)
        self.assertEqual(car.mileage, 10000)
        with self.assertRaises(ValueError):
            hw.Car(-10, 10000)
        with self.assertRaises(ValueError):
            hw.Car(60, -10000)

    # Test for Exercise 9: Student, Course
    def test_course_enrollment(self):
        student = hw.Student("Alice")
        course = hw.Course()
        self.assertEqual(len(course.students), 0)
        course.enroll(student)
        self.assertEqual(len(course.students), 1)
        self.assertIn(student, course.students)

    # Test for Exercise 10: Flight
    def test_flight(self):
        flight = hw.Flight("Paris", "10:00")
        self.assertEqual(flight.destination, "Paris")
        self.assertEqual(flight.departure, "10:00")
        flight.add_passenger("Alice")
        self.assertIn("Alice", flight.passengers)
        flight.change_destination("Berlin")
        self.assertEqual(flight.destination, "Berlin")
        flight.delay(1)
        self.assertEqual(flight.departure, "11:00")
    
    # Test for Exercise 11: Book, Library
    def test_library(self):
        book = hw.Book("1984", "George Orwell")
        library = hw.Library()
        library.add_book(book)
        self.assertIn(book, library.books)
        found_book = library.find_by_title("1984")
        self.assertEqual(found_book, book)

    # Test for Exercise 12: Matrix
    def test_matrix(self):
        matrix1 = hw.Matrix([[1, 2], [3, 4]])
        matrix2 = hw.Matrix([[5, 6], [7, 8]])
        result = matrix1.add(matrix2)
        self.assertEqual(result.matrix, [[6, 8], [10, 12]])

    # Test for Exercise 13: Rectangle
    def test_rectangle(self):
        rectangle = hw.Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)
        self.assertEqual(rectangle.perimeter(), 14)
        self.assertFalse(rectangle.is_square())
        square = hw.Rectangle(4, 4)
        self.assertTrue(square.is_square())

    # Test for Exercise 14: Circle
    def test_circle(self):
        circle = hw.Circle(5)
        self.assertEqual(circle.area(), 78.53981633974483)
        self.assertEqual(circle.circumference(), 31.41592653589793)

    # Tests for Exercise 15: Triangle
    def test_triangle(self):
        triangle = hw.Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)
        self.assertEqual(triangle.perimeter(), 12)
        with self.assertRaises(ValueError):
            triangle = hw.Triangle(-1, 4, 5)
        with self.assertRaises(ValueError):
            triangle = hw.Triangle(10, 4, 5)

     # Tests for Exercise 17: MusicPlayer
    def test_music_player(self):
        player = hw.MusicPlayer()
        player.add_song("Song1")
        player.add_song("Song2")
        self.assertIn("Song1", player.playlist)
        self.assertIn("Song2", player.playlist)
        player.play_song()
        self.assertEqual(player.current_song, "Song1")
        player.next_song()
        self.assertEqual(player.current_song, "Song2")
        player.shuffle()
        self.assertIn(player.current_song, ["Song1", "Song2"])

    # Tests for Exercise 18: Product
    def test_product(self):
        product = hw.Product("Apple", 1, 10)
        self.assertEqual(product.check_stock(), 10)
        product.add_stock(5)
        self.assertEqual(product.check_stock(), 15)
        product.sell(7)
        self.assertEqual(product.check_stock(), 8)
        with self.assertRaises(ValueError):
            product.sell(10)

    # Tests for Exercise 19: VideoGame
    def test_video_game(self):
        game = hw.VideoGame("Game1", "Action", "PG")
        self.assertEqual(game.title, "Game1")
        self.assertEqual(game.genre, "Action")
        self.assertEqual(game.rating, "PG")
        game.change_rating("PG-13")
        self.assertEqual(game.rating, "PG-13")
        game.change_genre("Adventure")
        self.assertEqual(game.genre, "Adventure")

    # Tests for Exercise 20: School, Person, Teacher, Student
    def test_school(self):
        school = hw.School()
        teacher = hw.Teacher("Mr. Smith", 40)
        student = hw.Student("Alice", 12)
        school.add_teacher(teacher)
        school.add_student(student)
        self.assertIn(teacher, school.teachers)
        self.assertIn(student, school.students)
        self.assertIn(teacher, school.get_all())
        self.assertIn(student, school.get_all())

    # Tests for Exercise 21: Card, Deck
    def test_deck(self):
        deck = hw.Deck()
        self.assertEqual(deck.count(), 52)
        card = deck.deal()
        self.assertEqual(deck.count(), 51)
        deck.shuffle()
        self.assertNotEqual(card, deck.deal())

if __name__ == "__main__":
    unittest.main()