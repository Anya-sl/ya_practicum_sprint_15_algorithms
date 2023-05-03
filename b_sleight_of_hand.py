# 86613674

def get_scores(pushed_keys: int, str_numbers: str) -> int:
    scores = 0
    numbers = {num: 0 for num in range(1, 10)}
    for num in str_numbers:
        if num.isalnum():
            numbers[int(num)] += 1
    for value in numbers.values():
        if 0 < value <= pushed_keys:
            scores += 1 
    return scores


if __name__ == '__main__':
    pushed_keys = int(input()) * 2
    str_numbers = ''
    for i in range(4):
        str_numbers += input()
    print(get_scores(pushed_keys, str_numbers))
