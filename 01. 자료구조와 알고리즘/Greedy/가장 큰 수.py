def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    if numbers[0] == '0': return '0'
    return ''.join(numbers)
