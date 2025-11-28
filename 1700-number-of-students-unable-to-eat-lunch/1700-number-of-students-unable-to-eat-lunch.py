class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        cnt = Counter(students)
        for s in sandwiches:
            if cnt[s] == 0:
                break
            cnt[s] -= 1
        return sum(cnt.values())

        
            


        