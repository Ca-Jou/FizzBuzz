class FizzBuzz:

    @staticmethod
    def answer(n):
        if n <= 0:
            raise ValueError
        if n % 3 == 0  and n % 5 == 0:
            return 'FizzBuzz'
        elif n % 3 == 0:
            return 'Fizz'
        elif n % 5 == 0:
            return 'Buzz'

