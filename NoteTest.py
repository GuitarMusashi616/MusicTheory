import unittest

from NoteRepo import NoteRepo

class NoteTest(unittest.TestCase):
    def initialize_note_repo(self):
        note_repo = NoteRepo()
        self.assertEqual(note_repo.get_note_by_id(0), "C3")
        self.assertEqual(note_repo.get_note_by_id(1), "C#3")
        self.assertEqual(note_repo.get_note_by_id(2), "D3")
        self.assertEqual(note_repo.get_note_by_id(3), "D#3")



if __name__ == '__main__':
    unittest.main()

