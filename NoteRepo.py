from Note import Note


class NoteRepo:
    def __init__(self):
        self.note_names = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" ]
        self.octaves = range(3, 7)
        self.notes = []
        self.note_name_to_id = {}
        self.id_to_note_name = {}
        self.setup()

    def setup(self):
        self.assign_note_name_to_ids()
        self.assign_notes_to_ids()

    def assign_note_name_to_ids(self):
        for i, octave in enumerate(self.octaves):
            for j, note_name in enumerate(self.note_names):
                note = note_name + str(octave)
                id = i * len(self.note_names) + j
                self.note_name_to_id[note] = id
                self.id_to_note_name[id] = note

    def assign_notes_to_ids(self):
        for i, octave in enumerate(self.octaves):
            for j, note_name in enumerate(self.note_names):
                id = i * len(self.note_names) + j
                self.notes.append(Note(id, note_name, octave))
    
    def get_note_by_id(self, id: int):
        return self.notes[id]

    def get_note_by_name(self, name: str):
        id = self.note_name_to_id[name]
        return self.notes[id]