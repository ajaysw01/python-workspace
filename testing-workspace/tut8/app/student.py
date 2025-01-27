class Student:
    def __init__(self, name, dob, branch, credits=0):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credits

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def get_credits(self):
        return self.credits

    @staticmethod
    def is_eligible_for_degree(student):
        return student.get_credits() >= 20
