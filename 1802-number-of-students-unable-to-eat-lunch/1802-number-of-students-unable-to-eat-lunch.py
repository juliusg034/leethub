class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circle = 0
        # square = 1
        rotation = 0

        while len(students) > 0:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                rotation = 0
            else:
                back = students.pop(0)
                students.append(back)
                rotation += 1
            
            if rotation == len(students):
                break
        
        return len(students)


