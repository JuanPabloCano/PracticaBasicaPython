class Fibonacci:

    def fibonacci_sequence(self, n):
        if n > 1:
            return self.fibonacci_sequence(n - 1) + self.fibonacci_sequence(n - 2)
        return n
