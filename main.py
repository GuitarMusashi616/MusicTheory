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

# print(note)
# print(chord)

# Print all chords
for i in range(len(noteRepo.notes) - 12):
    for chord_type in ChordType:
        note = noteRepo.get_note_by_id(i)
        print(note)
        chord = chordFactory.create(note, chord_type)
        print(chord)
        print()
        print()

