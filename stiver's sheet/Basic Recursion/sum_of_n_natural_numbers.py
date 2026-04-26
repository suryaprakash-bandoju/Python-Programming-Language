n = int(input())
total = 0
def sum_of_n_numbers(n):
    # total = n*(n+1)//2
    # return total
    if n == 1:
        return 1
    return n+sum_of_n_numbers(n-1)

result = sum_of_n_numbers(n)
print(result)