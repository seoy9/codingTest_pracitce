def solution(s):
    answer = s

    if 'zero' in s:
        answer = answer.replace("zero", "0")
    if 'one' in s:
        answer = answer.replace("one", "1")
    if 'two' in s:
        answer = answer.replace("two", "2")
    if 'three' in s:
        answer = answer.replace("three", "3")
    if 'four' in s:
        answer = answer.replace("four", "4")
    if 'five' in s:
        answer = answer.replace("five", "5")
    if 'six' in s:
        answer = answer.replace("six", "6")
    if 'seven' in s:
        answer = answer.replace("seven", "7")
    if 'eight' in s:
        answer = answer.replace("eight", "8")
    if 'nine' in s:
        answer = answer.replace("nine", "9")

    return int(answer)