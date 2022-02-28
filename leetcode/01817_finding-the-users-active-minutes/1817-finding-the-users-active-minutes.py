class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        active = {}
        answer = [0] * k
        for id, time in logs:
            if id not in active:
                active[id] = {time}
            else:
                active[id].add(time)

        for id, uam in active.items():
            ll = len(uam)
            answer[ll-1] += 1
        return answer
