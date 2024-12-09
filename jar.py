class Jar:
    def __init__(self, capacity=12):
        # Valida que a capacidade é um número inteiro não negativo
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Retorna uma string com o número de cookies
        return "🍪" * self._size

    def deposit(self, n):
        # Adiciona cookies ao jarro, verificando o limite de capacidade
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in the jar for that many cookies.")
        self._size += n

    def withdraw(self, n):
        # Remove cookies do jarro, verificando se há cookies suficientes
        if self._size < n:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self._size -= n

    @property
    def capacity(self):
        # Retorna a capacidade do jarro
        return self._capacity

    @property
    def size(self):
        # Retorna o número atual de cookies no jarro
        return self._size
