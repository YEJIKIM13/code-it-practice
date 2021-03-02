# 15. in-order 순회 구현하기
# in-order 순회 기본 동작들
"""
왼쪽 부분 트리를 in-order 순회한다
현재 노드의 데이터를 출력한다
오른쪽 부분 트리를 in-order 순회한다
"""
# in-order 순회를 하기위해 만든 traverse_in_order 함수를 직접 구현해 보세요
# traverse_in_order 함수는 트리의 root 노드를 파라미터로 받습니다.
# 그리고 그 트리를 in-order 순회하면서 각 노드의 데이터를 출력합니다.
"""
<재귀함수>
그러면 어떻게 None 이 되는가? 계속 왼쪽으로 가다보면 leaf 노드가 나온다. leaf 의 lef t나 child 는 None 이기 때문에 끝이 난다.
조건을 만족하지 않으면 if 문은 실행되지 않기에! 
"""


class Node:
    """이진 트리 노드를 나타내는 클래스"""

    def __init__(self, data):
        """이진 트리 노드는 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None


def traverse_inorder(node):
    """in-order 순회 함수"""
    """
    그런데 이때 traverse_inorder 함수에 넘어온 파라미터 node가 None인 경우를 생각해보세요. 
    그럼 현재 노드의 왼쪽 자식 노드 또는 오른쪽 자식 노드가 없다는 뜻이고, 
    이 경우에는 더이상 in-order 순회를 진행할 필요가 없습니다. 
    그러니까 이 경우에는 traverse_inorder 함수에서 아무것도 하지 않아도 된다는 뜻이죠.
    """
    # 어차피 왼쪽 오른쪽 보는 건 그 노드 가서 생각할 문제니까
    if node is not None:
        traverse_inorder(node.left_child)  # 재귀적으로 왼쪽 부분 트리 순회
        print(node.data)  # 데이터 출력
        traverse_inorder(node.right_child)  # # 재귀적으로 오른쪽 부분 트리 순회


# 여러 노드 인스턴스 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스들 연결
node_F.left_child = node_B
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

# 노드 F를 root 노드로 만든다
root_node = node_F

# 만들어 놓은 트리를 in-order 로 순회한다
traverse_inorder(root_node)