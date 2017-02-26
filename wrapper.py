class UserData:

    def __init__(self,name, ppid, score=0):
        self.name = name
        self.ppid = ppid
        self.score = score

    def add_score(self, score):
        return self.score + float(score)

if __name__ == '__main__':
    UserData()