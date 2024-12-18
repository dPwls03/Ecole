# 학생들이 답을 찍는 규칙, 득점 점수 저장하는 배열, 높은 득점 학생 저장 배열
def solution(answers) :
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

# 문제의 답과 각 학생의 패턴을 비교하여 점수 계산
    for idx, answer in enumerate(answers):
         # 학생이 패턴을 벗어나지 않고 반복적으로 답을 고르게
        if answer == student1[idx % len(student1)]:
            score[0] += 1 # 답이 맞으면 점수 + 1
        if answer == student2[idx % len(student2)]:
            score[1] += 1
        if answer == student3[idx % len(student3)]:
            score[2] += 1
        
# 최고 점수를 받은 학생을 찾기 위한 루프
    for idx, s in enumerate(score):
        
         # 현재 학생의 점수가 최고 점수와 같다면 result에 해당 학생 번호 추가
        if s == max(score):
            result.append(idx + 1)
            
    print("score:", score)
    
    # 최고 득점을 한 학생의 번호를 반환
    return result

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))


