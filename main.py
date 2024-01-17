from collections import Counter
from collections import OrderedDict
import math

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
     
    def player_rank(self, rank):
        ordered_standings = self.__merge_sort(self.standings)

        return ordered_standings[rank-1]
    
    def __merge_sort(self, arr):
        pivot = math.floor(len(arr)/2)

        left_arr = self.__partition(arr, 0, pivot)
        right_arr = self.__partition(arr, pivot, len(arr))

        return self.__merge(left_arr, right_arr)

    def __partition(self, arr, start, end):
        partitioned_list = []

        for item in list(arr)[start:end]:
            partitioned_list.append(item)
        
        return partitioned_list

    def __merge(self, left, right):
        merged_arr = []

        left_index = 0
        right_index = 0

        while len(left) > left_index and len(right) > right_index:
            if self.standings[left[left_index]]['score'] < self.standings[right[right_index]]['score']:
                merged_arr.append(right[right_index])
                right.pop(right_index)
                right_index += 1
            elif self.standings[left[left_index]]['score'] == self.standings[right[right_index]]['score']:
                if self.standings[left[left_index]]['games'] <= self.standings[right[right_index]]['games']:
                    merged_arr.append(right[right_index])
                    right.pop(right_index)
                    right_index += 1
                else:
                    merged_arr.append(left[left_index])
                    left.pop(left_index)
                    left_index += 1
            else:
                merged_arr.append(left[left_index])
                left.pop(left_index)
                left_index += 1
        
        if len(left) > 0: merged_arr.extend(left[left_index:len(left)])
        if len(right) > 0: merged_arr.extend(right[right_index:len(right)])

        return merged_arr

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
