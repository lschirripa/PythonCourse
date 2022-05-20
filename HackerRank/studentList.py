studentList.py

if __name__ == '__main__':
    
    studentList = []
    studentsWithSecondLowestScore = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        studentList.append([name,score])
        scores.add(score)

    secondLowest = sorted(scores)[1]

    for name,score in studentList:
        if secondLowest == score:
            studentsWithSecondLowestScore.append(name)
    
    for names in sorted(studentsWithSecondLowestScore):
        print(names)