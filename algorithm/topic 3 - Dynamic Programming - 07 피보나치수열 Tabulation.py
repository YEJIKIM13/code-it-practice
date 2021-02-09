# n번째 피보나치 수를 찾아주는 함수 fib_tab을 작성해 보세요.
# fib_tab는 꼭 tabulation 방식으로 구현하셔야 합니다!

# 사전형, 인덱스 아님
# def fib_tab(n):
#     fib_table = {}
#     fib_table[1] = 1
#     fib_table[2] = 1
#     if n > 2:
#         for i in range(3, n+1):
#             fib_table[i] = fib_table[i-1] + fib_table[i-2]
#     return fib_table[n]

def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))