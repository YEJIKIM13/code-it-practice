finished_classes = set()

# 데이터 저장
finished_classes.add("자료구조")
finished_classes.add("알고리즘")
finished_classes.add("네트워크")
finished_classes.add("운영체제")

print(finished_classes)  # 세트 출력

# 중복 데이터 저장 시도
finished_classes.add("자료구조")

print(finished_classes)  # 세트 출력

# 데이터 탐색
print("알고리즘" in finished_classes)
print("프로그래밍 기초" in finished_classes)
print("알고리즘 " in finished_classes)

# 저장한 데이터 삭제
finished_classes.remove("운영체제")

print(finished_classes)  # 세트 출력