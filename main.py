from FizzBuzz import FizzBuzz

print("Welcome to FizzBuzz !")
print("Write an integer and press Return...")
number = input()

if FizzBuzz.check_input(number):
    print(FizzBuzz.answer(int(number)))

print("La bise !")
