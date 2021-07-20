# 23분

# title()는 문자의 첫단어를 대문자로 바꿔준다.
# capitalize()는 단어 전체의 첫 단어를 대문자로 바꿔준다.
def solution(s):
    s = s.lower()
    answer = ''
    temp = s.split(" ")
    print(temp)
    for i in range(len(temp)):
        answer += temp[i].capitalize()
        answer += " "
    answer = answer[0: len(answer) -1]
    return answer