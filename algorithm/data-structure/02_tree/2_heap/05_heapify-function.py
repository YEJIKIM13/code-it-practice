# 05. heapify 함수 구현
"""
heapify 함수는 파라미터로
* 완전 이진 트리를 나타내는 리스트, tree
* heapify 하려는 노드의 인덱스, index
* 그리고 트리 안에 있는 총 노드의 개수, tree_size 를 받습니다.

그리고 파라미터로 받은 tree 의 index 번째 노드가, 힙 속성을 유지하도록 트리 안의 노드들을 재배치합니다. (앞으로 “index" 번째 노드는 그냥 줄여서 “노드 index"라고 하겠습니다)
heapify 함수가 이런 기능을 하려면 아래와 같은 상세 작업을 순서대로 해야합니다.

1. 부모 노드(heapify 하려는 현재 노드), 왼쪽 자식 노드, 오른쪽 자식 노드, 이 3가지 노드 중에서 가장 큰 값을 가진 노드가 무엇인지 파악합니다.
2. (1)가장 큰 값을 가진 노드가 부모 노드라면 그 상태 그대로 둡니다. (2)가장 큰 값을 가진 노드가 자식 노드 중에 있다면 그 자식 노드와 부모 노드의 위치를 바꿔줍니다.
3. 기존의 부모 노드가 자식 노드로 내려갔을 때, 다시 힙 속성을 어길 수도 있습니다. 힙 속성이 충족될 때까지 1~2 단계를 반복합니다.

이때 단계 2-2를 보면 heapify 함수 내에는 두 노드의 위치를 바꿀 수 있는 기능이 필요하다는 걸 알 수 있습니다. 이런 기능을 하는 swap 이라는 함수를 미리 작성해뒀는데요.
swap 함수는 리스트로 구현한 완전 이진 트리인 tree 와 두 인덱스인 index_1과 index_2 를
파라미터로 받습니다. 그리고 트리 내에서 두 인덱스에 해당하는 두 노드의 위치를 바꿔주죠. heapify 함수의 내부 코드를 작성할 때 swap 함수를 사용해보세요.
"""


def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 부모 노드(heapify 하려는 현재 노드), 왼쪽 자식 노드, 오른쪽 자식 노드
    # 이 3가지 노드 중에서 가장 큰 값을 가진 노드가 무엇인지 파악하기

    largest = index  # 가장 큰 값 가진 노드의 인덱스 저장, 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index
    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:  # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 또 heapify 함수를 호출한다


# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify 하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)
