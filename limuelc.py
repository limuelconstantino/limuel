def calculate_grade(score):
  """
  This function takes a score as input and returns the corresponding letter grade.

  Args:
      score: The numerical score (0-100).

  Returns:
      The letter grade (A, B, C, D, or F).
  """
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

def main():
  """
  This function gets the user's score, calculates the grade, and prints the result.
  """
  score = float(input("Enter your score (0-100): "))

  # Check for invalid score input
  if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    return

  grade = calculate_grade(score)
  print("Your grade is:", grade)

if __name__ == "__main__":
  main()
