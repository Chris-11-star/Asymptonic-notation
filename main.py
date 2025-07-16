import time

def test(n):
    first = 0
    second = 0
    third = 0

    start = time.time()

    for i in range(n + 1):
        first += 1

    j = 1
    while j <= n + 1:
        second += 1
        j *= 2

    for i in range(100):
        third += 1

    end = time.time()
    total_time = end - start

    print(f"When n is {n}:")
    print(f"  First loop:  {first} times")
    print(f"  Second loop: {second} times")
    print(f"  Third loop:  {third} times")
    print(f"  Time taken:  {total_time:.6f} seconds")

test(10)
test(1000)
test(100000)
