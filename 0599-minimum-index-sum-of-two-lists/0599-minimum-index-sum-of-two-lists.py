class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {val: i for i, val in enumerate(list1)}

        min_sum = float('inf')

        output = []

        for j, val in enumerate(list2):
            if val in index_map:
                curr_sum = j + index_map[val]

                if curr_sum < min_sum:
                    min_sum = curr_sum
                    output = [val]
                elif curr_sum == min_sum:
                    output.append(val)
        return output
        