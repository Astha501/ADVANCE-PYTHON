class Exam:
    def __init__(self):
        self.questions = {
            "Python is a ___ language": "programming",
            "2 + 2 = ?": "4"
        }

    def start_exam(self):
        score = 0

        for q in self.questions:
            ans = input(q + " : ")
            if ans == self.questions[q]:
                score += 1

        print("Your Score:", score)

exam = Exam()
exam.start_exam()