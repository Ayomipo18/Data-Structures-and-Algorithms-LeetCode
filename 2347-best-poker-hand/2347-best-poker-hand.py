class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks_map, suits_count, suit = {}, 0, suits[0]
        map_ans, ans = {4: "Three of a Kind", 3: "Three of a Kind", 2: "Pair", 1: "High Card"}, 1
        for i, rank in enumerate(ranks):
            if rank not in ranks_map:
                ranks_map[rank] = 0
            ranks_map[rank] += 1
            if suits[i] == suit:
                suits_count += 1
                
        if len(suits) == suits_count:
            return "Flush"
        else:
            for key, val in ranks_map.items():
                ans = max(ans, val)
                
        return map_ans[ans]