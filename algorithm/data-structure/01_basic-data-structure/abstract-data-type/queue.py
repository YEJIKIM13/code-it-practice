# deque 는 파이썬 collections 모듈에서 가지고 온다
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("승희")
queue.append("지호")
queue.append("예원")
queue.append("효정")
queue.append("미현")

print(queue)  # 큐 출력

# 큐의 가장 앞 데이터에 접근
print(queue[0])  # 삭제하려는 데이터를 리턴함 

# 큐의 맨 앞 데이터 삭제
print(queue.popleft())

print(queue)  # 큐 출력
