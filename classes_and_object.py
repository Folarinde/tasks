class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print('My name is',name, 'I am', age,'years old. My tracks are',tracks,'I scored:',score)

    def change_name(self, name):
        return name
    def change_age(self, age):
        return age
    def add_track(self, tracks): 
        return self.tracks + tracks
    def get_score(self, score):
        return score

Dele = Student('Dele', 28, ['FE','BE'],55.4)

print('My name is',Dele.change_name('Peter'),'I am',Dele.change_age(34),
'years old. My tracks are',Dele.add_track(['UI/UX']),'I scored',Dele.get_score(60.25))
