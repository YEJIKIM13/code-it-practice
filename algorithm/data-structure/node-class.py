# 노드 객체 생성 위한 노드 클래스 정의
class Node:
    """링크드 리스트의 노드 클래스"""
    # 객체 생성시 호출되는 __init__ 메소드 쓰기
    # 첫 번째 파라미터는 self, 노드를 생성할 때 이 노두가 저장할 정보 받아오자

    def __init__(self, data):
        # 인스턴스 변수들의 초기값 설정
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스, 일단 비워둠

# 데이ㅓ 2, 3, 5, 7, 11을 담는 노드들 생성, 아직은 서로 연결안됨
head_node = Node(2) # 2가 data 파라미터로 들어가고 self.data 속성에 data, 즉 2가 저장됨
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node # iterate - 반복, 반복문으로 리스트를 돌 때 도움을 주는 역할을 하는 값

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next # 갱신