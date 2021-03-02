# 지난 챕터에서 만들었던 링크드 리스트 클래스도 한 번 해시 테이블에서 사용할 수 있게 바꿔보자, 더블리 링크드 리스트 이

# Node 클래스
# 링크드 리스트 노드가 변수 data 대신 key 와 value 를 저장
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스

# LinkedList 클래스
# 링크드 리스트 클래스에서는 필요한 메소드들만 가지고 와서 쓰면 된다. 노드 클래스랑 마찬가지로 그대로 사용할 수는 없고 조금씩 고쳐서 써야함
# __init__메소드는 바꾸지 않아도 됨
class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    # 탐색 메소드
    def find_node_with_key(self, key):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        """특정 key 를 가지고 있는 노드를 찾음, 링크드 리스트 처음부터 끝까지 돌면서 원하는 key 를 갖는 노드 리턴하도록 수"""
        # 코드에서는 기존에 data 변수를 다 key 로 바꿔줌

        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

    # 추가 (맨 뒤 삽입) 메소드
    def append(self, key, value):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(key, value)

        # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 이미 노드가 있으면
        else:
            self.tail.next = new_node  # tail의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # tail 업데이트

    # 삭제 메소드
    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        # 원래 링크드 리스트 삭제 메소드에서 노드 삭제 시 삭제하는 노드의 데이터를 리턴했는데, 이 부분을 빼주자
        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    # 문자열 메소드
    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        # 출력 형식만 조금 바꿔줬음

        res_str = ""

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str