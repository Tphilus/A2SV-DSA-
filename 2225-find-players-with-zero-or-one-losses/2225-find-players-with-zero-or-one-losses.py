class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_counts = {}
        all_players = set()

        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            
            loss_counts[loser] = loss_counts.get(loser, 0) + 1
        
        undefeated = []
        one_loss = []

        for player in all_players:
            count = loss_counts.get(player, 0)

            if count == 0:
                undefeated.append(player)
            elif count == 1:
                one_loss.append(player)
        
        return [sorted(undefeated), sorted(one_loss)]
