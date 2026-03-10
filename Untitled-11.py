class Freelancer:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

class Client:
    def __init__(self, name):
        self.name = name

class Project:
    def __init__(self, title, freelancer):
        self.title = title
        self.freelancer = freelancer

    def show(self):
        print("Project:", self.title)
        print("Assigned to:", self.freelancer.name)

f1 = Freelancer("Rahul", "Python")
c1 = Client("Company A")

p1 = Project("Website Development", f1)
p1.show()