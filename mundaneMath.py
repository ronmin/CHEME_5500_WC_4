#! python
# mundaneMath.py - Calculates the sum of all even numbers between 1 and 100.

def main():
    summ = sum(range(2, 101, 2))
    return summ

if __name__ == '__main__':
    print('The sum of all even numbers between 1 and 100 is %s.' % (main()))
