# 파이썬 리스트 생성
trending = []

# 특정 위치에 데이터 삽입
trending.insert(0, "2월 일정")
trending.insert(1, "코드잇 자료구조 공부")
trending.insert(2, "알고리즘 공부")
trending.insert(3, "백준 문제풀기")

print(trending)  # 리스트 출력

# 괄호를 이용한 인덱스 접근
print(trending[0])
print(trending[1])

trending[0] = "3월 일정"

print(trending)

# in 을 이용한 탐색
print("3월 일정" in trending)
print("4월 일정" in trending)

# del 을 이용한 삭제
del trending[3]

print(trending)
