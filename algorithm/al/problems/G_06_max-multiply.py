"""
힌트 1
Brute Force 방식으로 하면 가능한 모든 곱을 구한 후 비교할 수 있지만, 굉장히 비효율적입니다. Greedy Algorithm으로 비효율을 해결해 봅시다.
이 문제를 풀 때, 각 단계에서 어떤 탐욕적 선택을 할 수 있을까요?

힌트 2
이 문제에서 할 수 있는 탐욕적 선택은 각 뭉치에서 가장 큰 값을 선택하는 것입니다.
"""

def max_product(card_lists):
    # 코드를 작성하세요.
    # 누적된 곱을 저장하는 변수
    product = 1

    # 반복문을 돌면서 카드 뭉치를 하나씩 본다
    for card_list in card_lists:
        # product에 각 뭉치의 최댓값을 곱해 준다
        product *= max(card_list)

    return product


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))
