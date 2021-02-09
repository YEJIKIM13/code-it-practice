# n번째 피보나치 수를 찾아주는 함수 fib_memo을 작성해 보세요.
# fib_memo는 꼭 memoization 방식으로 구현하셔야 합니다!

def fib_memo(n, cache):
    # 베이스 케이스
    if n < 3:
        return 1
    
    # 이미 n번째 피보나치를 계산했으면 저장된 값을 바로 리턴
    if n in cache:
        return cache[n]
    # 아직 n번째 피보나치 수를 계산하지 않았으면 계산한 후 cache에 저장
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    
    # 계산한 값 리턴
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))