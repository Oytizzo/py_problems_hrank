# if __name__ == '__main__':
#     n = int(input())
#     list_of_students = []
#     for _ in range(n):
#         name = input()
#         score = float(input())
#         name_and_score = [name, score]
#         list_of_students.append(name_and_score)
#     list_of_students.sort(key=lambda item: item[1])
#     print(list_of_students)
#
#     second_lowest_student_grade = list_of_students[]

mark_sheet=[]
score_list=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark_sheet += [[name, score]]
        score_list += [score]
    b = sorted(list(set(score_list)))[1]

    for a, c in sorted(mark_sheet):
        if c == b:
            print(a)
