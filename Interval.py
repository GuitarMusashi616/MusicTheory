from Note import Note
from NoteRepo import NoteRepo

class Interval:
    def __init__(self, steps: list[int], note_repo: NoteRepo):
        self.steps = steps
        self.note_repo = note_repo


    def get_I(self, root: Note):
        new_id = root.id + self.steps[0]
        return self.note_repo.get_note_by_id(new_id)
    
    def get_II(self, root: Note):
        new_id = root.id + self.steps[1]
        return self.note_repo.get_note_by_id(new_id)
    
    def get_III(self, root: Note):
        new_id = root.id + self.steps[2]
        return self.note_repo.get_note_by_id(new_id)

    def get_IV(self, root: Note):
        new_id = root.id + self.steps[3]
        return self.note_repo.get_note_by_id(new_id)
    
    def get_V(self, root: Note):
        new_id = root.id + self.steps[4]
        return self.note_repo.get_note_by_id(new_id)

    def get_VI(self, root: Note):
        new_id = root.id + self.steps[5]
        return self.note_repo.get_note_by_id(new_id)
    
    def get_VII(self, root: Note):
        new_id = root.id + self.steps[6]
        return self.note_repo.get_note_by_id(new_id)

    def get_VIII(self, root: Note):
        new_id = root.id + self.steps[7]
        return self.note_repo.get_note_by_id(new_id)
        
