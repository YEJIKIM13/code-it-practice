# 노드 객체 생성 위한 노드 클래스 정의
class Node:
    """링크드 리스트의 노드 클래스"""

    # 객체 생성시 호출되는 __init__ 메소드 쓰기
    # 첫 번째 파라미터는 self, 노드를 생성할 때 이 노두가 저장할 정보 받아오자

    def __init__(self, data):
        # 인스턴스 변수들의 초기값 설정
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스, 일단 비워둠


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        # 인스턴스 변수들의 초기값 설정, 여기선 속성 두 가지
        self.head = None
        self.tail = None

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)  # 새 데이터 담을 노드 새로 하나 만들어주기

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:  # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    # 링크드 리스트 맨 끝에 노드 정보를 추가하는 메소드 작성
    # data - 우리가 추가하려는 데이터
    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 링크드 리스트에 데이터 추가
my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 링크드 리스트에 삽입
# 인덱스 2에 있는 노드의 다음 순서에 151을 삽입
node_2 = my_list.find_node_at(2)  # 인덱스 2에 있는 노드 접근
my_list.insert_after(node_2, 151)  # 2번 인덱스에 있는 node_2와 데이터 151을 넘겨줌

# 전체 링크드 리스트 출력
print(my_list)

# 헤드노드는 인스턴스 변수이기 때문에 메소드를 안 써도 가지고 올 수 있다.
head_node = my_list.head  # 헤드 노드 접근
my_list.insert_after(head_node, 9)  # 헤드 노드 뒤에 9 삽입

print(my_list)
