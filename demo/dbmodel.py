class DbCourse:
    def __init__(self, id, title, duration, fee):
        self.id = id
        self.title = title
        self.duration = duration
        self.fee = fee

    def __str__(self):
        return "%s %d %d" % (self.title, self.duration, self.fee)
