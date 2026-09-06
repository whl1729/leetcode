from typing import List

def build_max_heap(heap: List[int]):
    length = len(heap)
    for i in reversed(range(length // 2)):
        max_heapify(heap, i)

def max_heapify(heap: List[int], index: int):
    length = len(heap)
    largest, left, right = index, 2 * index + 1, 2 * index + 2
    if left < length and heap[left] > heap[largest]:
        largest = left
    if right < length and heap[right] > heap[largest]:
        largest = right
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(heap, largest)

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        distances = [-1 for _ in range(k)]
        results = [-1 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            cur_distance = abs(query[0]) + abs(query[1])
            if i < k - 1:
                distances[i] = cur_distance
                continue

            if i == k - 1:
                distances[i] = cur_distance
                build_max_heap(distances)
            elif cur_distance < distances[0]:
                distances[0] = cur_distance
                max_heapify(distances, 0)

            results[i] = distances[0]

        return results


if __name__ == "__main__":
    s = Solution()

    queries = [[984,781],[951,299],[135,109],[-430,991],[630,-831],[468,534],[13,-494],[712,600],[-970,-905],[-258,226],[137,991],[282,693],[609,892],[130,-844],[793,821],[199,-816],[185,-243],[-951,-162],[59,342],[258,797],[-139,936],[-304,-120],[982,-542],[911,315],[266,444],[206,-916],[561,840],[-50,670],[-87,433],[804,584],[191,341],[-406,-563],[-526,23],[-600,139],[594,337],[-256,60],[937,156],[-444,-150],[-602,928],[339,-564],[-576,-705],[53,-885],[-843,936],[58,-153],[56,218],[-113,26],[892,802],[315,600],[450,745],[581,804]]
    k = 15
    expected = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1875,1765,1614,1501,1461,1421,1312,1250,1250,1226,1128,1122,1122,1113,1075,1075,1055,1015,1002,975,974,969,969,931,931,903,903,903,903,739,720,710,710,710,710,710]
    result = s.resultsArray(queries, k)
    assert result == expected

    queries = [[-41,0],[34,-31],[46,-43],[-30,-39],[30,10],[-4,14],[35,3]]
    k = 4
    expected = [-1,-1,-1,89,69,65,41]
    result = s.resultsArray(queries, k)
    assert result == expected

    queries = [[7,7],[-9,4]]
    k = 2
    expected = [-1,14]
    result = s.resultsArray(queries, k)
    assert result == expected

    queries = [[1,2],[3,4],[2,3],[-3,0]]
    k = 2
    expected = [-1,7,5,3]
    result = s.resultsArray(queries, k)
    assert result == expected

    queries = [[5,5],[4,4],[3,3]]
    k = 1
    expected = [10,8,6]
    result = s.resultsArray(queries, k)
    assert result == expected