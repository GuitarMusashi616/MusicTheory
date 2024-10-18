# 🎵 Music Theory Library 🎶

Welcome to the **Music Theory Library**! This repository is a Python-based library designed to help musicians, music theorists, and developers explore and create musical concepts programmatically. Whether you're building a music app, composing a new piece, or just curious about music theory, this library provides the tools you need to work with notes, chords, intervals, and scales.

## 📚 Features

- **Note Management**: Easily manage and retrieve musical notes with `NoteRepo`.
- **Chord Creation**: Generate various types of chords using `ChordFactory`.
- **Interval Calculation**: Calculate musical intervals with the `Interval` class.
- **Scale Enumeration**: Explore different musical scales with the `Scale` enum.
- **Chord Types**: Work with different chord types using the `ChordType` enum.

## 🛠️ Installation

To use this library, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/music-theory-library.git
cd music-theory-library
pip install -r requirements.txt
```

## 🚀 Usage

Here's a quick example of how to create a major chord using this library:

```python
from NoteRepo import NoteRepo
from ChordFactory import ChordFactory
from ChordType import ChordType

# Initialize the note repository and chord factory
note_repo = NoteRepo()
chord_factory = ChordFactory(note_repo)

# Get a note and create a major chord
note = note_repo.get_note_by_name("C4")
chord = chord_factory.create(note, ChordType.MAJOR)

print(chord)
```

## 🧪 Testing

To run the tests, use the following command:

```bash
python -m unittest discover
```

## 📂 Project Structure

- **`main.py`**: Entry point for the library, demonstrating basic usage.
- **`NoteRepo.py`**: Manages notes and provides methods to retrieve them.
- **`ChordFactory.py`**: Creates chords based on given notes and chord types.
- **`Interval.py`**: Handles interval calculations between notes.
- **`Scale.py`**: Enumerates different musical scales.
- **`ChordType.py`**: Enumerates different chord types.
- **`NoteTest.py`**: Contains unit tests for the `NoteRepo` class.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code is well-documented and includes tests.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions or feedback, please contact [yourname@example.com](mailto:yourname@example.com).

---

Enjoy exploring the world of music theory with our library! 🎼✨

---