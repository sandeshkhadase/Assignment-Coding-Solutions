def find_top_student(students_scores):
  max_score = max(students_scores.values())
  
  top_student = []
  for name, score in students_scores.items():
    if score == max_score:
      top_student.append(name)
  
  return top_student
