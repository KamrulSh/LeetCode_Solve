class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for item in strs:
            sorted_item = "".join(sorted(item))
            if sorted_item not in hashmap:
                hashmap[sorted_item] = [item]
            else:
                hashmap[sorted_item].append(item)

        # print(hashmap)
        group = []
        for val in hashmap.values():
            group.append(val)

        return group
