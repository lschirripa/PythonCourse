if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_list = student_marks[query_name]

    avg = float(sum(query_list)/len(query_list))
    
    print(f"{avg:.2f}")