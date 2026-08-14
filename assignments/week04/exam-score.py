scores = []
for i in range(5):
    score = int(input(f"Enter score of student {i+1}: "))
    scores.append(score)
for i in range(len(scores)):
    score = scores[i]
    if score >= 50:
        print(f"student {i+1} : {score} Pass")
    else:
        print(f"student {i+1} : {score} Not")