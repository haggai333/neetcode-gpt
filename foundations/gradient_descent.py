class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x=init
        for _ in range(iterations):
            x-=(learning_rate*(x*2))
        return round(x,5)