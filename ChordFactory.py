from Chord import Chord
from ChordType import ChordType
from Interval import Interval
from Note import Note
from NoteRepo import NoteRepo


class ChordFactory:
    def __init__(self, note_repo: NoteRepo):
        perfect_interval = [0, 2, 4, 5, 7, 9, 11, 12]
        major_interval = perfect_interval
        minor_interval = [x-1 if i in {1,2,5,6} else x for i,x in enumerate(major_interval) ]
        diminished_interval = [x-1 for x in minor_interval]
        augmented_interval = [x+1 for x in major_interval]

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
        
        elif chord_type == ChordType.DOMINANT_SEVENTH:
            third = self.major_interval.get_III(root)
            fifth = self.perfect_interval.get_V(root)
            seventh = self.minor_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

        elif chord_type == ChordType.MAJOR_SEVENTH:
            third = self.major_interval.get_III(root)
            fifth = self.perfect_interval.get_V(root)
            seventh = self.major_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

        elif chord_type == ChordType.MINOR_SEVENTH:
            third = self.minor_interval.get_III(root)
            fifth = self.perfect_interval.get_V(root)
            seventh = self.minor_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

        elif chord_type == ChordType.HALF_DIMINISHED_SEVENTH:
            third = self.minor_interval.get_III(root)
            fifth = self.diminished_interval.get_V(root)
            seventh = self.minor_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

        elif chord_type == ChordType.DIMINISHED_SEVENTH:
            third = self.minor_interval.get_III(root)
            fifth = self.diminished_interval.get_V(root)
            seventh = self.diminished_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

        elif chord_type == ChordType.MINOR_MAJOR_SEVENTH:
            third = self.minor_interval.get_III(root)
            fifth = self.perfect_interval.get_V(root)
            seventh = self.major_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

        elif chord_type == ChordType.AUGMENTED_MAJOR_SEVENTH:
            third = self.major_interval.get_III(root)
            fifth = self.augmented_interval.get_V(root)
            seventh = self.major_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

        elif chord_type == ChordType.AUGMENTED_SEVENTH:
            third = self.major_interval.get_III(root)
            fifth = self.augmented_interval.get_V(root)
            seventh = self.minor_interval.get_VII(root)
            return Chord(self.get_chord_name(root, chord_type), root, third, fifth, seventh)

            

