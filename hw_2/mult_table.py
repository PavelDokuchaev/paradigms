def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            result = i * j
            print(f"{i} * {j} = {result}")


n = 9
multiplication_table(n)

# Выбрана процедурная парадигма, потому что мы произвдим конкретные дейстия.
