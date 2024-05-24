from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x:x*4)
    answer = "".join(numbers)
    if answer[0]=='0': answer = '0'
    return answer