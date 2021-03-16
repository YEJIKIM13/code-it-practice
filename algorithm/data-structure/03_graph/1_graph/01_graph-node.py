class StationNode:
    """지하철 역 노드를 나타내는 클래스"""
    def __init__(self, name, num_exists):
        self.name = name
        self.num_exists = num_exists


# 지하철 역 노드 인스턴스 생성
station_0 = StationNode("교대역", 14)
station_1 = StationNode("사당역", 14)
station_2 = StationNode("종로3가역", 16)
station_3 = StationNode("서울역", 16)

# 모든 노드가 동등한 위치! (head node 나 root node 와는 다르게)

# 노드들을 파이썬 리스트에 저장
# stations = [station_0, station_1, station_2, station_3]

# 지하철 역 노드들을 파이썬 딕셔너리에 저장한다
stations = {
    "교대역": station_0,
    "사당역": station_1,
    "종로3가역": station_2,
    "서울역": station_3
}

node_1 = stations["교대역"]
node_2 = stations["서울역"]