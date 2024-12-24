def solution_ex1 (num1,num2):
    return num1+num2

def solution_ex2 (my_string):
    return my_string[::-1]

def solution_ex3 (my_string):
    return len(my_string)

def solution_ex4 (my_string,second_string):
    return my_string + " " + second_string

def solution_ex5 (is_wovel):
    if is_wovel.lower() in 'aeiou':
        return True
    
    return False

def solution_ex6 (my_string):
    return my_string[-1] + my_string[1:-1] + my_string[0]

def solution_ex7 (my_string):
    return my_string.upper()

def solution_ex8 (num1,num2):
    return num1 * num2

def solution_ex9 (num1):
    if num1 % 2 == 0 :
        return True
    
    return False

def solution_ex10(my_string):
    return my_string[:3]

def solution_ex11(name,age):
    message = f"My name is {name} and I am {age} years old."
    return message

def solution_ex12(my_string):
    return my_string[2:6]

def solution_ex13(num_str):
    return int(num_str)

def solution_ex14(my_string):
    return my_string * 3

def solution_ex15(num1,num2):
    quotient = num1 // num2
    remainder = num1 % num2
    message = f"Quotient: {quotient} , Remainder: {remainder}"
    return message

def solution_ex16 (num1,num2):
    return num1 / num2

def solution_ex17 (my_string):
    return my_string.count('o')

def solution_ex20 (num1,num2):
    return num1 ** num2

def solution_ex21 (palindrom):
    return palindrom == palindrom[::-1]

def solution_ex22 (anagram_part1,anagram_part2):
    return sorted(anagram_part1.lower()) == sorted(anagram_part2.lower())

num1 = 5
num2 = 2
my_string = "Hello world"
second_string = "Hello"
name = "Chingiz"
age = "99"
num_str = "42"
palindrom = "racecar"
anagram_part1 = "yssr"
anagram_part2 = "sysr"
is_wovel = "w"

print (solution_ex1 (num1,num2))
print (solution_ex2 (my_string))
print (solution_ex3 (my_string))
print (solution_ex4 (my_string,second_string))
print (solution_ex5 (is_wovel))
print (solution_ex6 (my_string))
print (solution_ex7 (my_string))
print (solution_ex8 (num1,num2))
print (solution_ex9 (num1))
print (solution_ex10(my_string))
print (solution_ex11(name,age))
print (solution_ex12(my_string))
print (solution_ex13(num_str))
print (solution_ex14(my_string))
print (solution_ex15(num1,num2))
print (solution_ex16 (num1,num2))
print (solution_ex17(my_string))
#solution ex 18 
esc_string = "She said, \"Hello!\""
print (esc_string)
#solution ex 19
multi_line_string = """This is line 1
This is line 2
This is line 3"""
print (multi_line_string)
print (solution_ex20 (num1,num2))
print (solution_ex21 (palindrom))
print (solution_ex22 (anagram_part1,anagram_part2))