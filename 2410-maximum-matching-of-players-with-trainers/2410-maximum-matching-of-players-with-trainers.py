class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players = sorted(players)
        trainers = sorted(trainers)
        i = j = 0
        sum_pairs = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                sum_pairs += 1
                i += 1
                j += 1
            else:
                j += 1
        return sum_pairs
        