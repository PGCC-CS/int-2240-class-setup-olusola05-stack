# Lab 3 - Student Grade Calculator

def calculateAverage(score1, score2, score3):
    """
    Calculates and returns the average of three test scores.
    """
    average = (score1 + score2 + score3) / 3
    return round(average, 2)


def getLetterGrade(average):
    """
    Returns the letter grade based on the average score.
    """
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"


def getAcademicStanding(letter):
    """
    Returns the academic standing based on the letter grade.
    """
    if letter == "A":
        return "Excellent"
    elif letter == "B":
        return "Good"
    elif letter == "C":
        return "Satisfactory"
    elif letter == "D":
        return "Needs Improvement"
    else:
        return "Failing"


def main():
    try:
        score1 = float(input("Enter first test score: "))
        score2 = float(input("Enter second test score: "))
        score3 = float(input("Enter third test score: "))

        # Validate scores
        if not (0 <= score1 <= 100 and 0 <= score2 <= 100 and 0 <= score3 <= 100):
            print("Error: All scores must be between 0 and 100.")
            return

        average = calculateAverage(score1, score2, score3)
        letter = getLetterGrade(average)
        standing = getAcademicStanding(letter)

        print(f"\nAverage score: {average}")
        print(f"Letter grade: {letter}")
        print(f"Academic Standing: {standing}")

    except ValueError:
        print("Error: Please enter valid numeric scores.")


main()

