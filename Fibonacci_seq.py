#! python3
# Fibonacci_seq.py - Enter a number and have the program generate the Fibonacci sequence to that number
#                    or to the Nth number.

import time


def Fibonacci_seq_Nth(n):
    seq = [1, 1]
    for N in range(1, n + 1, 1):
        seq.append(seq[-1] + seq[-2])
    return seq[:-3]


def Fibonacci_seq_to_N(n):
    seq = [1, 1]
    while seq[-1] + seq[-2] <= n:
        seq.append(seq[-1] + seq[-2])
    return seq[:]


def main():
    try:
        n = int(input('Please enter a positive integer --> '))
    except NameError:
        print('Error!')
    else:
        start_time = time.time()
        print('The Fibonacci sequence to the nth number is %s' % (Fibonacci_seq_Nth(n)))
        print('The Fibonacci sequence to that number is %s' % (Fibonacci_seq_to_N(n)))
        print('This program took %d seconds to finish.' % (round(time.time() - start_time, 3)))


if __name__ == '__main__':
    main()
