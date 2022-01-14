if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score_of_the_selected_student = student_marks[query_name]
    # print(score_of_the_selected_student)
    average_mark_of_the_student = sum(score_of_the_selected_student) / 3.00
    print(format(average_mark_of_the_student, ".2f"))
