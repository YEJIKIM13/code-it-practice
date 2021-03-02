# 10. 완전 이진 트리 직접 구현하기
# 자식 노드와 부모 노드를 찾는 기능을 함수로 직접 구현
"""
get_left_child_index 함수는 리스트 complete_binary_tree 와 정수 index 를 파라미터로 받습니다.
그리고 왼쪽 자식 노드가 있는 인덱스를 찾아서 리턴해줍니다. 단, 왼쪽 자식 노드가 없을 경우, None 을 리턴합니다.
get_right_child_index 함수는 리스트 complete_binary_tree 와 정수 index 를 받습니다.
그리고 오른쪽 자식 노드가 있는 인덱스를 찾아서 리턴해줍니다. 단, 오른쪽 자식 노드가 없을 경우, None 을 리턴합니다.
get_parent_index 함수는 리스트 complete_binary_tree 와 정수 index 를 받습니다.
그리고 부모 노드가 있는 인덱스를 찾아서 리턴해줍니다. 단, 부모 노드가 없을 경우, None 을 리턴합니다.
실행 코드에서는 위 이미지에 있는 트리를 그대로 사용합니다.
"""
def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    parent_index = index // 2
    if 0 < parent_index < len(complete_binary_tree):
        return parent_index
    return None

def get_left_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    # 왼쪽 자식 노드의 인덱스가 유효한 범위 안에 있는 값인지를 확인
    left_child_index = index * 2
    if 0 < left_child_index < len(complete_binary_tree):
        return left_child_index
    return None

def get_right_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    right_child_index = (index * 2) + 1
    if 0 < right_child_index < len(complete_binary_tree):
        return right_child_index
    return None


# 실행 코드
root_node_index = 1  # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)