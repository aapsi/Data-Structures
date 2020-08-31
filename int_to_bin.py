from Stack import Stack

def int_to_bin(n):
    s = Stack()
    while n > 0:
        rem = n % 2
        s.push(rem)
        n //= 2

    bin = ""
    while not s.is_empty():
         bin += str(s.pop())

    return bin

print(int_to_bin(242))
