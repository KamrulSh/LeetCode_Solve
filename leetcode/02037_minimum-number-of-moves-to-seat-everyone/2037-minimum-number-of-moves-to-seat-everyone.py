class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        total = 0
        for seats, students in zip(seats, students):
            total += abs(seats - students)
        return total
