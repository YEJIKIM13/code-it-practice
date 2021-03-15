# 08. 힙 정렬 구현하기
"""
힙 정렬을 직접 구현해보자.
어떤 리스트 하나가 있다고 합시다. 이때 그 리스트를 힙 정렬하려면
1. 먼저 리스트를 힙으로 만듭니다.
2. root 노드와 마지막 노드의 위치를 바꿉니다. 마지막 위치로 간 기존의 root 노드는 이제 힙에서 없다고 가정합니다.
3. 새로운 root 노드가 힙 속성을 지킬 수 있게 heapify합니다.
4. 힙에 남아있는 노드가 없도록 단계 2 ~ 3을 반복합니다.
힙 정렬을 하기위해 heapsort 라는 함수를 구현해볼게요. heapsort 함수는 정렬할 리스트를 tree 라는 파라미터로 받아서 힙 정렬합니다. 이때 저번 과제에서 완성한 heapify 함수를 사용할게요.
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

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:  # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 1. 먼저 리스트를 힙으로 만들기 (가장 마지막 노드부터 root 노드까지, 역순으로 heapify 해주기)
    # 마지막 노드부터 root 노드까지 heapify를 해준다
    for index in range(tree_size, 0, -1):
        heapify(tree, index, tree_size)
        """
        index 변수에는 순서대로 tree_size, tree_size - 1, tree_size - 2, tree_size - 3, …, 3, 2, 1 순으로 값이 담기게 됩니다. 
        이때 0은 포함되지 않는다는 것에 주의하세요. 
        리스트의 0번째에는 None 이 있기 때문에 heapify를 해줄 필요가 없습니다.
        이 코드가 실행되고 나면 리스트 tree는 힙이 됩니다.
        """
    for i in range(tree_size - 1, 0, -1):
        swap(tree, 1, i)  # root 노드와 마지막 노드의 위치를 바꿔줌
        heapify(tree, 1, i)  # root 노드에 heapify를 호출한다
        """
        tree_size는 현재 트리에 들어있는 총 노드의 개수를 나타냅니다. 
        heapify 함수의 내용 중 일부를 보면 tree_size는 해당 인덱스가 유효한지, 그러니까 해당 인덱스에 노드가 존재하는지를 판단하는 기준으로 사용됩니다. 
        즉, 리스트에 아무리 많은 노드들이 있다고 해도 결국 heapify의 대상은 tree_size 값을 통해 결정됩니다. 이 사실을 잘 활용하면 될 것 같은데, 어떻게 하면 좋을까요?
        매번 heapify를 호출할 때, 파라미터 tree_size도 1씩 줄여가면 됩니다. 
        그럼 힙에 맨 뒤 노드들을 무시하고 heapify를 할 수 있습니다.
        현재 i는 tree_size - 1부터 시작해서 계속 1씩 감소하는데요. 이 i를 heapify 함수의 파라미터 tree_size로 넘겨주면 heapify 함수가 인식하는 리스트의 크기가 매번 줄어듭니다. 
        즉, tree라는 전체 리스트의 사이즈는 그대로지만 실제로 heapify의 대상이 되는 리스트의 크기는 하나씩 줄어들게 되는 겁니다. 
        이렇게 하면 힙에서 맨 뒤 노드들을 하나씩 무시해주면서 나머지를 갖고 heapify할 수 있겠죠?
        """


# 실행 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)
