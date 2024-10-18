from Chord import Chord
from ChordType import ChordType
from Interval import Interval
from Note import Note
from NoteRepo import NoteRepo


class ChordFactory:
    def __init__(self, note_repo: NoteRepo):
        interval_list = [0, 2, 4, 5, 7, 9, 11, 12]
        perfect_interval = [x if i not in {1,2,5,6} else -1 for i,x in enumerate(interval_list) ]
        major_interval = [x if i not in {0, 3, 4, 7} else -1 for i,x in enumerate(interval_list) ]
        minor_interval = [x-1 for x in major_interval]
        diminished_interval = [x-1 for x in perfect_interval]
        augmented_interval = [x+1 for x in perfect_interval]

        self.perfect_interval = Interval(perfect_interval, note_repo)
        self.major_interval = Interval(major_interval, note_repo)
        self.minor_interval = Interval(minor_interval, note_repo)
        self.diminished_interval = Interval(diminished_interval, note_repo)
        self.augmented_interval = Interval(augmented_interval, note_repo)

    def get_chord_name(self, root: Note, chord_type: ChordType):
        return f"{root.note} {chord_type.name}"

    def create(self, root: Note, chord_type: ChordType):
        if chord_type == ChordType.MAJOR:
            third = self.major_interval.get_III(root)
            fifth = self.perfect_interval.get_V(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth)

        elif chord_type == ChordType.MINOR:
            third = self.minor_interval.get_III(root)
            fifth = self.perfect_interval.get_V(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth)

        elif chord_type == ChordType.AUGMENTED:
            third = self.major_interval.get_III(root)
            fifth = self.augmented_interval.get_V(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth)

        elif chord_type == ChordType.DIMINISHED:
            third = self.minor_interval.get_III(root)
            fifth = self.diminished_interval.get_V(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth)

