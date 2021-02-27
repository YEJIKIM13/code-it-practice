grades = {}

# key - value 데이터 삽입
grades["레리"] = 100
grades["데이비드"] = 80
grades["조"] = 70

print(grades)  # 딕셔너리 출력

# 한 키에 여러 밸류 저장 시도
grades["레리"] = 90

print(grades)  # 딕셔너리 출력

# key 를 이용해서 value 탐색
print(grades["레리"])
print(grades["데이비드"])

# key 를 이용한 삭제
grades.pop("레리")  # 삭제하는 대상의 value 를 리턴

print(grades)  # 딕셔너리 출력
