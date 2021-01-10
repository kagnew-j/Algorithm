#chapter 4_data structure
#problem_13_palindrome 회문

# 순차 탐색
def palindrome(s):
    """
    큐와 스택을 사용한 회문 확인 함수
    입력 : 문자열 s
    출력 : TF
    """
    qu = []
    st = []
    # 큐와 스택에 알파벳 문자 삽입
    for x in s :
        if x.isalpha(): # 해당 문자가 알파벳인지 확인(숫자, 공백, 특수문자 제외)
            qu.append(x.lower()) 
            st.append(x.lower()) 
    # 큐와 스택에서 문자 추출하며 비교
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

print(palindrome("wow"))
# True
print(palindrome("Madam, I'm Adam."))
# True
print(palindrome("Madam, I am Adam."))
# False

# exercise 13-1
# palindrom without queue and stack
def palindrome_for(s):
    """
    회문 확인 함수
    입력 : 문자열 s
    출력 : TF
    """
    # 알파벳 정제
    string = ""
    for x in s:
        if x.isalpha():
            string += x.lower()
    # 인덱스 활용 가운데로 좁여가며 비교
    back = 0
    for front in range(len(string)//2):
        back -= 1
        if string[front] != string[back]:
            return False
    return True

print(palindrome_for("wow"))
print(palindrome_for("Madam, I'm Adam."))
print(palindrome_for("Madam, I am Adam."))

# book answer
def palindrome_book(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha() == False :
            i += 1
        elif s[j].isalpha() == False :
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True

print(palindrome_book("wow"))
print(palindrome_book("Madam, I'm Adam."))
print(palindrome_book("Madam, I am Adam."))