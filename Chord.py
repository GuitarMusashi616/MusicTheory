from ChordType import ChordType
from Note import Note


class Chord:
    def __init__(self, name: str, *notes: Note):
        self.name = name
        self.notes = notes

    def __repr__(self):
        return f"{self.name} ({self.notes})"

