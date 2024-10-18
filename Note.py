class Note:
    def __init__(self, id: int, note: str, octave: int):
        self.id = id
        self.note = note
        self.octave = octave

    @staticmethod
    def create(id, note, octave):
        return Note(id, note, octave)   

    def __str__(self):
        return f"{self.id}: {self.note}{self.octave}"

    def __repr__(self):
        return f"Note({self.id}: {self.note}{self.octave})"
        
