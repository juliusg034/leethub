class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = {}

        # map containing preference -> numbers of students
        for preference in students:
            counts[preference] = counts.get(preference, 0) + 1

        remaining_students = len(sandwiches)
        for sandwich in sandwiches:
            if counts.get(sandwich, 0) == 0:
                break

            remaining_students -= 1
            counts[sandwich] -= 1
        
        return remaining_students

