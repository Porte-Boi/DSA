def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2) + fib(n-1)

if __name__ == "__main__":
   # print(find_sum(3))
    print(fib(4))