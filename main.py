from Chord import Chord
from ChordFactory import ChordFactory
from Note import Note
from ChordType import ChordType
from NoteRepo import NoteRepo

# Do some music theory
# Chord Creator

noteRepo = NoteRepo()
chordFactory = ChordFactory(noteRepo)

# note = noteRepo.get_note_by_name("C4")

# chord = chordFactory.create(note, ChordType.MAJOR)

for i in range(len(noteRepo.notes) - 10):
    note = noteRepo.get_note_by_id(i)
    print(note)
    chord = chordFactory.create(note, ChordType.MAJOR)
    print(chord)
    chord = chordFactory.create(note, ChordType.MINOR)
    print(chord)
    chord = chordFactory.create(note, ChordType.AUGMENTED)
    print(chord)
    chord = chordFactory.create(note, ChordType.DIMINISHED)
    print(chord)
    print()
    print()

# print(note)
# print(chord)
