class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.tracks = kwargs.get('tracks')
        self.score = kwargs.get('score')
        # print("name:", self.name, "age:", self.age, "track:", self.tracks, "score:", self.score)
    def change_name(self, new_name):
        self.name = new_name
        # print(self.name)
    def change_age(self, new_age):
        try:
            self.age = int(new_age)
            # print(self.age)
        except:
            pass
    def add_track(self, new_track):
        self.tracks[len(self.tracks):] = [new_track] 
        # print(self.tracks)
    def get_score(self):
        return self.score
    




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
