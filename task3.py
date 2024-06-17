class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}")
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "lion", "roar")

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "elephant", "trumpet")

class Girraffe(Animal):
    def __init__(self, name):
        super().__init__(name, "giraffe", "bleat")

animal1 = Lion("Simba")
animal2 = Elephant("Dumbo")
animal3 = Girraffe("Melman")

animal_list = [animal1, animal2, animal3]
for i in animal_list:
    i.make_sound()
#Recursive Function: (a function that calls itself)
#Write a recursive function called factorial(n) that calculates the 
#factorial of a given positive integer n. Factorial of 4 = 4*3*2*1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
#List Comprehension:
#Generate a list of even numbers between 4 and 30 (inclusive) using list comprehension (in one line)

even_numbers = [x for x in range(4, 31) if x % 2 == 0]

print(even_numbers)

#Find the Largest Item:
#Given a list of numbers, write a function to find the 
#largest item in the list without using list methods ([].method())



def largest_num(list1):
    largest = list1[0]  
    for i in list1:
        if i > largest:
            largest = i
    return largest

print(largest_num([5, 2, 3, 6]))

#Find Common Elements in Lists:
#Write a function called common_elements(list1, list2) that returns 
#a list of common elements between two input lists.
#Example: common_elements([1, 2, 3, 4], [3, 4, 5, 6]) should return [3, 4].
list2 = [1,2,3]
list4 = [3,4,5]


def common_elements(list2, list4):
    new_list = []
    for i in list2:
       for j in list4:
           if i == j:
               new_list.append(i)
               print(new_list)
common_elements(list2, list4)

#Count Vowels and Consonants:
##Write a function called count_vowels_consonants(word) that counts 
#the number of vowels and consonants in a given word.
#Example: count_vowels_consonants("hello") should return (2, 3)


def count_vowels(word):
  vowels = []
  consonant = []

  for i in word:
    if i == "a" or i =="e" or i == "i" or i == "o" or i =="u":
      vowels.append(i)
    else:
      consonant.append(i)

  print(len(vowels), len(consonant))
      

count_vowels("hello")
count_vowels("everyone")
#Check Palindrome:
#Write a function called is_palindrome(word) that checks whether a given word is a palindrome (reads the same forwards and backwards).
#Example: is_palindrome("racecar") should return True.
def is_palindrome(word):
    if word == word[::-1]:
        return True
print(is_palindrome("mom"))
#Find Prime Numbers in a Range:
#Write a function called find_primes(start, end) that takes a range of integers (start and end) and returns a list of prime numbers within that range.
#Example: find_primes(10, 30) should return [11, 13, 17, 19, 23, 29]
list_primes = []
def find_primes(start, end):

    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):  # Loop from 2 to the square root of i
                if i % j == 0:  # If i is divisible by j, it's not a prime
                    break
            else:
                list_primes.append(i)  # Append prime numbers to the list
    return list_primes
print(find_primes(0, 31))
#Dictionary Merge:
#Create a function called merge_dicts(dict1, dict2) that merges two dictionaries into a new dictionary. If keys overlap, prioritize values from dict2.
#Example: merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) should return {"a": 1, "b": 3, "c": 4}.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
def merge_dicts(dict1, dict2):
    merged_dicts = {}
    for key in dict1:
            merged_dicts[key] = dict1[key]
            for key in dict2:
                  merged_dicts[key] = dict2[key] #the key value will be overwritten in the second iteration
                  return merged_dicts
print(merge_dicts(dict1, dict2))

  








